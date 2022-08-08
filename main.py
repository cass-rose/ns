from getnats import getDict
import json
from time import sleep

def setup(headers, template, main):
    print(f"Welcome, {main}! Let's get started!")
    cont=True
    while cont==True:
        nations=getDict(headers)
        if len(nations):
            print("Since we last checked, these are the newest nations that haven't been tg'ed yet!\n")
        else:
            print("It seems there aren't any new nations! Maybe wait a bit.")
        for set in nations:
            print(f"https://www.nationstates.net/page=compose_telegram?tgto={set}&message={template}")
            print("____________________________________________________________________________________________________________________________________________________________________________________________\n")
            print("Please copy and paste this link into your browser and hit 'Send'. You will have to wait between 40 and 100 seconds before you can send the next batch, assuming you have sent 8 telegrams.\n")

        a=input("Would you like to quit? If not, the program will run again. Y/N?")
        if a.lower()=='y' or a.lower()=='yes':
            cont=False

    print("Have a great day!")


def main():
    try:
        with open("config.json", "r") as f:
            info= json.load(f)
            main=info["main"]
            template=info["template"]

    except json.decoder.JSONDecodeError:
        print("The file is incorrect!")
        return
    if "code" in template:
        print("Please put your template code in the config.json file.")
        quit()
    headers = {
        'User-agent': f'Snag, by Synstylae(https://github.com/cass-rose/ns), nation running the script is : https://www.nationstates.net/nation={main}.'}

    setup(headers, template, main)

main()
