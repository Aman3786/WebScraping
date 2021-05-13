import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import wget
import os
import csv

links = []
product_no = 1

file  = r"C:\Users\mustafa\Desktop\Ceopa\link8\link8.csv"

for pages in range(25,0,-1):
    images = []
    Title = []
    print(f"page = {pages}")
    print()
    
    session = requests.get(f'https://www.etsy.com/uk/shop/canvasbrushesknives?page={pages}#items').text
    soup = BeautifulSoup(session,'lxml')
    
   
    #need to be changed every time
    divtag = soup.find('ul',class_='listing-cards')
    print(divtag)

    #Getting the links of the product.....
    for divsub in divtag.find_all('a'):
        links.insert(0,divsub.get('href'))

    #Getting the name of the product....
    for title in divtag.find_all('a'):
        Title.insert(0,title.get('title'))
        print(f'[+] {title.get("title")}')

#https://www.etsy.com/uk/shop/LeahCaylorFineArt?section_id=23778381

    #Getting the image downloaded of the product....
    for number,link in enumerate(links):
        print(f"{number+1} Link...........................")
        subimages = []
        linksession = requests.get(link).text
        linksoup = BeautifulSoup(linksession,'lxml')
        
        
        photo = linksoup.find('ul',class_='wt-list-unstyled wt-overflow-hidden image-overlay-list wt-position-relative wt-vertical-center wt-display-flex-xs wt-justify-content-center')
        
        #singlephoto = photo.find('img')
        #print(singlephoto.get('src'))
        #wget.download(singlephoto.get('src'))

        try:
            for imglink in photo.find_all('img'):
                #print(imglink)
                image = imglink.get('data-delay-srcset')
                image = image.split(' ')
                print(f'[+] {image[2]}')
                subimages.append(image[2])
                #wget.download(image[2])
        except:
            subimages.append('None')
            print('No Images')

        images.append(subimages)
        print()

    #Writing into the csv....
    if not os.path.exists(file):
        csv_file = open(file,'w')
        csv_writer = csv.writer(csv_file,lineterminator='\n')
        csv_writer.writerow(['Sr.no','Title','Product Link','Product Image link1','Product Image link2','Product Image link3','Product Image link4','Product Image link5','Product Image link6','Product Image link7','Product Image link8','Product Image link9','Product Image link10'])
    else:
        csv_file = open(file,'a')
        csv_writer = csv.writer(csv_file,lineterminator='\n')

    for i in range(len(Title)):
        print(f'{i+1} writing')
        try:
            csv_writer.writerow([product_no,Title[i],links[i],images[i][0],images[i][1],images[i][2],images[i][3],images[i][4],images[i][5],images[i][6],images[i][7],images[i][8],images[i][9]])
        except:
            try:
                csv_writer.writerow([product_no,Title[i],links[i],images[i][0],images[i][1],images[i][2],images[i][3],images[i][4],images[i][5],images[i][6],images[i][7],images[i][8],'None'])
            except:
                try:
                    csv_writer.writerow([product_no,Title[i],links[i],images[i][0],images[i][1],images[i][2],images[i][3],images[i][4],images[i][5],images[i][6],images[i][7],'None','None'])
                except:
                    try:
                        csv_writer.writerow([product_no,Title[i],links[i],images[i][0],images[i][1],images[i][2],images[i][3],images[i][4],images[i][5],images[i][6],'None','None','None'])
                    except:
                        try:
                            csv_writer.writerow([product_no,Title[i],links[i],images[i][0],images[i][1],images[i][2],images[i][3],images[i][4],images[i][5],'None','None','None','None'])
                        except:
                            try:
                                csv_writer.writerow([product_no,Title[i],links[i],images[i][0],images[i][1],images[i][2],images[i][3],images[i][4],'None','None','None','None','None'])
                            except:
                                try:
                                    csv_writer.writerow([product_no,Title[i],links[i],images[i][0],images[i][1],images[i][2],images[i][3],'None','None','None','None','None','None'])
                                except:
                                    try:
                                        csv_writer.writerow([product_no,Title[i],links[i],images[i][0],images[i][1],images[i][2],'None','None','None','None','None','None','None'])
                                    except:
                                        try:
                                            csv_writer.writerow([product_no,Title[i],links[i],images[i][0],images[i][1],'None','None','None','None','None','None','None','None'])
                                        except:
                                            csv_writer.writerow([product_no,Title[i],links[i],images[i][0],'None','None','None','None','None','None','None','None','None'])
                            
        
        product_no += 1

    csv_file.close()
        
        
        
    links = []

        












        
