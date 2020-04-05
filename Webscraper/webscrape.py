# Created by Ethan Roberts
# on 12/14/2019

# This is a webscraping program where I scrape the latest monitor prices on newegg.com.  
# I am using this program to teach myself webscraping fundamentals as well as Python programming langauage.

import requests
from bs4 import BeautifulSoup
from csv import writer


#url = 'https://www.newegg.com/p/pl?N=100160979%20600557170%20601305587&page=1'
#response = requests.get(url)  # must read 200 which means successfully connected to website
#src = response.content  #contains the source-code of the website
#soup = BeautifulSoup(src, 'html.parser') 


with open('monitorPrices.csv', 'w') as csv_file:    #write to csv
	csv_writer = writer(csv_file)
	fileHeaders = ['Monitor Info', 'Regular Price', 'Current Price']
	csv_writer.writerow(fileHeaders)

	# loop through pages 1 - 3 of the website and scrape data
	for i in range(1, 4):
		url = 'https://www.newegg.com/p/pl?N=100160979%20600557170%20601305587&page={}'.format(i)
		response = requests.get(url)  # must read 200 which means successfully connected to website
		src = response.content  #contains the source-code of the website
		soup = BeautifulSoup(src, 'html.parser') 
        
		#loop through the current page your on
		for item in soup.select('.item-info'):  #using soup.select, could've used soup.findAll
			itemName = item.find('a', class_='item-title').get_text()
			dollarAmount = item.find('span', class_='price-current-label').findNext('strong').get_text()
			cents = item.find('span', class_='price-current-label').findNext('sup').get_text()
			newPrice = dollarAmount + cents
			if (item.find('span', class_='price-was-data')):
				regPrice = item.find('span', class_='price-was-data').get_text()
			else:
				regPrice = newPrice
			csv_writer.writerow([itemName, regPrice, newPrice])