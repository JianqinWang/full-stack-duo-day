#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import sys


d_horror = {"aries": "1", "taurus": "2", "gemini": "3", "cancer": "4", "leo" : "5", "virgo": "6", "libra":"7", "scorpio": "8", "sagittarius": "9",  "capricorn": "10", "aquarius":"11", "pisces": "12"}

try:
    response = requests.get("https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=" + d_horror[sys.argv[1].lower()])
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    result = soup.find('div', {"class": "horoscope-content"}).getText()
    print(result)
except:
    print("Please enter a valid horrorscope")
