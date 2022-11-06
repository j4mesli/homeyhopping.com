import datetime
import ftplib
from ftplib import FTP_TLS

name = []
address = []
neighborhood = []
beds = []
baths = []
area = []
price = []
link = []
text=""
ending="						</tbody>\n					</table>\n				</div>\n				<button href=\"#\" id=\"load\" class=\"loadMore\">Load More </button>\n			</div>\n		</div>\n	</body>\n</html>\n"
with open('housingA.csv','r') as fileA:
    for x in fileA:
        x = x.replace(',,',', ,')
        x = x.split(',')
        name.append(x[0].replace('  ',''))
        address.append(x[1])
        neighborhood.append(x[2])
        temp = "$" + x[3].replace(' ','').replace(',','').replace('$','')
        if temp == "$":
            price.append(" ")
        elif temp == "$ ":
            price.append(" ")
        else:
            price.append(temp)
        beds.append(x[4])
        baths.append(x[5])
        area.append(x[6])
        link.append(x[7])
with open('housingAF.csv','r') as fileAF:
    for y in fileAF:
        y = y.replace(',,',', ,')
        y = y.split(',')
        name.append(y[0].replace('  ',''))
        address.append(y[1])
        neighborhood.append(y[2])
        temp = "$" + y[3].replace(' ','').replace(',','').replace('$','')
        if temp == "$":
            price.append(" ")
        elif temp == "$ ":
            price.append(" ")
        else:
            price.append(temp)
        beds.append(y[4])
        baths.append(y[5])
        area.append(y[6])
        link.append(y[7])
with open('housingNYROS.csv','r') as fileNYROS:
    for z in fileNYROS:
        z = z.replace(',,',', ,')
        z = z.split(',')
        name.append(z[0].replace('  ',''))
        address.append(z[1])
        neighborhood.append(z[2])
        temp = "$" + z[3].replace(' ','').replace(',','').replace('$','')
        if temp == "$":
            price.append(" ")
        elif temp == "$ ":
            price.append(" ")
        else:
            price.append(temp)
        beds.append(z[4])
        baths.append(z[5])
        temp = z[6]
        area.append(z[6])
        link.append(z[7])
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
with open('index.php','r') as page:
    for line in page:
        line = line.replace(',,',', ,')
        if "dateTime" in line:
            line = "				<h5 class=\"menuTitle\" style=\"color: #202020; margin-bottom: -1vw;\">Last Updated On: <span id='dateTime'>" + updateTime +"</span></h5>\n"
        elif "<tr class=\"listings\" name=\"listings\" id=\"listings\">" in line:
            break
        text = text + line
temp = 0
while temp < len(name):
    listing = "							<tr class=\"listings\" name=\"listings\" id=\"listings\">\n				    			<td id=\"name\" class=\"normal\"><p class=\"listings\" name =\"listings\" id=\"listings\">" + name[temp] +"</p></td>\n			    				<td id=\"address\" class=\"normal\"><p class=\"listings\" name =\"listings\" id=\"listings\">" + address[temp] + "</p></td>\n   								<td id=\"neighborhood\" class=\"normal\"><p class=\"listings\" name =\"listings\" id=\"hide\">" + neighborhood[temp] + "</p></td>\n								<td id=\"beds\" class=\"normal\"><p class=\"listings\" name =\"listings\" id=\"listings\">" + beds[temp] + "</p></td>\n								<td id=\"baths\" class=\"normal\"><p class=\"listings\" name =\"listings\" id=\"hide\">" + baths[temp] + "</p></td>\n								<td id=\"area\" class=\"normal\"><p class=\"listings\" name =\"listings\" id=\"hide\">" + area[temp] + "</td>\n								<td id=\"price\" class=\"normal\"><p class=\"listings\" name =\"listings\" id=\"listings\">" + price[temp] + "</p></td>\n								<td id=\"link\" class=\"normal\"><a class=\"listings\" id=\"listings\" name=\"listings\" href=\"" + link[temp].replace('\n','') + "\">Link</a></td>\n   						    </tr>\n"
    text = text + listing
    temp = temp + 1
text = text + ending
page.close()
#with open('index.html','w') as page:
#    page.write(text)
#page.close()
with open('index.php','w') as page:
    page.write(text)
page.close()
print("DONE WITH CHANGING PAGE")
host = ''
port = 
user = ''
password = ''
ftps = FTP_TLS()
ftps.connect(host, port)
# Output: '220 Server ready for new user.'
ftps.login(user, password)
# Output: '230 User usr logged in.'
list = ftps.nlst()
for i in list:
    if i == "index.php":
        ftpDelete = ftps.delete("index.php")
file = open('index.php','rb')
ftps.storbinary('STOR index.php', file)
list = ftps.nlst()
print(list)
# Output: ['mysubdirectory', 'mydoc']
ftps.quit()
print("DONE CERT")
