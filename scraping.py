# watch the class from here
#  https://youtu.be/XI5_nsClCYI?si=R_s7Wxtqrzn-W2gE

# pip install selenium

# ---------------------------------------------------------------------------------------------------------------------------------------------
# importing necessary things

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# ---------------------------------------------------------------------------------------------------------------------------------------------
# for just taking one element

# driver = webdriver.Chrome()
# query="laptop"
# driver.get(f"https://www.amazon.in/s?k={query}&crid=3J0IPSX8EQO5V&sprefix=laptop%2Caps%2C421&ref=nb_sb_noss_2")
# elem = driver.find_element(By.CLASS_NAME, "puis-card-container")
# print(elem.text)
# time.sleep(2)
# driver.close()

# ---------------------------------------------------------------------------------------------------------------------------------------------
# for taking more than one element

# driver = webdriver.Chrome()
# query="shirt" # put your query here
# page_no=1
# driver.get(f"https://www.amazon.in/s?k={query}&page={page_no}&crid=3J0IPSX8EQO5V&sprefix={query}%2Caps%2C421&ref=nb_sb_noss_2")
# elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
# for elem in elems:
#     print(elem.text)
#     print("-"*30)
# print(f"got {len(elems)} elements")
# # time.sleep(2)
# driver.close()

# ---------------------------------------------------------------------------------------------------------------------------------------------
# for taking from multiple pages and make them into a html file and put it in a data file

driver = webdriver.Chrome()
query="shirt" # put your query here
fileNo=1
for i in range(1,2):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=3J0IPSX8EQO5V&sprefix={query}%2Caps%2C421&ref=nb_sb_noss_2")
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    for elem in elems:
        d= elem.get_attribute("outerHTML")
        with open(f"data/{query}_{fileNo}.html","w",encoding="utf-8") as f:
            f.write(d)
            fileNo+=1
    print(f"got {len(elems)} elements")
driver.close()

# ---------------------------------------------------------------------------------------------------------------------------------------------
