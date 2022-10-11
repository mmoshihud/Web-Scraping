from bs4 import BeautifulSoup

import requests

url = "https://location.westernunion.com/bd?country=BD&q=Bangladesh"

link = requests.get(url)
htmlContent = link.content

result = BeautifulSoup(htmlContent, 'html.parser')

name = result.find_all(class_="wu_LocationCard_Hx___1iOfo wu_Hx___39bC5")

add = result.find_all(class_="wu_LocationCard_AddressLine___3sU8t")

for data in name:
    print(data.text)

for data in add:
    print(data.text)
