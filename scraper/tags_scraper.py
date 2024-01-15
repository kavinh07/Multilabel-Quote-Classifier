import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import multiprocessing

def main_1():
    df = pd.read_csv("quotes.csv")
    urls = df['Url'].to_list()
    small_url = urls[90000:91000]
    # print(small_url)
    labels = []
    for url in small_url:
        run = True
        while(run):
            try:
                driver  = webdriver.Chrome()
                driver.get(url)
                main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
                tags = []
                elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
                for element in elements:
                    tags.append(element.text)
                labels.append(tags)
                # print(tags)
                print(len(labels))
                run = False
                driver.quit()
            except:
                # print("Exception")
                time.sleep(2)
        # print("For loop end")
    zipped = list(zip(small_url, labels))
    df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
    df.to_csv("tag_1k_3_1.csv", index = False)   



def main_2():
    df = pd.read_csv("quotes.csv")
    urls = df['Url'].to_list()
    small_url = urls[91000:92000]
    # print(small_url)
    labels = []
    for url in small_url:
        run = True
        while(run):
            try:
                driver  = webdriver.Chrome()
                driver.get(url)
                main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
                tags = []
                elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
                for element in elements:
                    tags.append(element.text)
                labels.append(tags)
                # print(tags)
                print(len(labels))
                run = False
                driver.quit()
            except:
                # print("Exception")
                time.sleep(2)
        # print("For loop end")
    zipped = list(zip(small_url, labels))
    df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
    df.to_csv("tag_1k_3_2.csv", index = False) 



def main_3():
    df = pd.read_csv("quotes.csv")
    urls = df['Url'].to_list()
    small_url = urls[92000:93000]
    # print(small_url)
    labels = []
    for url in small_url:
        run = True
        while(run):
            try:
                driver  = webdriver.Chrome()
                driver.get(url)
                main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
                tags = []
                elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
                for element in elements:
                    tags.append(element.text)
                labels.append(tags)
                # print(tags)
                print(len(labels))
                run = False
                driver.quit()
            except:
                # print("Exception")
                time.sleep(2)
        # print("For loop end")
    zipped = list(zip(small_url, labels))
    df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
    df.to_csv("tag_1k_3_3.csv", index = False)   



def main_4():
    df = pd.read_csv("quotes.csv")
    urls = df['Url'].to_list()
    small_url = urls[93000:94000]
    # print(small_url)
    labels = []
    for url in small_url:
        run = True
        while(run):
            try:
                driver  = webdriver.Chrome()
                driver.get(url)
                main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
                tags = []
                elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
                for element in elements:
                    tags.append(element.text)
                labels.append(tags)
                # print(tags)
                print(len(labels))
                run = False
                driver.quit()
            except:
                # print("Exception")
                time.sleep(2)
        # print("For loop end")
    zipped = list(zip(small_url, labels))
    df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
    df.to_csv("tag_1k_3_4.csv", index = False) 



def main_5():
    df = pd.read_csv("quotes.csv")
    urls = df['Url'].to_list()
    small_url = urls[94000:95000]
    # print(small_url)
    labels = []
    for url in small_url:
        run = True
        while(run):
            try:
                driver  = webdriver.Chrome()
                driver.get(url)
                main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
                tags = []
                elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
                for element in elements:
                    tags.append(element.text)
                labels.append(tags)
                # print(tags)
                print(len(labels))
                run = False
                driver.quit()
            except:
                # print("Exception")
                time.sleep(2)
        # print("For loop end")
    zipped = list(zip(small_url, labels))
    df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
    df.to_csv("tag_1k_3_5.csv", index = False)   



def main_6():
    df = pd.read_csv("quotes.csv")
    urls = df['Url'].to_list()
    small_url = urls[95000:96000]
    # print(small_url)
    labels = []
    for url in small_url:
        run = True
        while(run):
            try:
                driver  = webdriver.Chrome()
                driver.get(url)
                main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
                tags = []
                elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
                for element in elements:
                    tags.append(element.text)
                labels.append(tags)
                # print(tags)
                print(len(labels))
                run = False
                driver.quit()
            except:
                # print("Exception")
                time.sleep(2)
        # print("For loop end")
    zipped = list(zip(small_url, labels))
    df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
    df.to_csv("tag_1k_3_6.csv", index = False) 


