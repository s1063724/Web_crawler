from typing import Iterator
from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement


def main():
    driver = webdriver.Chrome("./chromedriver")

    driver.get("https://job.taiwanjobs.gov.tw/Internet/Index/Index.aspx")
    driver.find_element_by_id("imgclose").click()
    # driver.find_element_by_xpath("//*[@id='hotkey_search']/input[7]").click()
    driver.find_element_by_xpath("//*[@id='divfind_job']/button[2]/span").click()

    driver.find_element_by_xpath("//*[@id='UC_Modal_CJOB-item_7']").click()

    driver.find_element_by_xpath("//*[@id='UC_FindJob_UC_Modal_CJOB']/div/div/div[3]/button[2]").click()

    driver.find_element_by_xpath("//*[@id='UC_FindJob_btn1']").click()
    table = driver.find_element_by_id("CPH1_tb_jobQueryResult")
    for i, hire in enumerate(get_hires(driver, table)):
        print(i)
        process_hire(hire, table)
    driver.find_element_by_xpath('//*[@id="spanExpendAll2"]').click()
    time.sleep(1000)
    driver.quit()


def get_hires(driver: webdriver.Chrome, table: WebElement) -> Iterator[WebElement]:
    idx = 0

    while True:
        hires = table.find_elements_by_css_selector(f"tr.post:nth-child(n+{idx * 2 + 2})")
        for hire in hires:
            yield hire
        if len(hires) == 0:
            break
        idx += len(hires)
        driver.execute_script("getPosts();")


def process_hire(hire: WebElement, table: WebElement) -> None:
    detail_id = hire.get_attribute("id").replace("hire", "detail")
    detail = table.find_element_by_id(detail_id)
    print(hire.get_attribute("outerHTML"))
    print(detail.get_attribute("outerHTML"))
    print("---------------------------------------")


if __name__ == '__main__':
    main()
