import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from tqdm import tqdm

def main():
    df = pd.read_csv("quotes_urls.csv")
    categories = df['Category'].to_list()
    urls = df['URL'].to_list()
    df_rows = []
    for idx , weblink in enumerate(urls):
        run = True
        page = weblink
        while(run):
            # dt = int((random.random())*10)
            # print(dt)
            # time.sleep(dt)
            try:
                driver = webdriver.Chrome()
                # temp = "https://www.brainyquote.com/topics/memorial-day-quotes"
                driver.get(page)
                main_seg = driver.find_element(By.ID, "quotesList")
                quotes = main_seg.find_elements(By.CLASS_NAME, "b-qt")
                authors = main_seg.find_elements(By.CLASS_NAME, "bq-aut")
                quotes_list = []
                urls_list = []
                authors_list = []
                for element in quotes:
                    quote = element.text
                    quote_view_url = element.get_attribute("href")
                    quotes_list.append(quote)
                    urls_list.append(quote_view_url)
                for element in authors:
                    author = element.text
                    authors_list.append(author)
                print(len(quotes_list), len(authors_list), len(urls_list))
                if len(quotes_list)==len(urls_list) and len(urls_list)==len(authors_list):
                    print("Length loop entered")        
                    for i in range(len(quotes_list)):
                        dict = {}
                        dict["Quote"] = quotes_list[i]
                        dict["Author"] = authors_list[i]
                        dict["Category"] = categories[idx]
                        dict["Url"] = urls_list[i]
                        df_rows.append(dict)
                if driver.find_elements(By.CLASS_NAME, "page-link"):
                    buttons = driver.find_elements(By.CLASS_NAME, "page-link")
                    for button in buttons:
                        if button.text == "Next":
                            print("next buton found")
                            inner = True
                            avail = driver.find_elements(By.CLASS_NAME, "page-item.disabled")
                            flag = 0
                            for items in avail:
                                if items.text == "Next":
                                    flag = 1
                            if flag == 0:
                                while(inner):
                                    print("Entered inner loop")
                                    try:
                                        print("Trying")
                                        page = button.get_attribute("href")
                                        print(page)
                                        inner = False
                                        print("Exiting")
                                    except:
                                        print("Exception")
                            else:
                                print("Opening another category")
                                run = False
                else:
                    print("Opening another category BIG")
                    run = False
                print("Quitting Driver")
                driver.quit()
            except:
                time.sleep(2)
    columns = ["Quote", "Author", "Category", "Url"]
    df2 = pd.DataFrame(data = df_rows, columns = columns)
    df2.to_csv("quotes.csv", index = False)

if __name__ == "__main__":
    main()