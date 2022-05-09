# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def login():
    # 개발
    url = 'http://172.16.6.30:40100/'
    user_id = 'sjchoi'
    user_pw = 'wheein0417**'
    user_otp = '1234'

    # 운영
    # url = 'http://172.16.2.10:40100/'
    # user_id = 'kanak'
    # user_pw = 'zjspr1101!'
    # user_otp = '1234'

    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)
    time.sleep(1)

    # 로그인
    driver.find_element(By.ID, 'user_id').send_keys(user_id)
    time.sleep(1)

    driver.find_element(By.ID, 'user_passwd').send_keys(user_pw)
    time.sleep(1)

    driver.find_element(By.ID, 'loginBtn').click()
    time.sleep(2)

    if driver.find_element(By.ID, 'defaultModal-ok'):
        driver.find_element(By.ID, 'defaultModal-ok').click()

    driver.find_element(By.ID, 'otp_seckey').send_keys(user_otp)
    time.sleep(1)

    driver.find_element(By.ID, 'BTN_OTP_AUTH').click()
    time.sleep(2)

    driver.find_element(By.ID, 'defaultModal-close').click()
    time.sleep(3)

    return driver


def clicking_path(driver, x_path):
    driver.find_element(By.XPATH, x_path).click()
    time.sleep(0.5)
    return driver


def clicking_id(driver, element_id):
    driver.find_element(By.ID, element_id).click()
    time.sleep(0.5)
    return driver


def input_send_path(driver, x_path, key_word):
    driver.find_element(By.XPATH, x_path).send_keys(key_word)
    time.sleep(0.5)
    return driver


def input_send_id(driver, element_id, key_word):
    driver.find_element(By.ID, element_id).send_keys(key_word)
    time.sleep(0.5)
    return driver

