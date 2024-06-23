# This code is used to scrap the mesure information of propertyfinder website using selenium

import requests
from bs4 import BeautifulSoup as soup
import csv
import os
from selenium import webdriver
import time

chrome_path = "chromedriver.exe"

link = input('Enter link : ')

driver = webdriver.Chrome(executable_path=chrome_path)

driver.get(link)
file = 'data.csv'
pages = True
page =1

try :
    while pages:
        if not os.path.exists(file):
            csv_file = open(file,'w')
            csv_writer = csv.writer(csv_file,lineterminator='\n')
            csv_writer.writerow(['Price','Area','Address','description'])
        else:
            csv_file = open(file,'a')


        total_height = int(driver.execute_script("return document.body.scrollHeight"))
        for j in range(1,total_height,15):
            driver.execute_script("window.scrollTo(0,{});".format(j))
            
        html = driver.page_source
        Soup = soup(html,'lxml')
        column = Soup.find('div',class_='column--primary')

        price = column.findAll('span',class_ = 'card__price-value')
        desc = column.findAll('h2', class_ = 'card__title card__title-link')
        
        address = column.findAll('span',class_ = 'card__location-text')

        area = column.findAll('p',class_ = 'card__property-amenity--area')

        for row in range(len(price)):
            csv_writer = csv.writer(csv_file,lineterminator='\n')
            csv_writer.writerow([price[row].text,area[row].text,address[row].text,desc[row].text])

        csv_file.close()
        print(f'page-{page} done..')
        page +=1


        try:
            driver.find_element_by_class_name('pagination__link--next').click()
        except:
            pages = False
            driver.quit()
except :
    csv_file.close()
    driver.quit()
