# 181219 - Flask를 활용한 어플리케이션 구축

## 1. 수업 내용

### 1. 평균 구하기

```python
my_score = [79,84,66,93]

sum_one = 0

for score in my_score:
    sum_one += score 

my_average = sum_one/len(my_score)

print(my_average)
#float

your_score = {
    "수학" : 87,
    "국어" : 83,
    "영어" : 76,
    "도덕" : 100
}
#float

sum_two = 0

# 다른방법1 : for subject in your_score:
#                sum_two += your_score[subject]

# 다른방법2 : your_score_average = sum(your_score.values())/len(your_score)

for key,value in your_score.items():
    sum_two += value

your_score_average = sum_two/len(your_score)

print(your_score_average)

```

`your_score.items()와 your_score.values()로 나오는것은 형태만 리스트이며 순서로 꺼낼 순 없다`

`합계를 구하는 함수 : sum() 딕셔너리-리스트 형태변환 메소드 : xxx.items() , xxx.values() `

### 2. 평균온도

```python
cities_temp = {
    '서울' : [-6, -10, 5],
    '대전' : [-3, -5, 2],
    '광주' : [0, -5, 10],
    '구미' : [2, -2, 9]
}

# for city in cities_temp:   <한손으로 key만 꺼내요>
#     temperatures = cities_temp[city]
#     avg_temperature = round(sum(cities_temp[city])/len(temperatures),2)
#     print(city, avg_temperature)
#     print(city + ':' + str(avg_temperature))
#     print('{0} : {1}', format(city, avg_temperature))


for city in cities_temp:
    temp_sum = sum(cities_temp[city])
    print(city, ':' ,round(temp_sum/len(cities_temp[city]),2))

```



### 3. 최고 온도, 최저 온도

```python
cities_temp = {
    '서울' : [-6, -10, 5],
    '대전' : [-3, -5, 2],
    '광주' : [0, -5, 10],
    '구미' : [2, -2, 9]
}

temp_hot = {}     # ★괄호의 형태에 따라 딕셔너리, 리스트 정해진다는 것을 기억
temp_cold = {}
temp_hot_list =[]
temp_cold_list = []


for city, temp in cities_temp.items():
    temp_hot[city] = max(temp)        #여기서 city(key)값은 자동으로 들어간다고 한다.

print(temp_hot)

for city, temp in cities_temp.items():
    temp_cold[city] = min(temp)

print(temp_cold)


for key,value in cities_temp.items():    #  <양손으로 key,value 둘다 꺼내요>
    temp_order_hot = max(value)
    temp_hot_list.append(temp_order_hot)

temp_hot_list.sort(reverse=True)

hottest_temp = temp_hot_list[0]


for key,value in cities_temp.items():
    temp_order_cold = min(value)
    temp_cold_list.append(temp_order_cold)

temp_cold_list.sort()

coldest_temp = temp_cold_list[0]

for city, temp in temp_hot.items():
    if temp == hottest_temp:
        print('가장 더웠던 도시는 :',city)

for city, temp in temp_cold.items():
    if temp == coldest_temp:
        print('가장 추웠던 도시는 :',city)

```

모범답안

```python
cities_temp = {
    '서울' : [-6, -10, 5],
    '대전' : [-3, -5, 2],
    '광주' : [0, -5, 10],
    '구미' : [2, -2, 9]
}

#all_temp에 모든 기온을 모은다
all_temp = []
for city, value in cities_temp.items():
    all_temp += value    #★ 리스트형식이라 자동으로 더해지는 것으로 보인다.
#all_temp에서 highest/lowest를 찾는다
highest = max(all_temp)
lowest = min(all_temp)
print(highest, lowest)
#cities_temp에서 highest/lowest가 속한 도시를 찾는다
hottest = []
coldest = []
for key, value in cities_temp.items():
    if highest in value:
        hottest.append(key)
    if lowest in value:
        coldest.append(key) 

```

### 4. Am I lucky? (실제로또번호와 랜덤생성번호 비교)

```python
import requests
import random

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)

lotto_data = response.json()

real_numbers = []   

for key,value in lotto_data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)



real_numbers.sort()
bonus_number = lotto_data['bnusNo']
bonus_number_list = [bonus_number]

numbers = list(range(1,46)) 

my_numbers = random.sample(numbers,6)

my_numbers.sort()

print(my_numbers)
print(real_numbers)
print(bonus_number)

# my_numbers = [1,5,3,4,8,6]
# real_numbers = [1,2,10,9,8,7]
# bonus_number_list = [2]

first_check = list(set(my_numbers) & set(real_numbers))
second_check = list(set(my_numbers) & set(bonus_number_list))
final_check = list(set(my_numbers) & set(real_numbers+bonus_number_list))

if len(first_check) == 6:
        print("1등")
elif len(first_check) == 5 and len(second_check) == 1 :
        print("2등")
elif len(final_check)== 5:
        print("3등")
elif len(final_check) == 4:
        print("4등")
elif len(final_check) == 3:
        print("5등")
else:
        print("꽝")

# my_numbers, real_numbers, bonus_number
# 1등 : my_numbers == real_numbers
# 2등 : real & my가 5개가 같고, my의 나머지 하나가 bonus_number
# 3등 : real+bonus & my가 5개가 같다
# 4등 : real+bonus & my가 5개가 같다
# 5등 : real+bonus & my가 5개가 같다
# 꽝
```



## 2. 기억해야 할 것

* git status

* 새로 수정을 하거나 하면 git add . (버전을 남긴다. 사진을 찍는다.)

* git commit -m "남기고 싶은 말"

* git log

* git clone https://github.com/BlackrockDigital/startbootstrap-creative.git 

* 뭐라 컴퓨터 이름을 짓든 ~/workplace

* git add . → git commit -m " " → git push 순으로 

* cd 주소

* ```python
  #딕셔너리를 리스트 모양으로 변환하는 방법
  
  temp=[]
  dictlist=[]
  
  for key, value in your_score.items():
     temp = [key,value]
     dictlist.append(temp)
  ```

* 설치할만한 크롬 확장 프로그램 : Onetab, Momentum

* cloud9(어디서든지, 어떤 PC든지 같은 코딩을 할 수 있는 서비스) 세팅 `Public URL빈칸 blank 선택` 
* codecademy 는 코드 학습 사이트
* bootstrap 에서 무료로 좋은 사이트 템플릿을 가져올 수 있음
* HTML에서 실행할거면 꼭 index에서 run을 클릭
*  href="css/creative.css" min.은 띄어쓰기 엔터 모두 없앤것.
* repository name : leesangju92.github.io

````
- Git 설정 순서
git init 
git add
git commit -m 'first commit'
git config --global user.name 'leesangju92'
git config --global.user.email 'leesangju92@gmail.com'
git log
git remote add origin https://github.com/leesangju92/leesangju92.github.io.git
이건 복사해서 붙여넣기
git remote -v
git push -u (첫번째만) origin master
username for 'https' : leesangju92 + 비밀번호 입력
username.github.io
````

