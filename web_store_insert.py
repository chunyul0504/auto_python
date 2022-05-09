# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from web_auto_function import *

search_agency_name = 'ES우리안과'

# 로그인
driver = login()

# 기본정보관리 진입
driver = clicking_path(driver, '//*[@id="menuList"]/li[1]/a')

# 사업자정보 진입
driver = clicking_path(driver, '//*[@id="MENU_100102"]/li[1]/a')

# 사업자 정보 관리 진입
driver = clicking_path(driver, '//*[@id="MENU_100096"]')

# 대표 가맹점명 검색.
driver = clicking_path(driver, '//*[@id="srch_typebtn"]')
driver = clicking_path(driver, '//*[@id="srch_typeWrap"]/div/ul/li[4]')
driver = input_send_id(driver, 'srch_value', search_agency_name)
driver = clicking_id(driver, 'BTN_SEARCH')

# 가맹점 명 텍스트 확인
search_agency_table = driver.find_element(By.XPATH, '//*[@id="grid_entp_mgmt_table"]/tbody')

text = driver.find_element(By.XPATH, '//*[@id="grid_entp_mgmt_table"]/tbody/tr[2]')
print(text.getText)





