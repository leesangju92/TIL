import requests
from bs4 import BeautifulSoup
from random import *

url = 'https://www.daum.net/'

doc = requests.get(url).text
#URL을 정의하고, res = requests.get(URL).text 하는 것으로도 가능 이때 doc는 필요없음
soup = BeautifulSoup(doc,'html.parser')

data_set = soup.select('.link_issue')

select_one_number =  randrange(1, 21, 2)-1
data = data_set[select_one_number]
print(select_one_number)

print(data_set)
#value앞의 점은 class를 의미
data1 = data_set[0].text
data2 = data_set[1].text
print("오늘의 달러 환율은 : ",data1)
print("오늘의 엔화 환율은 : ",data2)
#print("오늘의") print(data_set[0].text)도 가능py