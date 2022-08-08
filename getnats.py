import requests
# from xml.etree import ElementTree
import xmltodict
import re

def getDict(headers={'User-agent': f'Snag, by Synstylae(https://github.com/cass-rose/ns), No nation data is available.'}):
    response = requests.get(
        "https://www.nationstates.net/cgi-bin/api.cgi?q=happenings;filter=founding", headers=headers
    )
    treeDict=xmltodict.parse(response.content)
    natHapps=treeDict['WORLD']['HAPPENINGS']['EVENT']
    d=0
    nations=[]
    temp=''
    with open("last.txt", "r") as f:
        last=f.read()
    notUsed=True
    for hap in natHapps:
        d+=1
        nat=re.findall('\@@(.*?)\@',hap['TEXT'])[0]
        if nat== last:
            notUsed=False
        if nat != last and notUsed:
            temp+=(nat+',')
        if (d%8)==0 and len(temp):
            nations.append(temp)
            temp=''
        if d==1:
            with open("last.txt", "w") as f:
                f.write(nat)
    return nations
#
# def main():
#     nats=getDict()
#     print(nats)
# #
# main()
