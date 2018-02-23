from urllib import *
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
import urllib.request
import requests
from io import BytesIO
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from lxml import html
from datetime import date, datetime, timedelta
from dateutil.relativedelta import *


def scraping(first_name="", last_name=""):

    base_url = "https://www.ncf.edu/directory/listing/"
    url = base_url + "?le={}&nm=first_name".format(first_name[0].lower())

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    r = requests.get(url, headers=headers, stream=True)
    html = r.content.decode()
    soup = BeautifulSoup(html, "html.parser")

    phone_num = ""
    email = ""
    try:
        rows = soup.select("tr")

        for i, row in enumerate(rows):
            if i==0:
                continue

            cols = row.select("td")
            name_tmp = cols[0].text.strip()
            email_tmp = cols[1].text.strip()
            phone_num_tmp = cols[2].text.strip()

            if first_name in name_tmp.upper() and last_name in name_tmp.upper():
                phone_num = phone_num_tmp
                email = email_tmp
    except:
        phone_num = ""
        email = ""

    print(phone_num)
    print(email)

    return [phone_num, email]

# scraping(first_name="DEBORAH", last_name="ABEL")
scraping(first_name="FRANK", last_name="ALCOCK")