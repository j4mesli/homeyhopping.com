import datetime
import json
import ftplib
from ftplib import FTP_TLS

total = []
with open('housingA.csv','r') as fileA:
    for x in fileA:
        x = x.replace(',,',', ,')
        x = x.split(',')
        temp = "$" + x[3].replace(' ','').replace(',','').replace('$','')
        if temp == "$" or temp == "$ ":
            temp = " "
        total.append({
            'name': x[0].replace('  ',''),
            'address': x[1],
            'neighborhood': x[2],
            'price': temp,
            'beds': x[4],
            'baths': x[5],
            'area': x[6],
            'link': x[7]
        })
        print(x)
        print("A #" + fileA.index(x) + " DONE")
print("A DONE")
with open('housingAF.csv','r') as fileAF:
    for x in fileAF:
        x = x.replace(',,',', ,')
        x = x.split(',')
        temp = "$" + x[3].replace(' ','').replace(',','').replace('$','')
        if temp == "$" or temp == "$ ":
            temp = " "
        total.append({
            'name': x[0].replace('  ',''),
            'address': x[1],
            'neighborhood': x[2],
            'price': temp,
            'beds': x[4],
            'baths': x[5],
            'area': x[6],
            'link': x[7]
        })
        print(x)
        print("AF #" + fileAF.index(x) + " DONE")
print("AF DONE")
with open('housingNYROS.csv','r') as fileNYROS:
    counter = 0
    for x in fileNYROS:
        x = x.replace(',,',', ,')
        x = x.split(',')
        temp = "$" + x[3].replace(' ','').replace(',','').replace('$','')
        if temp == "$" or temp == "$ ":
            temp = " "
        total.append({
            'name': x[0].replace('  ',''),
            'address': x[1],
            'neighborhood': x[2],
            'price': temp,
            'beds': x[4],
            'baths': x[5],
            'area': x[6],
            'link': x[7]
        })
        print(x)
        counter += 1
        print("NYROS #" + str(counter) + " DONE")
print("NYROS DONE")
with open('entries.json', 'w') as entries:
    json.dump(total , entries)
print("JSON DUMP DONE")
time = datetime.datetime.now()
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
hour = ""
ampm = ""
minute = ""
second = ""
if time.hour == 0:
    ampm = "AM"
    hour = "12"
elif time.hour < 12:
    ampm = "AM"
    hour = str(time.hour)
elif time.hour == 12:
    ampm = "PM"
    hour = str(time.hour)
else:
    ampm = "PM"
    hour = str(time.hour - 12)
if time.minute < 10:
    minute = "0" + str(time.minute)
else:
    minute = str(time.minute)
if time.second < 10:
    second = "0" + str(time.second)
else:
    second = str(time.second)
updateTime = months[time.month - 1] + " " + str(time.day) + ", " + str(time.year) + " at " + hour + ":" + minute + ":" + second + " " + ampm +"."
with open('table.ejs','r') as page:
    for line in page:
        line = line.replace(',,',', ,')
        if "dateTime" in line:
            line = "				<h5 class=\"menuTitle\" style=\"color: #202020; margin-bottom: -1vw;\">Last Updated On: <span id='dateTime'>" + updateTime +"</span></h5>\n"
        elif "<tbody>" in line:
            break
        text = text + line
with open('table.ejs','w') as page:
    page.write(text)
print("DONE WITH CHANGING PAGE")
with open('keysHH.txt','w') as keys:
    host = keys[0]
    port = keys[1]
    user = keys[2]
    password = keys[3]
ftps = FTP_TLS()
ftps.connect(host, port)
# Output: '220 Server ready for new user.'
ftps.login(user, password)
# Output: '230 User usr logged in.'
list = ftps.nlst()
for i in list:
    if i == "index.php":
        ftpDelete = ftps.delete("index.php")
file = open('table.ejs','rb')
ftps.storbinary('STOR table.ejs', file)
list = ftps.nlst()
file = open('entries.json','rb')
ftps.storbinary('STOR entries.json', file)
print(list)
# Output: ['mysubdirectory', 'mydoc']
ftps.quit()
print("DONE CERT")
