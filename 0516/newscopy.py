# newscopy.py

#ctrl + shift + p -> python: Select Insterpreter 선택-> base~ 선택
#pip install beautifulsoup4
from bs4 import BeautifulSoup

import requests


headers = {
    "Uesr-Agent":"Dongyang"
}
#뉴스
webpage = requests.get("https://newsis.com/view/?id=NISX20230324_0002240442&cID=10401&pID=10400", headers=headers)
print(webpage)

#html 코드
soup = BeautifulSoup(webpage.content, "html.parser")
print(soup)

#내용
#article
news = soup.select_one("article").get_text().strip()
print(news)

'''
webpage2 = requests.get("http://www.domin.co.kr/news/articleView.html?idxno=1416639")
print(webpage2)
news2 = soup.select_one("article").get_text().strip()
print(news2)
'''
