import requests
from bs4 import BeautifulSoup

# response = requests.get('https://job.taiwanjobs.gov.tw/internet/index/job_search_by_keyword.aspx')
response = requests.get('https://job.taiwanjobs.gov.tw/Internet/Index/Index.aspx')

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify(), file=open("text.html", "w+", encoding="utf-8"))

get_table = soup.find(id="CPH1_tb_jobQueryResult")
print(get_table)
