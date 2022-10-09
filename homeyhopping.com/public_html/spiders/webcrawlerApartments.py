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
headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42"}

# counter for page no.
counter = 1
info = []
key = ''
# csv file
if os.path.isfile('housingA.csv') == True:
    key = 'w'
else:
    key = 'a'
with open('housingA.csv', key, encoding='utf8', newline='') as f: # opens (creates if not found) csv file
    writer = csv.writer(f) # writer to write to csv
    # master loop through csv
    decrement = 0
    while True:
        url="https://www.apartments.com/new-york-ny/" + str(counter) + "/?bb=3v14s7s5wHjj5q50G"
        page= requests.get(url, headers=headers)
        if page.status_code > 299:
            print("REQUEST INVALID")
            break
        # attains page content
        soup = BeautifulSoup(page.content, 'html.parser') # parses source code
        lists = soup.find_all('li', class_="mortar-wrapper") # finds class of listings in list
        # finds page
        maxpage = soup.find('span',class_='pageRange').text
        maxpage = int(maxpage[len(maxpage)-2:len(maxpage)])
        for i in lists: # finds info in list
            link = i.find('a',class_="property-link").get('href') # 8/8
            tempPage= requests.get(link, headers=headers)
            if tempPage.status_code > 299:
                print("REQUEST INVALID")
                break
            stew = BeautifulSoup(tempPage.content, 'html.parser') # parses source code
            tempAddress = stew.find('div', class_='propertyAddressContainer')
            name = stew.find('h1',class_='propertyName').text.replace('\r','').replace('\n','')
            address = tempAddress.find('span').text # 2/8 part 1
            try:
                body = stew.find('div', class_ = 'tab-section active')# there's a debug duplicate of all listings in the page, this filters that out
                listingsSingle = body.find_all('div', class_ = "pricingGridItem multiFamily ") # for listings w/ only one apartment per qualification, it hosts a different div
                for n in listingsSingle:
                    amenities = n.find('span',class_='detailsTextWrapper')
                    temp = amenities.find_all('span')
                    beds = temp[0].text # 5/8
                    baths = temp[1].text # 6/8
                    area = temp[2].text.replace('sq','').replace('ft','').replace(' ','') # 7/8
                    price = listingsSingle.find('span','rentLabel').text.replace('$','').replace(',','')
                    info = [name.replace('"',''), address.replace('"',''), neighborhood.replace('"',''), price.replace('"',''), beds.replace('"',''), baths.replace('"',''), area.replace('"',''), link.replace('"','')] # compiles to list
                    writer.writerow(info) # writes to csv
                listings = body.find_all('div',class_='pricingGridItem multiFamily hasUnitGrid')
                neighborhood = stew.find('a',class_='neighborhood').text # 3/8
                tempAddress = stew.find('div', class_='propertyAddressContainer')
                address = tempAddress.find('span').text # 2/8 part 1
                for n in listings:
                    amenities = n.find('span',class_='detailsTextWrapper')
                    temp = amenities.find_all('span')
                    beds = temp[0].text # 5/8
                    baths = temp[1].text # 6/8
                    area = temp[2].text.replace('sq','').replace('ft','').replace(' ','') # 7/8
                    apts = n.find_all('li', class_='unitContainer js-unitContainer')
                    for a in apts:
                        price = a.get('data-maxrent') # 4/8
                        realaddress = address + " #" + a.get('data-unit') # 2/8 part 2
                        info = [name.replace('"',''), address.replace('"',''), neighborhood.replace('"',''), price.replace('"',''), beds.replace('"',''), baths.replace('"',''), area.replace('"',''), link.replace('"','')] # compiles to list
                        for x in info:
                            x.replace('"','')
                        writer.writerow(info) # writes to csv
                    apts2 = n.find_all('li',class_='unitContainer js-unitContainer hideOnCollapsed')
                    for a in apts2:
                        if len(apts2) < 1:
                            break
                        elif apts2 == None:
                            break
                        else:
                            price = a.get('data-maxrent') # 4/8
                            realaddress = address + " #" + a.get('data-unit') # 8/8 pt 2
                            info = [name.replace('"',''), address.replace('"',''), neighborhood.replace('"',''), price.replace('"',''), beds.replace('"',''), baths.replace('"',''), area.replace('"',''), link.replace('"','')] # compiles to list
                            writer.writerow(info) # writes to csv
            except:
                body = stew.find_all('div','priceBedRangeInfoContainer')
                for n in body:
                    temp = n.find_all('p',class_='rentInfoDetail')
                    price = temp[0].text.replace('$','').replace(',','')
                    beds = temp[1].text.replace('bd','').replace(' ','')
                    baths = temp[2].text.replace('ba','').replace(' ','')
                    if temp[3] == "" or temp[3] == None:
                        info = [name.replace('"',''), address.replace('"',''), neighborhood.replace('"',''), price.replace('"',''), beds.replace('"',''), baths.replace('"',''), area.replace('"',''), link.replace('"','')] # compiles to list
                        writer.writerow(info) # writes to csv
                    else:
                        area = temp[3].text.replace('bd','').replace(' ','')
                        info = [name.replace('"',''), address.replace('"',''), neighborhood.replace('"',''), price.replace('"',''), beds.replace('"',''), baths.replace('"',''), area.replace('"',''), link.replace('"','')] # compiles to list
                        writer.writerow(info) # writes to csv
        if counter == maxpage:
            break
        else:
            if len(info) == 0:
                print("CAPTCHA NEEDED HERE, BROKE AT PAGE # " + str(counter) +"!")
                break
            counter = counter + 1
            continue
