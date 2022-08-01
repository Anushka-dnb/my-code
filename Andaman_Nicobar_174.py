# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 12:24:05 2022

@author: sawanta
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import json
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')

driver = webdriver.Chrome("C:/Users/sawanta/OneDrive - Dun and Bradstreet/Desktop/chromedriver.exe", chrome_options=options)
driver.get('https://ngodarpan.gov.in/index.php/home/statewise')

driver.find_element("xpath",'//*[@id="frm_griev"]/table[2]/tbody/tr[2]/td/table/tbody/tr[5]/td/ol/li[1]/a').click()

view= driver.find_element("xpath",'/html/body/div[9]/div[1]/div[3]/div/div/div[1]/form/div[2]/select')
view.send_keys("100")
data_list=[]
rows = driver.find_elements("xpath",'/html/body/div[9]/div[1]/div[3]/div/div/div[2]/table/tbody/tr')
for i in range(1, len(rows)+1):
    driver.find_element("xpath",'/html/body/div[9]/div[1]/div[3]/div/div/div[2]/table/tbody/tr['+str(i)+']/td[2]/a').click()
    time.sleep(5)
    Data = driver.find_element("xpath",'//*[@id="printThis"]').text 
    data_list.append(Data)
    driver.refresh()
    
# for moving on next page
try:
    driver.find_element('xpath','/html/body/div[9]/div[1]/div[3]/div/div/div[2]/ul/li[4]/a').click()
    rows = driver.find_elements("xpath",'/html/body/div[9]/div[1]/div[3]/div/div/div[2]/table/tbody/tr')
    for i in range(1, len(rows)+1):
        driver.find_element("xpath",'/html/body/div[9]/div[1]/div[3]/div/div/div[2]/table/tbody/tr['+str(i)+']/td[2]/a').click()
        time.sleep(5)
        Data = driver.find_element("xpath",'//*[@id="printThis"]').text 
        data_list.append(Data)
        driver.refresh()
except:
    pass

Andaman_list = data_list
Andaman_list