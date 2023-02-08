import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.ebl.com.bd/locator/atms"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

filename = "EBL_ATM.csv"
headers = ["SL.", "Division", "Name", "Address"]
# tables = soup.find_all("table", class_="table")

table = soup.find("tbody")

# extract data from table rows
rows = []
for tr in table.find_all("tr"):
    data = [td.text.strip() for td in tr.find_all("td")]
    rows.append(data)

# create a pandas DataFrame from the rows
df = pd.DataFrame(rows, columns=headers)

# write the DataFrame to a CSV file
df.to_csv(filename, index=False)
