from bs4 import BeautifulSoup
import pandas as pd


def main():
    path = 'H:\PycharmProjects\Web_crawler\job_info.html'
    htmlfile = open(path, 'r', encoding='gbk')
    htmlhandle = htmlfile.read()
    soup = BeautifulSoup(htmlhandle, 'html.parser')
    # print(soup.prettify())
    catch_data(soup)


def catch_data(soup):
    tables = soup.findAll('table')
    tab = tables[0]
    for tr in tab.tbody.findAll('tr'):
        for td in tr.findAll('td'):
            text = td.getText()
            print(text)


if __name__ == '__main__':
    main()
