#!/usr/bin/python3.10
import datetime
import json
from github import Github

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
text = ""
with open('heading.ejs','r') as page:
    for line in page:
        line = line.replace(',,',', ,')
        if "dateTime" in line:
            line = "				<h5 class=\"menuTitle\" style=\"color: #202020; margin-bottom: 0vw;\">Last Updated On: <span id='dateTime'>" + updateTime +"</span></h5>\n"
        elif "<tbody>" in line:
            break
        text = text + line
with open('heading.ejs','w') as page:
    page.write(text)
print("DONE WITH CHANGING PAGE")

# GitHub
g = Github("")
repo = g.get_user().get_repo("homeyhopping.com")
heading = repo.get_contents('views/partials/heading.ejs')
jsonFile = repo.get_contents('public/json/entries.json')
print(repo)
print(jsonFile)
print(heading)
jsondata = ""
count = 0
for i in total:
    count = count + 1
    temp = json.dumps(i)
    if jsondata == "":
        jsondata = "[" + jsondata + temp
    elif count == len(total):
        jsondata = jsondata + "," + temp + "]"
    else:
        jsondata = jsondata + "," + temp
# update ejs
repo.update_file(heading.path, "Automatic update to heading.ejs 'last updated on' span via GitHub API", text, heading.sha, branch="main")
print("heading done")
# update json
repo.update_file(jsonFile.path, "Automatic update to listings.json time span via GitHub API", jsondata, jsonFile.sha, branch="main")
print("json done")
