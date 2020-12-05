import requests
from bs4 import BeautifulSoup

url = ("https://search.naver.com/search.naver?query=날씨")
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

# with open('weather.html','w', encoding="utf8")as f:
#     f.write(soup.prettify())

data = soup.find('div', class_='today_area _mainTabContent')
cast = data.find('ul', class_='info_list').find('p',class_='cast_txt').text
today_w = data.find('span', class_="todaytemp").text
min_tem = data.find('span', class_="min").find('span', class_="num").text
max_tem = data.find('span', class_="max").find('span', class_="num").text
data_rain = soup.find('li', class_="date_info today")
rain_am = data_rain.find('span', class_="rain_rate wet").find('span', class_='num').text
rain_pm = data_rain.find('span', class_="rain_rate").find('span', class_='num').text
dust = soup.find('dl', class_="indicator").find_all('dd')[0].text
super_dust = soup.find('dl', class_="indicator").find_all('dd')[1].text


print('[오늘의 날씨]')
print(cast)
print(f'현재{today_w} (최저 {min_tem}/최고{max_tem}')
print(f'오전 강수확률 {rain_am} / 오후 강수확률 {rain_pm}')
print(f'미세먼지 {dust}')
print(f'초미세먼지 {super_dust}')