#!/usr/bin/python
# streeteasy, apartments.com, renthop, roomi
# rent | neighborhood | bedrooms/studio | bathrooms | address | link | status (new, down, up)

from bs4 import BeautifulSoup
import requests
import csv
import random
import time
import webbrowser
import os.path
# ensures site sees request as from browser
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42
# Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
# Googlebot/2.1 (+http://www.google.com/bot.html)
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    }

# counter for page no.
counter = 1
info = []
key = ''
# csv file
if os.path.isfile('housingNYROS.csv') == True:
    key = 'w'
else:
    key = 'a'
with open('housingNYROS.csv', key, encoding='utf8', newline='') as f: # opens (creates if not found) csv file
    writer = csv.writer(f) # writer to write to csv
    # master loop through csv
    while True:
        url="https://www.nyrentownsell.com/for-rent/nyc/%7Cprice:0-15000%7Corderby:date%7Corderbyvalue:desc%7Cpage:" + str(counter)
        page= requests.get(url, headers=headers)
        if page.status_code > 299:
            print("REQUEST INVALID")
            break
        # attains page content
        soup = BeautifulSoup(page.content, 'html.parser') # parses source code
        bodyHome = soup.find('div', class_="section") # finds wrapper of listings in soup
        lists = bodyHome.find_all('div',class_="box mb-3") # finds all listings
        # finds page
        maxpage = soup.find('ul',class_="pagination")
        maxpage = maxpage.find_all('li')
        if maxpage[len(maxpage)-1].text == '':
            maxpage = int(maxpage[len(maxpage)-2].text)
        elif maxpage[len(maxpage)-1].text == None:
            maxpage = int(maxpage[len(maxpage)-2].text)
        else:
            maxpage = int(maxpage[len(maxpage)-1].text)
        for i in lists: # finds info in list
            body = i.find('div',class_="p-2")
            link = body.find('a').get('href') # 8/8
            address = body.find('h4').text.replace('\n','')
            name = "RENT OWN SELL NEW YORK LISTING"
            temp = body.find('p',class_="graytext").text
            neighborhood = temp.split('*')[1][1:].replace('\n','')
            price = body.find('span',class_='doller').text.replace('$','').replace(',','').replace('\n','')
            temp = body.find('span',class_='span2').text.replace('No Fee','')
            temp = temp.split(' | ')
            beds = temp[0].replace('\n','')
            baths = temp[1].replace('\n','')
            area = ""
            info = [name.replace('"',''), address.replace('"',''), neighborhood.replace('"',''), price.replace('"',''), beds.replace('"',''), baths.replace('"',''), area.replace('"',''), link.replace('"','')] # compiles first listing to list
            writer.writerow(info) # writes to csv
        if counter == maxpage:
            break
        else:
            if len(info) == 0:
                print("CAPTCHA NEEDED HERE, BROKE AT PAGE # " + str(counter) +"!")
                break
            counter = counter + 1
            continue
