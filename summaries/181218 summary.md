# 181218 수업정리 `Ctrl + 1`

## 1. 개발환경 설정  `Ctrl + 2`

* Chocolatey `*+ space` 
  * 인스톨 매니저 `Enter후 tab`	
* python 3.6.7
* Git
* Chrome

* Typora

## 2. 수업 내용

### 0. 기초

```python
- print ("happy hacking")

- first_name = 'Lee'
  last_name = 'sangju'
  full_name = first_name + last_name

- height = 1.77
  weight = 60
  bmi = weight / height**2

- if (10%2 == 1):

      print ('홀수')

  else:

      print ('짝수')

- 'true' = str \ true(변수설정 못함) = bool \ 1 = int \ 10.2=float
```



### 1-1. list

```python
numbers = [1,2,3] #변수 이름은 뜻을 담아서 짓자
family = ['mom',1.64,'dad',1.74,'sister',1.56, True]
mcu = [
['ironman','captain america'],
['deadpool', 'xman'],
['spiderman']
]

#deadpool을 문자만 꺼내려면 어떻게 해야할까? mcu[1][0]
```

### 1-2. list 추출, 슬라이싱, 연산,제거

```python
family[-1]
family[-3:-1]
family[-3:]
family[:-1]
mcu[0][1]

x = ['life', 'is', 'short', True, 123, ['you', 'need', 'python']]
my_bool = x[3]
my_bool = x[3:4] # 이렇게 슬라이싱하면 하나가 나와도 list 형식으로 나옴
my_bool = x[-3]

team = [
    'john',
    10000,
    'neo',
    100,
    'tak',
    40500
]

team[-1] #40500
team[2:4] #['neo',100]

new_member = ['js',10]

team = team + new_member # team += new_member
#team = ['john',10000,'neo',100,'tak',40500,'js',100]

del(team[2]) #neo 사라짐, 또하면 100 사라짐 del(team[2:4])형식도가능
```



### 2. Range 함수 사용하기

```python
#문제 : 리스트 안에 내용들은 쉼표로 구분되어야 한다. 띄어쓰기로는 에러가 발생
numbers = list(range(1,46))
numbers = list(range(100))
numbers[2:5] #[start:end] start는 포함하며 end는 포함하지 않음 0,1,2(3번째)부터 5번째수
```



### 3-1. dict(dictionary)

* key(거의 str) : value 구조로 이어져 있음

```python
my_info = {
    'name':'neo', 
    'job':'hacker',
    'mobile':'01099275830',
    'email':'leesangju92@gmail.com'
}

my_info['name'] 

#이러면 neo가 나옴
```



### 3-2. dict 추출

```python
my_info = [
{
    'name':'john', 
    'job':'hacker',
    'mobile':'01099275830',
    'email':'leesangju92@gmail.com'
},
{
    'name':'neo', 
    'job':'player',
    'mobile':'01099275831',
    'email':'leesangju93@gmail.com'
},
{
    'name':'tak', 
    'job':'developer',
    'mobile':'01099275832',
    'email':'leesangju94@gmail.com'
}
]

print(my_info[1]['job']) 

#답은 player 실제로는 my_info[1]['job'][2]['data].. 
```

### 4. function

* 소괄호가 옆에 붙어 있으면 무조건 함수

```python
print('hi')
len('hi')   #2
len([1,2,3,4,5])    #5
del()
type('a')

scores = [45,68,78,88]
high_score = max(scores)
lowest_score = min(scores)


round(1.8) #2
round(1.876, 2) #1.88
#ceil() 올림 ← import해야함
#floor() 내림 ← import해야함


first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# full에 first와 second를 합쳐서 저장
full = first + second

# full_sorted에 full을 정렬하여 저장
full_sorted = sorted(full)

# *revers_sorted에 full을 내림차순으로 정렬하여 저장
revers_sorted= sorted(full, reverse=True) 

full.sort()
full.sort(reverse=True) #이건 정렬, 역정렬 시키는데 저장은 못시킨다. 출력이 되지 않기 때문
```

### 5. Method `점(.)이 찍혀있으면 Method`

