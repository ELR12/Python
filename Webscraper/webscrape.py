# Created by Ethan Roberts
# on 12/13/2020

# This is a webscraping program where I scrape the latest monitor prices on newegg.com.

import requests
from bs4 import BeautifulSoup
from csv import writer

# url = 'https://www.newegg.com/p/pl?N=100160979%20600557170%20601305587&page=1'
# response = requests.get(url)  # must read 200 which means successfully connected to website
# src = response.content  #contains the source-code of the website
# soup = BeautifulSoup(src, 'html.parser')

with open('monitorPrices.csv', 'w') as csv_file:  # write to csv
    csv_writer = writer(csv_file)
    fileHeaders = ['Monitor Info', 'Regular Price', 'Current Price']
    csv_writer.writerow(fileHeaders)

    # loop through pages 1 - 4 of the website and scrape data
    for i in range(1, 5):
        url = 'https://www.newegg.com/p/pl?N=100160979%20600557170%20601305587&page={}'.format(i)
        response = requests.get(url)  # must read 200 which means successfully connected to website
        src = response.content  # contains the source-code of the website
        soup = BeautifulSoup(src, 'html.parser')

        item_info = {'class': 'item-info'}
        item_action = {'class': 'item-action'}
        itemInfo_array = soup.find_all(attrs = item_info)  # returns an array of html to loop thr
        itemAction_array = soup.find_all(attrs = item_action)  # returns an array of html to loop thr

        # loop through the current page you're on
        for i, (a, b) in enumerate(zip(itemInfo_array, itemAction_array)):
            itemName = a.find('a', class_= 'item-title').get_text()
            oldPrice = b.find("span", class_= "price-was-data")
            newPrice = b.find("span", class_= "price-current-label")
            if (oldPrice is not None):
                oldPrice = oldPrice.get_text()
            if (newPrice is not None):
                newPrice = "$" +  newPrice.findNext().get_text()
            csv_writer.writerow([itemName, oldPrice, newPrice])
