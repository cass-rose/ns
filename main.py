from getnats import getDict
import json
from time import sleep
import PySimpleGUI as gui
import requests

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
    except FileNotFoundError:
        with open("config.json", "w", encoding="utf-8") as json_file:
            json_file.write(requests.get("https://gist.githubusercontent.com/cass-rose/f5c22bf635af4f08d8f130bf2279b3cc/raw/1883044c3b6fb09a6d69d108e46b50dcc904237b/config.json").text)
    if "code" in template:
        print("Please put your template code in the config.json file.")
        quit()
    headers = {
        'User-agent': f'Snag, by Synstylae(https://github.com/cass-rose/ns), nation running the script is : https://www.nationstates.net/nation={main}.'}

    setup(headers, template, main)
if __name__ == '__main__':
    main()
