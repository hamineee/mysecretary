import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/"
h = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
r = requests.get(url, headers = h)
r.raise_for_status()
soup = BeautifulSoup(r.text, 'html.parser')

# with open('headline.html', 'w', encoding="utf8")as f:
#     f.write(soup.prettify())
   
lst = soup.find('ul', class_="hdline_article_list").find_all('li')
print('[헤드라인 뉴스]')
for index, item in enumerate(lst):
    title = item.find('a').text.strip()
    link = item.find('a').get('href')
    print(f'{index+1}.', title)
    print(f'(링크 : https://news.naver.com{link})')
