from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.thecitybank.com/locate-atm-branch")
driver.implicitly_wait(60)

# radio_button = driver.find_element_by_id("atm")
radio_button = driver.find_element(
    By.XPATH, "/html/body/div[1]/div[3]/div/div/div/form/div/div[2]/input")

radio_button.click()

# Wait for the content to load
wait = WebDriverWait(driver, 60)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.location-tag")))

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

location_tags = soup.find_all("a", class_="location-tag")

data = []
for location_tag in location_tags:
    title = location_tag.find("p", class_="title").text
    details = location_tag.find_all("p", class_="detail")
    city = details[0].text
    address = details[1].text
    data.append({"Title": title, "City": city, "Address": address})

df = pd.DataFrame(data)
df.to_csv("City_Bank_ATM.csv", index=False)

driver.quit()

# for location_tag in location_tags:
#     title = location_tag.find("p", class_="title").text
#     details = location_tag.find_all("p", class_="detail")
#     city = details[0].text
#     address = details[1].text
#     print(f"Title: {title}")
#     print(f"City: {city}")
#     print(f"Address: {address}")
#     print("----" * 20)

# driver.quit()
