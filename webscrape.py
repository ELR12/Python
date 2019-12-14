# Created by
# Ethan Roberts
# on 12/14/2019

# This is a webscraping program where I scrape the latest monitor prices on newegg.com.  
# I am using this program to teach myself webscraping fundamentals as well as Python programming langauage.


import requests
from bs4 import BeautifulSoup
url = 'https://www.newegg.com/p/pl?Submit=ENE&IsNodeId=1&N=100160979%20600557170%20601305587&cm_sp=CAT_Monitors_2-_-VisNav-_-4K-42-Monitors_2'
response = requests.get(url)
src = response.content  #contains the source-code of the website
soup = BeautifulSoup(src, 'html.parser') 

#print(soup.find('a', class_='item-title').get_text())

for item in soup.select('.item-info'):  #using soup.select, could've used soup.findAll
	itemName = item.find('a', class_='item-title').get_text()
	price = item.find('li', class_='price-current').get_text()
	print(itemName, price)  #only print first 50 chars 
	