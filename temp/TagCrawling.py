## 프로젝트 초기에 태그 목록을 얻기 위해 처음 한 번만 사용된 코드입니다.
## This code is used only once at the beginning of the project to obtain a list of tags.


import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
import re

driver = webdriver.Safari()
driver.get("https://novelai.io/tags")

# Find the type elements
types = driver.find_elements(By.CSS_SELECTOR, '.type-list .item')
type_list = [typ.text for typ in types]

# Initialize a dictionary to store the tags
tags_by_type_category = {}

for i, typ in enumerate(type_list):
    types[i].click()
    # Find the category elements
    categories = driver.find_elements(By.CSS_SELECTOR, ".category-list .item")
    category_list = [category.text for category in categories]

    for j, category in enumerate(category_list):
        categories[j].click()
        # Find the tag elements
        tags = driver.find_elements(By.CSS_SELECTOR, ".tag-list .item")
        tag_list = [tag.text.strip() for tag in tags]
        # Add the tags to the dictionary, separated by type and category

        typ = typ.strip()
        category = category.strip()
        tags_by_type_category[typ, category] = tag_list

# create dataframe
df = pd.DataFrame.from_dict(tags_by_type_category, orient='index')
df.reset_index(inplace=True)
df.rename(columns={'index':'Type and category',0:'tags'}, inplace=True)

# Save the DataFrame to a CSV file
df.to_csv(r'temp/raw_tags.csv', index=False)

# Close the browser
driver.quit()