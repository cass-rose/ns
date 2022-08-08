import requests
# from xml.etree import ElementTree
import xmltodict
import re

def getDict(headers={'User-agent': 'Synstylae: (https://github.com/cass-rose/ns), nation: https://www.nationstates.net/nation=synstylae'}):
    headers = {
        'User-agent': 'Synstylae: (https://github.com/cass-rose/ns), nation: https://www.nationstates.net/nation=synstylae'
    }

    response = requests.get(
        "https://www.nationstates.net/cgi-bin/api.cgi?q=happenings;filter=founding", headers=headers
    )
    treeDict=xmltodict.parse(response.content)
    natHapps=treeDict['WORLD']['HAPPENINGS']['EVENT']
    d=0
    nations=[]
    temp=''
    for hap in natHapps:
        d+=1
        temp+=re.findall('\@@(.*?)\@',hap['TEXT'])[0]+','
        if (d%8)==0:
            nations.append(temp)
            temp=''

    return nations

def main():
    nats=getDict()
    print(nats)

main()
