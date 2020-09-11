import requests
from bs4 import BeautifulSoup

url = "http://hackers.co.kr/?c=s_eng/eng_contents/I_others_english"
r = requests.get(url)
r.raise_for_status()

soup = BeautifulSoup(r.text, 'html.parser')

# with open('eng.html', 'w')as f:
#     f.write(soup.prettify())


kor = soup.find_all('div', class_="conv_txt")[0]
eng = soup.find_all('div', class_="conv_txt")[1]

kor_sub = kor.find_all('span', class_="conv_sub")
eng_sub = eng.find_all('span', class_="conv_sub")

print('[오늘의 영어 회화]')
print('(영어 지문)')
for sub in eng_sub:
    print(sub.text)

print('(한글 지문)')
for sub in kor_sub:
    print(sub.text)

