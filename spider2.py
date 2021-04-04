import requests

url = 'https://job.taiwanjobs.gov.tw/internet/index/job_search_by_keyword.aspx'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print('取得網頁成功')
else:
    print('取得失敗')
print(htmlfile.text)
