#!/usr/bin/env python
# coding: utf-8

# In[259]:


# N.B. RUNNING THIS PROJECT MIGHT HAVE SOME ISSUES BECAUSE OF CAPCHA RESTRICTIONS. TRY RUNNING IT MULTIPLE TIMES AND EVENTUALLY IT WILL BYPASS CAPCHA.

#import library
from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[299]:


# connect to the website
URL = 'https://www.amazon.com/Retreez-Funny-Mug-Programming-Inspirational/dp/B08WKZ84DC/ref=sr_1_67?keywords=data+gift&qid=1687443747&sr=8-67'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
 
page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id="productTitle").get_text()

tag = soup2.find('span',class_="a-offscreen")
for i in tag:
    price = i.text
    
review = soup2.find('span',class_="a-icon-alt")
for i in review:
    rating = i.text
 
    
amountOfRatings = soup2.find(id="acrCustomerReviewText").get_text()

print(title)
print(price)
print(rating)
print(amountOfRatings)






# In[300]:


price = price.strip()[1:]
title = title.strip()
rating = rating.strip()[:3]
amountOfRatings = amountOfRatings.strip().split(" ",1)[0]


print(title)
print(price)
print(rating)
print(amountOfRatings)


# In[304]:


import datetime
today = datetime.date.today()
print(today)


# In[306]:


import csv

header = ['Product', 'Price', 'Rating', 'AmountOfRating', 'Date']
data = [title, price, rating, amountOfRatings, today]

with open('AmazonProductScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    


# In[311]:


import pandas as pd
df = pd.read_csv(r'C:\Users\hfort\AmazonProductScraperDataset.csv')
print(df)



# In[ ]:


# Appending data to the csv dataset

with open('AmazonProductScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)
    


# In[318]:


# make it automatic

def check_price():
    URL = 'https://www.amazon.com/Retreez-Funny-Mug-Programming-Inspirational/dp/B08WKZ84DC/ref=sr_1_67?keywords=data+gift&qid=1687443747&sr=8-67'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
 
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id="productTitle").get_text()
    title = title.strip()

    tag = soup2.find('span',class_="a-offscreen")
    for i in tag:
        price = i.text
    price = price.strip()[1:]
    
    review = soup2.find('span',class_="a-icon-alt")
    for i in review:
        rating = i.text
    rating = rating.strip()[:3]
 
    
    amountOfRatings = soup2.find(id="acrCustomerReviewText").get_text()
    amountOfRatings = amountOfRatings.strip().split(" ",1)[0]
    
    import datetime
    today = datetime.date.today()
    
    import csv
    header = ['Product', 'Price', 'Rating', 'AmountOfRating', 'Date']
    data = [title, price, rating, amountOfRatings, today]
    
    with open('AmazonProductScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
    if(price < 10):
        send_mail()


# In[ ]:


while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


import pandas as pd
df = pd.read_csv(r'C:\Users\hfort\AmazonProductScraperDataset.csv')
print(df)


# In[ ]:


# automatic email sent if price drop below a determined treshold

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.ehlo()
    # Need to enter the password in a more private code...
    server.login('h.fortier94@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The item you want is below $10! Now is your chance to buy!"
    body = "Henri now is the time to buy the item you wanted for a long time ! The price is now below 10$. Here's the link : https://www.amazon.com/Retreez-Funny-Mug-Programming-Inspirational/dp/B08WKZ84DC/ref=sr_1_67?keywords=data%2Bgift&qid=1687443747&sr=8-67&th=1"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'h.fortier94@gmail.com',
        msg
     
    )


# In[ ]:




