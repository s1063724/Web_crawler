from typing import Iterator
from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement


def main():
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://job.taiwanjobs.gov.tw/internet/index/job_search_by_keyword.aspx")
    driver.find_element_by_id("imgclose").click()
    driver.find_element_by_xpath("//*[@id='hotkey_search']/input[7]").click()
    # driver.find_element_by_id("CPH1_btnSearch").click()
    # table = driver.find_element_by_id("CPH1_tb_jobQueryResult")

    time.sleep(1000)


if __name__ == '__main__':
    main()
