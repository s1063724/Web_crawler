from selenium import webdriver
from typing import Iterator
import time
from selenium.webdriver.remote.webelement import WebElement
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import pandas as pd


def main():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://job.taiwanjobs.gov.tw/Internet/Index/Index.aspx')
    to_job_info(driver)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find_all('table', {'class': 'table table-striped table-hover panel-group table-rwd table-jobSearch'})
    print(table.prettify())
    # print(soup.prettify())
    time.sleep(100)


def to_job_info(driver):
    driver.find_element_by_id("imgclose").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='divfind_job']/button[2]/span").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='UC_Modal_CJOB-item_7']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='UC_FindJob_UC_Modal_CJOB']/div/div/div[3]/button[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='UC_FindJob_btn1']").click()
    time.sleep(3)
    for i in range(1, 21):
        driver.execute_script('getPosts();')
        time.sleep(3)

if __name__ == '__main__':
    main()
