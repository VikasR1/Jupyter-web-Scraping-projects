# get all urls of a page and printing them in csv file

import re
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import pandas as pd

# hiding my ip 
proxies = {
    'http' : '204.185.204.64:8080',
    'https' :'204.185.204.64:8080'
}
url1= 'http://httpbin.org/ip'
req_proxy = requests.get(url1, proxies = proxies)
print('your proxy ip is: ', req_proxy.json())

# hiding ip code ends 

URL = 'https://www.yelp.co.uk/search?find_desc=salon&find_loc=London&start='

page_urls = []

for page in range(0,23):
    response = requests.get(URL + str(page))
    # print('Printing url of page {}'.format(page))
    url = URL + str(page)
    page_urls.append(url)
    print("Printing url of page no {}".format(page))

    # sleep(randint(2,4))
url_dict = {
    'Page Url' : page_urls
}

df = pd.DataFrame(url_dict)
print(df)
df.to_csv('yelp_salon_urls.csv')