def main_7():
    df = pd.read_csv("quotes.csv")
    urls = df['Url'].to_list()
    small_url = urls[96000:97000]
    # print(small_url)
    labels = []
    for url in small_url:
        run = True
        while(run):
            try:
                driver  = webdriver.Chrome()
                driver.get(url)
                main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
                tags = []
                elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
                for element in elements:
                    tags.append(element.text)
                labels.append(tags)
                # print(tags)
                print(len(labels))
                run = False
                driver.quit()
            except:
                # print("Exception")
                time.sleep(2)
        # print("For loop end")
    zipped = list(zip(small_url, labels))
    df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
    df.to_csv("tag_1k_3_7.csv", index = False)   



def main_8():
    df = pd.read_csv("quotes.csv")
    urls = df['Url'].to_list()
    small_url = urls[97000:98000]
    # print(small_url)
    labels = []
    for url in small_url:
        run = True
        while(run):
            try:
                driver  = webdriver.Chrome()
                driver.get(url)
                main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
                tags = []
                elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
                for element in elements:
                    tags.append(element.text)
                labels.append(tags)
                # print(tags)
                print(len(labels))
                run = False
                driver.quit()
            except:
                # print("Exception")
                time.sleep(2)
        # print("For loop end")
    zipped = list(zip(small_url, labels))
    df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
    df.to_csv("tag_1k_3_8.csv", index = False) 



def main_9():
    df = pd.read_csv("quotes.csv")
    urls = df['Url'].to_list()
    small_url = urls[98000:99000]
    # print(small_url)
    labels = []
    for url in small_url:
        run = True
        while(run):
            try:
                driver  = webdriver.Chrome()
                driver.get(url)
                main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
                tags = []
                elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
                for element in elements:
                    tags.append(element.text)
                labels.append(tags)
                # print(tags)
                print(len(labels))
                run = False
                driver.quit()
            except:
                # print("Exception")
                time.sleep(2)
        # print("For loop end")
    zipped = list(zip(small_url, labels))
    df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
    df.to_csv("tag_1k_3_9.csv", index = False)   



def main_10():
    df = pd.read_csv("quotes.csv")
    urls = df['Url'].to_list()
    small_url = urls[99000:100000]
    # print(small_url)
    labels = []
    for url in small_url:
        run = True
        while(run):
            try:
                driver  = webdriver.Chrome()
                driver.get(url)
                main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
                tags = []
                elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
                for element in elements:
                    tags.append(element.text)
                labels.append(tags)
                # print(tags)
                print(len(labels))
                run = False
                driver.quit()
            except:
                # print("Exception")
                time.sleep(2)
        # print("For loop end")
    zipped = list(zip(small_url, labels))
    df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
    df.to_csv("tag_1k_3_10.csv", index = False) 



# def main_11():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[80000:81000]
#     # print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 time.sleep(2)
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag_1k_2_11.csv", index = False)   



# def main_12():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[81000:82000]
#     # print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 # print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 # print("Exception")
#                 time.sleep(2)
#         # print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag_1k_2_12.csv", index = False) 



# def main_13():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[82000:83000]
#     # print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 # print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 # print("Exception")
#                 time.sleep(2)
#         # print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag_1k_2_13.csv", index = False)   



# def main_14():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[83000:84000]
#     # print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 # print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 # print("Exception")
#                 time.sleep(2)
#         # print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag_1k_2_14.csv", index = False) 



# def main_15():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[84000:85000]
#     # print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 # print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 # print("Exception")
#                 time.sleep(2)
#         # print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag_1k_2_15.csv", index = False)   



# def main_16():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[85000:86000]
#     # print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 # print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 # print("Exception")
#                 time.sleep(2)
#         # print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag_1k_2_16.csv", index = False) 


# def main_17():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[86000:87000]
#     # print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 # print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 # print("Exception")
#                 time.sleep(2)
#         # print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag_1k_2_17.csv", index = False)   



# def main_18():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[87000:88000]
#     # print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 # print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 # print("Exception")
#                 time.sleep(2)
#         # print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag_1k_2_18.csv", index = False) 



# def main_19():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[88000:89000]
#     # print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 # print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 # print("Exception")
#                 time.sleep(2)
#         # print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag_1k_2_19.csv", index = False)   



