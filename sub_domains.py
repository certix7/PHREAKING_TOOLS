import requests,json

site=input("pls put your site to revers :")

url="https://domains.yougetsignal.com/domains.php "
headers={
'Host':' domains.yougetsignal.com',
'Referer':' https://www.yougetsignal.com/tools/web-sites-on-web-server/',
'Origin':' https://www.yougetsignal.com',
}

data='remoteAddress={0}&key='.format(site)

response = requests.post('https://domains.yougetsignal.com/domains.php', params=data)
data=json.loads(response.text)
with open("NASER_bugs.txt","w") as f:
    #
    de=data["domainArray"]
    
    for i in de:
        for x in i:
            print(x,file=f,end="")


