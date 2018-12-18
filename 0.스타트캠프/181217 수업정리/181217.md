# 181217 수업정리

## 1. 수업내용

### 리스트

`list [숫자, 글자, 참/거짓, 리스트]`  호출할 때는 `list[0]`

### 딕셔너리

`{"가족":4. "부모님":2}`  접근할 때는 `dic["가족"]` 

### 반복문

```python
while (조건문):
    문장1
    문장2 #종료조건이 필요함

for i in I;
	print(M) #종료조건이 필요하지 않음
```

### 함수를 호출

```python
import requests
from bs4 import BeautifulSoup
```

### 날씨

```python
import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID={}".format(key)

data = requests.get(url).json()
weather = data['weather'][0]['description']
temp = float(data['main']['temp'])-273.15
temp_min = float(data['main']['temp_min'])-273.15
temp_max = float(data['main']['temp_max'])-273.15

print("""서울의 오늘 날씨는 [{}] 이며, 섭씨 {:.1f}도 입니다.
최저/최고 온도는 {:.1f}/{:.1f}도 입니다.
""".format(weather, temp, temp_min, temp_max)
)
```

### Hi

```python
greeting = "bon jour"
print(greeting)
print(greeting)
print(greeting)
print(greeting)
print(greeting)
```

### 점심메뉴

```python
import random

menu=["김치볶음밥","김치찌게","된장찌게", "탕수육"]

choice = random.choice(menu)

print(choice)
```

### 미세먼지

```python
import requests
from bs4 import BeautifulSoup

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey={}&sidoName=서울&pageNo=3'.format(key)
response = requests.get(url).text
soup = BeautifulSoup(response, 'xml')
gn = soup('item')[7]
location = gn.stationName.text
time = gn.dataTime.text

# 얘가 중요한 것!
dust = int(gn.pm10Value.text)

print('{0} 기준: 서울시 {1}의 미세먼지 농도는 {2} 입니다.'.format(time, location, dust))

if 150 < dust:
  print ("매우나쁨")
elif 80 < dust:
  print ("나쁨")
elif 30 < dust:
  print ("보통")
else:
  print ("좋음")
# 그래서 지금 공기가 어느정도로 안좋은건데..?

```

### 로또

```python
# 1. random 외장 함수 가져오기
import random
# 2. 1~45까지 숫자 numbers에 저장하기
numbers = range(1,46)
# 3. numbers에서 6개 뽑기 lucky numbers에 저장
lucky_numbers = random.sample(numbers,6) 
#정렬
lucky_numbers.sort()
# 4. 출력하기
print (lucky_numbers)
```

### 코스피

```python
import requests
from bs4 import BeautifulSoup

response = requests.get('https://finance.naver.com/sise/')
doc = response.text
soup = BeautifulSoup(doc,'html.parser')
kospi = soup.select_one('#KOSPI_now').text
kosdaq = soup.select_one('#KOSDAQ_now').text


print("코스피",kospi)
print("코스닥",kosdaq)
```

### 환율

```python
import requests
from bs4 import BeautifulSoup

response = requests.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section')# 코드는 숨겨져 있어요
doc = response.text
#URL을 정의하고, res = requests.get(URL).text 하는 것으로도 가능 이때 doc는 필요없음
soup = BeautifulSoup(doc,'html.parser')

data_set = soup.select('.value')
#value앞의 점은 class를 의미
data1 = data_set[0].text
data2 = data_set[1].text
print("오늘의 달러 환율은 : ",data1)
print("오늘의 엔화 환율은 : ",data2)
#print("오늘의") print(data_set[0].text)도 가능

```

### 주식

```python
# 코드는 숨겨져 있어요
from iexfinance.stocks import Stock

corps = Stock(["TSLA", "AAPL", "GOOGL", "AMZN"])

data_set=corps.get_price()

#tsla = Stock('TSLA').get_price()

print(data_set)
#print(data_set["TSLA"])

```



### 2. 기억해야할 것

* .value 앞의 점은 클래스를 의미
* `select_one` 은 맨위 하나를 선택하며 `.text ` 같이 형식을 붙일 수 있음
* `select`는 여러개 선택하지만 형식을 붙일 순 없음
* 리스트 같이 복수형인 경우 `_set`같은 것을 이름에 붙여주자
* 무료 교육 사이트 : UDACITY, EDX, COURSERA. CS50
* 정렬하는 방법은 `XXX.sort()` 
* 부등호에서 등호는 무조건 맨 마지막 `<=` 