```python
my_list = [4,7,9,1,3,6]
#최대/최소
max(my_list)
min(my_list)
#특정 요소의 인덱스?  Ex : my_list에서 3의 위치
my_list.index(3)
#리스트를 뒤집으려면?
my_list.reverse()

dust = 100  # <class : int> 100은 int 오브젝트
lang = 'python' #str 스트링 오브젝트
samsung = ['elec', 'sds', 's1'] #list

samsung.index('sds') #1

lang.capitalize() #lang은 그대로 있으며 Python만 출력됨
lang.replace('on','off') # 원본은 그대로, pythoff만 출력
lang.index('o')

samsung.sort() #이 경우에는 원본이 바뀌어버리고 출력되진 않음. 통일되지 않았음.

samsung.append('bio') #samsung + ['bio']

#이때 new_samsung = samsung.append('bio')해도 저장안됨. 출력이 안되고 원본만 바뀌기 때문
```

| 클래스   | int  | str      | list            | dic                         |
| -------- | ---- | -------- | --------------- | --------------------------- |
| 오브젝트 | 1    | strin'g' | one, two, three | 'one':1, 'two':2, 'three':3 |

`표 만드려면 |(원화+shift)이용`

### 6. 로또만들기

```python
import requests

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)

lotto_data = response.json()

common_words = 'drwtNo'

real_numbers = []   #이거 꼭 필요하다. (.append를 사용하려면)

for key in lotto_data:
    if common_words in key: # 또는 if 'drwtNo' in key:
        real_numbers.append(lotto_data[key])

real_numbers.sort()

print(real_numbers)

#lotto_data = requests.get(url, verify=False).json()

# real_numbers = [
#     lotto_data['drwtNo1'],
#     lotto_data['drwtNo2'],
#     lotto_data['drwtNo3'],
#     lotto_data['drwtNo4'],
#     lotto_data['drwtNo5'],
#     lotto_data['drwtNo6'],
# ] 모두 주석 처리는 Ctrl + /
```

### 7. 로또 번호 가져오기

```python
import requests

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)

lotto_data = response.json()

common_words = 'drwtNo'

real_numbers = []   #이거 꼭 필요하다. (.append를 사용하려면)

# for key in lotto_data:
#     if common_words in key:   # 또는 if 'drwtNo' in key:
#         real_numbers.append(lotto_data[key])

for key,value in lotto_data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)


real_numbers.sort()
bonus_number = lotto_data['bnusNo']
print(real_numbers)

#lotto_data = requests.get(url, verify=False).json()

# real_numbers = [
#     lotto_data['drwtNo1'],
#     lotto_data['drwtNo2'],
#     lotto_data['drwtNo3'],
#     lotto_data['drwtNo4'],
#     lotto_data['drwtNo5'],
#     lotto_data['drwtNo6'],
# ] 모두 주석 처리는 Ctrl + /
```

### 8. 날씨 가져오기

```python
from darksky import forecast

multicampus = forecast('dd996bfc7faf684b8807f014ee6ec994', 37.50509, 127.042665)

print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])


# import requests

# url = 'https://api.darksky.net/forecast/dd996bfc7faf684b8807f014ee6ec994/37.505090,%20127.042665'

# response = requests.get(url)
# data = response.json()

# print(data['currently']['summary'])
```



## 3. 오늘 기억해야 할 것 `Enter 2번 또는 클릭`

* 설치한 것들
  * Python 3.6.7
  * VScode
  * Chocolatey
  * Typora
  * Git

* VScode 명령어들

  * cd /c users
  * cd ~ = cd /c/users/student (홈이란 뜻)
  * cd / → 루트 최상단
  * VScode에서 ①mkdir : 폴더 생성 ②rmdir : 폴더 제거 ③tab : 자동완성 ④touch : 파일 생성
  * python 파일명.py
  * python -i
  * exit() Ctrl+z // $일때 Ctrl+L = clear
  * 3**2 = 9 
  * 3*2 = 6
  * 4/2 = 2.0 (실수가 나옴) 사칙연산기호 지원, 계산우선순위 같음
  * 10%3 = 1 (나머지)9%
  * 키보드↑ 이전에 사용했던 명령어
  * #주석다는것
  * -1 : 마지막
  * n차원 리스트(배열)
  * range(1,46) , list(range(1,46)), list(range(100))
  * number = int('123') , number + 3 = 126 
  * int(True) = 1 int(False) = 0 
  * 백틱(`) 3번 + enter 하면 코드 박스 생김라벨 만들기 백틱 + 하고싶은말 + 백틱
  * 불러오는것은 무조건 `[]`  
  * python 함수 documentation : 공식문서 구글링하는 방법 또는 `help(함수)` 
  * `round(number[, ndigits]) -> number` 소괄호 안 중에 대괄호 안은 옵션, 나머지는 필수 
  * pypi
  * $ git commit -m "변경사항"  Ex: ~20181218
