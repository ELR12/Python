# Created by Ethan Roberts
# on 12/13/2020

# This is a job-scraping program where I scrape the latest monitor prices on newegg.com.
#TODO:  Add locations of where the jobs are (is it in hsv or is this job in chicago?)


import requests
from bs4 import BeautifulSoup
from csv import writer

with open('jobs.csv', 'w') as csv_file:  # write to csv
    csv_writer = writer(csv_file)
    fileHeaders = ['CompanyName', 'JobTitle', 'DatePosted']
    csv_writer.writerow(fileHeaders)

    urlArray = (
        ["https://www.indeed.com/jobs?q=software+engineer&l=Huntsville%2C+AL&sort=date&start={}", #hsv
        "https://www.indeed.com/jobs?q=software+enginner&l=Chicago%2C+IL&sort=date&start={}"] #chicago
    )

    for link in urlArray:
        for i in range(10,30,10):
            url = link.format(i)
            response = requests.get(url)  # must read 200 which means successfully connected to website
            src = response.content  # contains the source-code of the website
            soup = BeautifulSoup(src, 'html.parser')

            jobTitle = {"class": "jobtitle"}
            companyTitle = {"class": "company"}
            datePosted = {"class": "result-link-bar"}
            titleArray = soup.find_all(attrs=jobTitle)
            companyArray = soup.find_all(attrs=companyTitle)
            datePostedArray = soup.find_all(attrs=datePosted)

            for i, (a,b,c) in enumerate(zip(titleArray, companyArray, datePostedArray)):
                companyName = b.get_text()
                jobName = a.get_text()
                postDate = c.find("span").get_text()
                print(companyName, jobName,postDate,"\n")
                csv_writer.writerow([companyName, jobName,postDate])