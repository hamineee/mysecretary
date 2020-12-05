import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

def scrape_weather():
    url = "https://search.naver.com/search.naver?query=날씨"
    soup = create_soup(url)
    data = soup.find('div', class_='today_area _mainTabContent')
    cast = data.find('ul', class_='info_list').find('p',class_='cast_txt').text
    today_w = data.find('p', class_="info_temperature").text.replace('도씨','') #replace()로 지우고 싶은 text를 공백으로 대체해줄 수 있음
    min_tem = data.find('span', class_="min").text
    max_tem = data.find('span', class_="max").text
    rain_am = soup.find('span', class_="point_time morning").text.strip()
    rain_pm = soup.find('span', class_="point_time afternoon").text.strip()
    dust = soup.find('dl', class_="indicator").find_all('dd')[0].text   #class 이름으로 구분 되지 않을 땐 리스트 순서로 찾아준다.
    super_dust = soup.find('dl', class_="indicator").find_all('dd')[1].text

    print('오늘의 날씨')
    print()
    print(cast)
    print('현재 {}(최저 {}/최고 {})'.format(today_w,min_tem,max_tem))
    print('오전 {} / 오후 {}'.format(rain_am,rain_pm))
    print('미세먼지 {}'.format(dust))
    print('초미세먼지 {}'.format(super_dust))
    print()

def scrape_headline_news():
    print('[헤드라인 뉴스]')
    url = "https://news.naver.com/"
    soup = create_soup(url)
    headline_lst = soup.find('ul', class_="hdline_article_list").find_all('li', limit=3) #limit: list 가져오는 개수 제한할 수 있음
    for index, news in enumerate(headline_lst):
        title = news.find('a').text.strip()
        #link = news.find('a').get('href')
        link = url + news.find('a')["href"]
        print('{}. {}'.format(index+1, title))
        print('(링크: {})'.format(link))
        print()
        
scrape_weather()
scrape_headline_news()
    