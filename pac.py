import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://bj.ke.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
url=input('输入网站：')
response = requests.get(url,headers=headers)
if response.status_code == 200:
   html_content=response.text
soup = BeautifulSoup(response.text, 'html.parser')
divs=soup.find('div',class_="mediainfo_mediaRight__SDOq4")
for div in divs:
    print(div.get_text())