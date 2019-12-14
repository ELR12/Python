# Created by Ethan Roberts
# on 12/14/2019

# This is a webscraping program where I scrape the latest monitor prices on newegg.com.  
# I am using this program to teach myself webscraping fundamentals as well as Python programming langauage.

import requests
from bs4 import BeautifulSoup
from csv import writer


url = 'https://www.newegg.com/p/pl?Submit=ENE&IsNodeId=1&N=100160979%20600557170%20601305587&cm_sp=CAT_Monitors_2-_-VisNav-_-4K-42-Monitors_2'
response = requests.get(url)
src = response.content  #contains the source-code of the website
soup = BeautifulSoup(src, 'html.parser') 

with open('monitorPrices.csv', 'w') as csv_file:    #write to csv
	csv_writer = writer(csv_file)
	fileHeaders = ['Monitor Info', 'Regular Price', 'Current Price']
	csv_writer.writerow(fileHeaders)

	for item in soup.select('.item-info'):  #using soup.select, could've used soup.findAll
		itemName = item.find('a', class_='item-title').get_text()
		regPrice = item.find('li', class_='price-was').get_text()
		newPrice = item.find('li', class_='price-current').get_text()
		csv_writer.writerow([itemName, regPrice, newPrice])
	