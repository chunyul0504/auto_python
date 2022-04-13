# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

url = 'http://172.16.6.30:40100/'

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url)
time.sleep(1)

# 로그인
driver.find_element(By.ID, 'user_id').send_keys('sjchoi')
time.sleep(1)

driver.find_element(By.ID, 'user_passwd').send_keys('wheein0417**')
time.sleep(1)

driver.find_element(By.ID, 'loginBtn').click()
time.sleep(2)

if driver.find_element(By.ID, 'defaultModal-ok'):
    driver.find_element(By.ID, 'defaultModal-ok').click()

driver.find_element(By.ID, 'otp_seckey').send_keys('1234')
time.sleep(1)

driver.find_element(By.ID, 'BTN_OTP_AUTH').click()
time.sleep(2)

driver.find_element(By.ID, 'defaultModal-close').click()
time.sleep(3)

# 원천사 정보 관리 진입
driver.find_element(By.XPATH, '//*[@id="menuList"]/li[1]/a').click()
time.sleep(0.5)

driver.find_element(By.XPATH, '//*[@id="MENU_100102"]/li[2]/a').click()
time.sleep(0.5)

driver.find_element(By.XPATH, '//*[@id="MENU_100107"]').click()
time.sleep(1)

# 원천사 조회
driver.find_element(By.ID, 'BTN_OPTRMGMT_SEARCH').click()
time.sleep(1)

# 원천사 등록 시작 반복
# 은행에 법인 선택하게 되어있음.
# 주의 (code_list = name_list) 개수가 같아야함.
code_list = ['300206', '300207', '300208', '300209', '300210', '300211', '300212', '300213', '300214', '300215', '300216', '300217', '300218', '300219', '300220', '300221', '300222', '300223', '300224', '300225', '300226', '300227', '300228', '300229', '300230', '300231', '300232', '300233', '300234', '300235', '300236', '300237', '300238', '300239', '300240', '300241', '300242', '300243', '300244', '300245', '300246', '300247', '300248', '300249', '300250', '300251', '300252', '300253', '300254', '300255', '300256', '300257', '300258', '300259', '300260', '300261', '300262', '300263', '300264', '300265', '300266', '300267', '300268', '300269', '300270', '300271', '300272']
name_list = ['주택', '수협', '수출입은행', '농협(10)', '농협중앙', '단위농협', '농협(13)', '농협(14)', '농협(15)', '농협(16)', '농협(17)', '국민', '우리', '조흥', '제일', '서울', '신한', '한미', '대구', '부산', '광주', '제주', '전북', '경남', '새마을금고', '신협', '상호저축은행', '모건스탠리은행', '시티', 'HSBC은행', '도이치은행', '에이비엔암로은행', 'JP모간체이스은행', '미즈호코퍼레이트은행', '미쓰비시도쿄UFJ은행', 'BOA', '우체국', '하나', '신한통합', '금결원(직불)', '동양종합금융증권', '현대증권', '미래에셋증권', '삼성증권', '한국투자증권', '우리투자증권', '교보증권', '하이투자증권', 'HMC투자증권', '키움증권', '이트레이드증권', 'SK증권', '대신증권', '솔로몬투자증권', '한화증권', '하나대투증권', '굿모닝신한증권', '동부증권', '유진투자증권', '메리츠증권', 'NH투자증권', '부국증권', '신영증권', 'LIG투자증권', '직불공통', '케이뱅크', '카카오뱅크']

# 원천사 등록 시작 반복
for code, name in zip(code_list, name_list):
    print(code)
    print(name)

    driver.find_element(By.ID, 'BTN_OPTRMGMT_NEW').click()
    time.sleep(1)

    driver.find_element(By.ID, 'oid').clear()
    driver.find_element(By.ID, 'oid').send_keys(code)
    time.sleep(0.5)
    driver.find_element(By.ID, 'oid_nm').send_keys(name)
    time.sleep(0.5)

    driver.find_element(By.ID, 'oid_typebtn').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="oid_typeWrap"]/div/ul/li[2]').click()
    time.sleep(0.5)

    driver.find_element(By.ID, 'corp_typebtn').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="corp_typeWrap"]/div/ul/li[2]').click()
    time.sleep(0.5)

    driver.find_element(By.ID, 'BTN_SAVE').click()
    time.sleep(0.5)

    driver.find_element(By.ID, 'defaultModal-close').click()
    time.sleep(0.5)

    # 원천사 신규 입력
    driver.find_element(By.ID, 'BTN_OPTRMGMT_NEW').click()
    time.sleep(1)











