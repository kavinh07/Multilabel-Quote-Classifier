import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
    url = "https://www.brainyquote.com/topics"
    driver = webdriver.Edge()
    driver.get(url)
    time.sleep(5)
    main_seg = driver.find_element(By.CLASS_NAME, "row.bq_left")
    contents = main_seg.find_elements(By.CLASS_NAME, "topicIndexChicklet.bq_on_link_cl")
    category_dict ={}
    for content in contents:
        category_name = content.find_element(By.CLASS_NAME, "topicContentName").text
        category_url = content.get_attribute("href")
        category_dict[category_name] = category_url
    cols = ['Category', 'URL']
    df = pd.DataFrame(list(category_dict.items()), columns=cols)
    df.to_csv("quotes_urls.csv", index= False)
    driver.quit()


if __name__ == "__main__":
    main()