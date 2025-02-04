# pip install bs4 pandas
from bs4 import BeautifulSoup
import os
import pandas as pd
import json

data_list = []  # Store each item as a dictionary
ind=0
# Iterate over all HTML files in the "data" directory
for file in os.listdir("data"):
    with open(f"data/{file}", "r", encoding="utf-8") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')

    # Extract price (handles missing price)
    price_tag = soup.find("span", class_="a-price-whole")
    price = price_tag.get_text().strip() if price_tag else "N/A"

    # Extract name (handles missing name)
    name_tag = soup.find("h2", class_="a-size-base-plus")
    name = name_tag.get_text().strip() if name_tag else "Unknown Product"

    # Extract image URL (handles missing `srcset`)
    img_tag = soup.find("img", class_="s-image")
    if img_tag:
        if "srcset" in img_tag.attrs:
            srcset = img_tag["srcset"].split(",")
            highest_res_url = srcset[-1].strip().split(" ")[0]  # Highest resolution
        else:
            highest_res_url = img_tag["src"]  # Fallback to `src`
    else:
        highest_res_url = "No Image"

    # Extract link (handles missing link)
    link_tag = soup.find("a", class_="a-link-normal s-no-outline")
    link = "https://amazon.in" + link_tag["href"] if link_tag else "No Link"

    # Append extracted data to list
    data_list.append({"index": ind,"name": name, "price": price, "img": highest_res_url, "link": link})
    ind+=1

# Convert list to DataFrame
df = pd.DataFrame(data_list)

# Convert DataFrame to a list of dictionaries and save as JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(df.to_dict(orient="records"), f, indent=4, ensure_ascii=False)

print("Data extraction completed and saved to data.json")
