# -*- coding: utf-8 -*-
from selenium import webdriver
import time
ie=webdriver.Ie()
url='http://www.phei.com.cn/'
ie.get(url)
time.sleep(10)
with open('phei.html','w',encoding='utf-8') as f:
    f.write(ie.page_source)
    ie.quit()