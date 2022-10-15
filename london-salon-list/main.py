# Saving the file and opening the saved file for parsing purpose


# pip install requests --upgrade --quiet
# pip install bs4 --upgrade --quiet
# pip install pandas --upgrade --quiet

import requests
import urllib.request
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import pandas as pd


# hiding my ip 
proxies = {
    'http' : '45.33.12.251:8080',
    'https' :'45.33.12.251:8080'
}
url1= 'http://httpbin.org/ip'
req_proxy = requests.get(url1, proxies = proxies)
print('your proxy ip is: ', req_proxy.json())

# hiding ip code ends 

url = 'https://www.yelp.co.uk/search?find_desc=salon&find_loc=London&start=0'
response = requests.get(url)

#save the webpage in local
with open('salon1.html', 'wb+') as file:
    file.write(response.content)

# read the saved page
with open('salon1.html', 'rb') as file:
    soup = BeautifulSoup(file.read(), 'lxml')