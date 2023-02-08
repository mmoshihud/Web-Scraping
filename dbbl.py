import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://app.dutchbanglabank.com/DBBLWeb/ATMLocation"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

filename = "DBBL_ATM.csv"
headers = ["SL No", "ATM Name", "Address"]

table = soup.find_all("table", class_="displaytbl")


data = []
for table in table:
    rows = table.find_all("tr")
    for row in rows[1:]:
        row_data = [cell.text for cell in row.find_all("td")]
        data.append(row_data)

df = pd.DataFrame(data, columns=headers)
df.to_csv(filename, index=False)