# def main_20():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[89000:90000]
#     # print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 # print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 # print("Exception")
#                 time.sleep(2)
#         # print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag_1k_2_20.csv", index = False) 



###After part:

# def main_1():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[50000:52500]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
                # print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag1.csv", index = False)   



# def main_2():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[52500:55000]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag2.csv", index = False) 



# def main_3():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[55000:57500]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag3.csv", index = False)   



# def main_4():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[57500:60000]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag4.csv", index = False) 



# def main_5():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[60000:62500]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag5.csv", index = False)   



# def main_6():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[62500:65000]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag6.csv", index = False) 


# def main_7():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[65000:67500]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag7.csv", index = False)   



# def main_8():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[67500:70000]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag8.csv", index = False) 



# def main_9():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[70000:72500]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag9.csv", index = False)   



# def main_10():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[72500:75000]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag10.csv", index = False) 



# def main_11():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[75000:77500]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag11.csv", index = False)   



# def main_12():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[77500:80000]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag12.csv", index = False) 



# def main_13():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[80000:82500]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag13.csv", index = False)   



# def main_14():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[82500:85000]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag14.csv", index = False) 



# def main_15():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[85000:87500]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag15.csv", index = False)   



# def main_16():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[87500:90000]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag16.csv", index = False) 


# def main_17():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[90000:92500]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag17.csv", index = False)   



# def main_18():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[92500:95000]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag18.csv", index = False) 



# def main_19():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[95000:97500]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag19.csv", index = False)   



# def main_20():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[97500:100000]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag20.csv", index = False)



# def main_21():
#     df = pd.read_csv("quotes.csv")
#     urls = df['Url'].to_list()
#     small_url = urls[100000:]
#     print(small_url)
#     labels = []
#     for url in small_url:
#         run = True
#         while(run):
#             try:
#                 driver  = webdriver.Chrome()
#                 driver.get(url)
#                 main_seg = driver.find_element(By.CLASS_NAME, "qdBox")
#                 tags = []
#                 elements = main_seg.find_elements(By.CLASS_NAME, "qkw-btn")
#                 for element in elements:
#                     tags.append(element.text)
#                 labels.append(tags)
#                 print(tags)
#                 print(len(labels))
#                 run = False
#                 driver.quit()
#             except:
#                 print("Exception")
#                 time.sleep(2)
#         print("For loop end")
#     zipped = list(zip(small_url, labels))
#     df = pd.DataFrame(zipped, columns = ['links', 'tags']) 
#     df.to_csv("tag21.csv", index = False) 

if __name__ == "__main__":
  
    # creating processes 
    p1 = multiprocessing.Process(target=main_1) 
    p2 = multiprocessing.Process(target=main_2) 
    p3 = multiprocessing.Process(target=main_3) 
    p4 = multiprocessing.Process(target=main_4) 
    p5 = multiprocessing.Process(target=main_5) 
    p6 = multiprocessing.Process(target=main_6) 
    p7 = multiprocessing.Process(target=main_7) 
    p8 = multiprocessing.Process(target=main_8) 
    p9 = multiprocessing.Process(target=main_9) 
    p10 = multiprocessing.Process(target=main_10) 
    # p11 = multiprocessing.Process(target=main_11) 
    # p12 = multiprocessing.Process(target=main_12) 
    # p13 = multiprocessing.Process(target=main_13) 
    # p14 = multiprocessing.Process(target=main_14) 
    # p15 = multiprocessing.Process(target=main_15) 
    # p16 = multiprocessing.Process(target=main_16) 
    # p17 = multiprocessing.Process(target=main_17) 
    # p18 = multiprocessing.Process(target=main_18) 
    # p19 = multiprocessing.Process(target=main_19) 
    # p20 = multiprocessing.Process(target=main_20) 
    # p21 = multiprocessing.Process(target=main_21)
    # starting processes 
    p1.start() 
    p2.start() 
    p3.start() 
    p4.start() 
    p5.start() 
    p6.start() 
    p7.start() 
    p8.start() 
    p9.start() 
    p10.start() 
    # p11.start() 
    # p12.start() 
    # p13.start() 
    # p14.start() 
    # p15.start() 
    # p16.start() 
    # p17.start() 
    # p18.start() 
    # p19.start() 
    # p20.start() 
    # p21.start()
  
    print("done")