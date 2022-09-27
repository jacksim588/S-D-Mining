import urllib
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
import pandas as pd
from math import nan
from datetime import date
import psycopg2
import time
import requests
import gzip

urls=['https://www.boots.com/brands']


for url in urls:
    print('requesting')
    req = Request(url)
    print('opening')
    try:
        html_page = gzip.decompress(urlopen(req).read()).decode('utf-8')
    except OSError:
        html_page = urlopen(req).read().decode('utf-8')
    print('converting to soup')
    soup = bs(html_page, 'html.parser')
    #print(soup)

    brandListSelectors=soup.find_all("div", {"class": "brand_list_selector"})
    brandListSelectors=brandListSelectors[0].find_all('a', href=True)
    brandListSelectors=[e['href'] for e in brandListSelectors]
    #print(brandListSelectors)

    brandListSelectors=['https://www.boots.com/brands']
    for brandsPage in brandListSelectors:
        req = Request(url)
        try:
            html_page = gzip.decompress(urlopen(req).read()).decode('utf-8')
        except OSError:
            html_page = urlopen(req).read().decode('utf-8')
        brandsSoup = bs(html_page, 'html.parser')
        #print(soup)
        brandsURls = brandsSoup.find_all("div", {"id": "brand_list_viewer"})
        brandsURls=brandsURls[1].find_all('a', href=True)
        brandsURls=[e['href'] for e in brandsURls]
        for brandURL in brandsURls:
            print(brandURL)

'''    nameArray = soup.find_all("h1", {"itemprop": "name"})
    print(nameArray)
    name=nameArray[0].text.strip()
    print(name)

    promotionArray = soup.find_all("li", {"class": "pdp-promotion-redesign"})
    print(promotionArray)
    promotion=promotionArray[0].text.strip()
    print(promotion)'''
        