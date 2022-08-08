import requests
# from xml.etree import ElementTree
import xmltodict
import re

def getDict():
    headers = {
        'User-agent': 'Synstylae(developer: +https://github.com/cass-rose/ns)'
    }

    response = requests.get(
        "https://www.nationstates.net/cgi-bin/api.cgi?q=happenings;filter=founding;limit=8", headers=headers
    )
    # f=open('response.txt','w')
    # f.write(response.text)
    # f.close()
    treeDict=xmltodict.parse(response.content)
    # print(treeDict)
    natHapps=treeDict['WORLD']['HAPPENINGS']['EVENT']
    for hap in natHapps:
        print(re.findall('\@@(.*?)\@',hap['TEXT'])[0]+',')

getDict()
