import os
import requests
import re

url = input("Enter URL (http(s)://website.com) : ")
res = requests.get(url).text
pwd = os.getcwd()
fileaddr = os.path.join(pwd, "index.html")
with open(fileaddr, 'w+', encoding='utf-8') as f:
    result = re.sub('((?<=((href=")))|(?<=((src="))))/(.+?)(?=")',
                    url+'/'+r'\6', res)
    f.seek(0)
    f.write(result)

for i in range(2):
    pid = os.fork()
    if pid == 0:
        os.system('python3 -m http.server 2020')
    else:
        os.system('./ngrok http 2020')