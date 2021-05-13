from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time
import os
import csv

file = 'C:\\Users\\mustafa\\Desktop\\Restaurants1.csv'
if not os.path.exists(file):
    csv_file = open(file,'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Mobile'])
else:
    csv_file = open(file,'a')
    csv_writer = csv.writer(csv_file)
    

numbers = {'acb':'0','yz':'1','wx':'2','vu':'3','ts':'4','rq':'5','po':'6','nm':'7','lk':'8','ji':'9'}
mob = ''
final_num = []
#img_link = []
#Name = []
#Ratings = []
#Time = []

chrome_path = "C:\\Users\\mustafa\\Desktop\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://www.justdial.com/Bhubaneshwar/Restaurants/nct-10408936/page-49')
time.sleep(5)
html = driver.page_source

soup = BeautifulSoup(html,'lxml')
ull = soup.find("section",class_='rslwrp')
    
for i in ull.find_all('li',class_='cntanr'):
    #img = i.find('img')
    #img_link.append(img.get('src'))
    
    #name = i.find('span',class_='lng_cont_name')
    #Name.append(name.text)

    #try:
     #   ratings = i.find('span',class_='green-box')
      #  Ratings.append(ratings.text)
    #except:
     #   ratings = 0
      #  Ratings.append(ratings)

    #try:
     #   time = i.find('span',class_='distnctxt rsrtopn-1')
      #  print(time.text)
       # Time.append(time.text)
   # except:
    #    time = 'OPEN NOW'
     #   Time.append(time)
    
    spann = i.find_all('span',class_='mobilesv')
    if len(spann) > 10:
        spann = spann[6:]
        for j in spann:
            num = j['class'][1]
            num = num.split('-')
            if num[1] in numbers:
                mob = mob + numbers[num[1]]
        final_num.append(mob)      
    else:
        spann  = spann[:10]
        for j in spann:
            num = j['class'][1]
            num = num.split('-')
            if num[1] in numbers:
                mob = mob + numbers[num[1]]
        final_num.append(mob)
            
    mob = ''


for i in range(len(final_num)):
    csv_writer.writerow([final_num[i]])
        
csv_file.close()
print(len(final_num))
#print(len(img_link))
#print(len(Name))
#print(len(Ratings))
#print(len(Time))


    
