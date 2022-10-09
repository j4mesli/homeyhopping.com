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
if os.path.isfile('housingAF.csv') == True:
    key = 'w'
else:
    key = 'a'
with open('housingAF.csv', key, encoding='utf8', newline='') as f: # opens (creates if not found) csv file
    writer = csv.writer(f) # writer to write to csv
    # master loop through csv
    decrement = 0
    while True:
        url="https://www.apartmentfinder.com/New-York/New-York-Apartments/Page" + str(counter)
        page= requests.get(url, headers=headers)
        if page.status_code > 299:
            print("REQUEST INVALID")
            break
        # attains page content
        soup = BeautifulSoup(page.content, 'html.parser') # parses source code
        bodyHome = soup.find('ol', class_="layout-row layout-wrap") # finds wrapper of listings in soup
        lists = bodyHome.find_all('li') # finds all listings
        # finds page
        maxpage = soup.find('span',class_='pageRange').text
        maxpage = int(maxpage[len(maxpage)-2:len(maxpage)])
        for i in lists: # finds info in list
            tempLink = i.find('h2',class_="flex-12 ellipses layout-hidden-xs desktop-title")
            link = tempLink.find('a').get('href') # 8/8
            tempPage= requests.get(link, headers=headers)
            if tempPage.status_code > 299:
                print("REQUEST INVALID")
                break
            stew = BeautifulSoup(tempPage.content, 'html.parser') # parses source code
            address = stew.find('h2', class_='profile-mailing-address').text
            tempname = stew.find('div',class_='name')
            name = tempname.find('h1').text
            neighborhood = stew.find('span',class_="neighborhood").find_all('a')[1].text
            try:
                body = stew.find('div', class_ = 'tab-content active')# there's a debug duplicate of all listings in the page, this filters that out
                firstListing = body.find('div', class_="row rentalGridRow bold first") # find first listing
                if firstListing == None:
                    firstListing = body.find('div', class_="row rentalGridRow first") # find first listing
                    if firstListing == None:
                        firstListing = body.find('div', class_="row rentalGridRow bold first hasUnitDescription") # find first listing
                        if firstListing == None:
                            firstListing = body.find('div', class_="row rentalGridRow first hasUnitDescription") # find first listing
                beds = firstListing.get('data-beds')
                if int(beds) == 0:
                    beds = "Studio"
                baths = firstListing.get('data-baths')
                price = firstListing.get('data-maxrent')
                temp = firstListing.find('div',class_='md-2 sqft hide-sm')
                if temp==None:
                    temp = firstListing.find('div',class_='md-3 sqft hide-sm')
                area = temp.find('span').text.replace(' ','').replace('Sq','').replace('Ft','').replace(',','').replace('\r','').replace('\n','')
                unit = firstListing.get('data-unit').replace('Apartment ','').replace('#','')
                if unit == "":
                    thisaddress = address
                elif unit == None:
                    thisaddress = address
                else:
                    thisaddress = address + " #" + unit
                info = [name.replace('"',''), thisaddress.replace('"',''), neighborhood.replace('"',''), price.replace('"',''), beds.replace('"',''), baths.replace('"',''), area.replace('"',''), link.replace('"','')] # compiles first listing to list
                writer.writerow(info) # writes to csv
                listings = body.find_all('div',class_='row rentalGridRow bold') # find listings not hidden
                if listings == None:
                    listings = body.find_all('div',class_='row rentalGridRow') # find listings not hidden
                    if listings == None:
                        listings = body.find_all('div',class_='row rentalGridRow bold hasUnitDescription') # find listings not hidden
                        if listings == None:
                            listings = body.find_all('div',class_='row rentalGridRow hasUnitDescription') # find listings not hidden
                for n in listings:
                    beds = n.get('data-beds')
                    if int(beds) == 0:
                        beds = "Studio"
                    baths = n.get('data-baths')
                    price = n.get('data-maxrent')
                    temp = n.find('div',class_='md-2 sqft hide-sm')
                    if temp==None:
                        temp = firstListing.find('div',class_='md-3 sqft hide-sm')
                    area = temp.find('span').text.replace(' ','').replace('Apartment ','').replace('Sq','').replace('Ft','').replace(',','').replace('\r','').replace('\n','')
                    unit = n.get('data-unit').replace('Apartment ','').replace('#','')
                    if unit == "":
                        thisaddress = address
                    elif unit == None:
                        thisaddress = address
                    else:
                        thisaddress = address + " #" + unit
                    info = [name.replace('"',''), thisaddress.replace('"',''), neighborhood.replace('"',''), price.replace('"',''), beds.replace('"',''), baths.replace('"',''), area.replace('"',''), link.replace('"','')] # compiles first listing to list
                    writer.writerow(info) # writes to csv
                listings = body.find_all('div',class_='row rentalGridRow hideOnCollapsed bold') # finds hidden listings
                if listings == None:
                    listings = body.find_all('div',class_='row rentalGridRow hideOnCollapsed') # finds hidden listings
                    if listings == None:
                        listings = body.find_all('div',class_='row rentalGridRow hideOnCollapsed bold hasUnitDescription') # finds hidden listings
                        if listings == None:
                            listings = body.find_all('div',class_='row rentalGridRow hideOnCollapsed hasUnitDescription') # finds hidden listings
                for n in listings:
                    beds = n.get('data-beds')
                    if int(beds) == 0:
                        beds = "Studio"
                    baths = n.get('data-baths')
                    price = n.get('data-maxrent')
                    temp = n.find('div',class_='md-2 sqft hide-sm')
                    if temp==None:
                        temp = firstListing.find('div',class_='md-3 sqft hide-sm')
                    area = temp.find('span').text.replace(' ','').replace('Apartment ','').replace('Sq','').replace('Ft','').replace(',','').replace('\r','').replace('\n','')
                    unit = n.get('data-unit').replace('Apartment ','').replace('#','')
                    if unit == "":
                        thisaddress = address
                    elif unit == None:
                        thisaddress = address
                    else:
                        thisaddress = address + " #" + unit
                    info = [name.replace('"',''), thisaddress.replace('"',''), neighborhood.replace('"',''), price.replace('"',''), beds.replace('"',''), baths.replace('"',''), area.replace('"',''), link.replace('"','')] # compiles first listing to list
                    writer.writerow(info) # writes to csv
            except:
                body = stew.find('div', class_='js-expandableContainer expandableContainer collapsed')
                listing = body.find('div', class_='row rentalGridRow bold first')
                if listing == None:
                    listing = body.find('div', class_='row rentalGridRow first')
                    if listing == None:
                        listing = body.find('div', class_='row rentalGridRow first hasUnitDescription')
                        if listing == None:
                            listing = body.find('div', class_='row rentalGridRow bold first hasUnitDescription')
                beds = listing.get('data-beds')
                if int(beds) == 0:
                    beds = "Studio"
                baths = listing.get('data-baths')
                price = listing.get('data-maxrent')
                temp = listing.find('div',class_='md-2 sqft hide-sm')
                if temp==None:
                    temp = listing.find('div',class_='md-3 sqft hide-sm')
                area = temp.find('span').text.replace(' ','').replace('Apartment ','').replace('Sq','').replace('Ft','').replace(',','').replace('\r','').replace('\n','')
                unit = listing.get('data-unit').replace('Apartment ','').replace('#','')
                if unit == "":
                    thisaddress = address
                elif unit == None:
                    thisaddress = address
                else:
                    thisaddress = address + " #" + unit
                info = [name.replace('"',''), thisaddress.replace('"',''), neighborhood.replace('"',''), price.replace('"',''), beds.replace('"',''), baths.replace('"',''), area.replace('"',''), link.replace('"','')] # compiles first listing to list
                writer.writerow(info) # writes to csv
        if counter == maxpage:
            print("DONE")
            break
        else:
            if len(info) == 0:
                print("CAPTCHA NEEDED HERE, BROKE AT PAGE # " + str(counter) +"!")
                break
            counter = counter + 1
            continue
