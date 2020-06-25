# -*- coding: utf-8 -*-

# pip install selenium
# pip install beautifulsoup4

from selenium import webdriver
import requests,os
from pathlib import Path
import time

searchTerm = "building images"
output_dir = "./Images/Selenium/"
num = 1

browser = webdriver.Chrome()

browser.get("https://www.google.com/")

browser.implicitly_wait(2000)
search = browser.find_element_by_name("q")

search.send_keys(searchTerm)
search.submit()

imagetab = browser.find_element_by_class_name("qs")
imagetab.click()

images = browser.find_elements_by_class_name("rg_i")

for i in range(len(images)):
    images[i].click()
    time.sleep(2)
    currimg = browser.find_elements_by_class_name("n3VNCb")
    url = currimg[0].get_attribute("src")
    print(url)
    try:
        file = "%s%s/%s" % (output_dir, searchTerm, num)
        num = num+1
        if Path(file).is_file():
            print("File already exists")
            continue
        r = requests.get(url)
        os.makedirs(os.path.dirname(file), exist_ok=True)            
        with open(file,"wb") as f:
            f.write(r.content)
    except Exception:
        pass
    
browser.quit()

# currimg = ((By.XPATH, "")))
# currimg = browser.find_element_by_xpath("//div//img[@class='n3VNCb']")
# currimg = browser.find_elements_by_class_name("n3VNCb")
# WebDriverWait(browser, 20)
# for img in currimg:
#     print(img.get_attribute("src"))
# "//a[@class='eHAdSb']//img[@class='n3VNCb']"