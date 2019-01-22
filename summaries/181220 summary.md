# 181220 Summary

## 1. 수업내용

### 1. Am I lucky  해설

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
        print("2등")     #또는 bonus_number in my_numbers
elif len(final_check) == 5:
        print("3등")
elif len(final_check) == 4:
        print("4등")
elif len(final_check) == 3:
        print("5등")
else:
        print("꽝")


# 또 다른 방법 1
# r=0
# for i in my_numbers:
#         if i in real_numbers:
#                 r += 1
# if r == 6:
#         print("1등")
# elif 

# 또 다른 방법2 이중 for문:
#  count = 0
# for my_number in my_numbers:
#         for real_number in real_numbers:
#                 if my_number == real_number:
#                         count += 1
# print(count)
#
# if count == 6:
#         print(1)
# elif count == 5 and bonus_number in my_numbers:
#         print(2)



#시뮬레이션 코드
# n = 0
# while True:
#         my_numbers = random.sample(numbers,6)
#         first_check = list(set(my_numbers) & set(real_numbers))
#         n = n + 1
#         if len(first_check) == 6:
#                 print(n)
#                 print(my_numbers)
#                 break
```

### 2. 함수 만들기

```python
import requests
import random

def pick_lotto():
    numbers = random.sample(range(1,46),6)
    return numbers 

def get_lotto(draw_no): #()안에 있는 것이 변수라고 생각해도 된다.args(arguments) 
    url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo='+ str(draw_no) #자료형은 통일시켜줄 것
    lotto_data = requests.get(url, verify=False).json()
    bonus_number = lotto_data['bnusNo']
    numbers = []   
    for key,value in lotto_data.items():
        if 'drwtNo' in key:
            numbers.append(value)
    return {'numbers':numbers, 'bonus':bonus_number}

def am_i_lucky():
    num_check = list(set(my_numbers) & set(real_numbers['numbers']))
    if len(num_check) == 6:
        print('1등') 
    elif len(num_check) == 5 and real_numbers['bonus'] in my_numbers:
        print('2등')
    elif len(num_check) == 5:
        print('3등')
    elif len(num_check) == 4:
        print('4등')
    elif len(num_check) == 3:
        print('5등')
    else:
        print('꽝')


my_numbers = pick_lotto()
print(my_numbers)

real_numbers = get_lotto(832)
print(real_numbers)

am_i_lucky()

```

```python
def am_i_lucky(pick, draw):
    match = set(pick) & set(draw)
    if len(match) == 6:
        print('1등')
    elif len(match) == 5:
        print('3등')
    else:
        print('꽝')


def am_i_lucky(pick, draw):
    match = set(pick) & set(draw)
    if len(match) == 6:
        return('1등')      리턴 뒤에 괄호 있어도 되고 없어도 된다.
    elif len(match) ==5:
        return('3등')
    else:
        return('꽝')
```

```python
import requests
import random

def pick_lotto():
    numbers = random.sample(range(1,46),6)
    return numbers 

def get_lotto(draw_no):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+ str(draw_no) 
    lotto_data = requests.get(url).json()
    bonus_number = lotto_data['bnusNo']
    numbers = []   
    for key,value in lotto_data.items():
        if 'drwtNo' in key:
            numbers.append(value)
    return {'numbers':numbers, 'bonus':bonus_number
         
def am_i_lucky(pick, draw):
    num_check = list(set(pick) & set(draw['numbers']))
    if len(num_check) == 6:
        return '1등' 
    elif len(num_check) == 5 and draw['bonus'] in pick:
        return '2등'
    elif len(num_check) == 5:
        return '3등'
    elif len(num_check) == 4:
        return '4등'
    elif len(num_check) == 3:
        return '5등'
    else:
        return '꽝'

result = am_i_lucky(pick_lotto(),get_lotto(831))
print(result)
        
```

### 3. 함수 호출

```python
math_functions.py

print(__name__)

def average(numbers):
    return sum(numbers)/len(numbers)

def cube(x):
    return x*x*x

def main():
    my_score = [79,84,66,93]
    print('평균:',average(my_score))
    print(cube(3))

if __name__ == '__main__':
    main()
```

```python
do_math.py

print(__name__)

# import math_functions
# math_functions.cube(5)
# math_functions.average([10,20,30])

from math_functions import cube,average
#여기서 import한 파일에서 print(__name__)하면 __main__이 아닌 해당 파일이름이 나온다.



print(average([10,20,30]))
print(cube(5))

```

```python
# import lotto_functions
# lotto_functions.am_i_lucky(lotto_functions.pick_lotto(),lotto_functions.get_lotto() )

from lotto_functions import am_i_lucky,get_lotto,pick_lotto

result = am_i_lucky(pick_lotto(),get_lotto())
print(result)
```







## 2. 기억해야할 것

* HTML에서 h1, h2, h3, h4, h5, h6는 글자 크기 조정 기능이 아닌 역할지정 기능

* ☆CSS 만져보기

* 변수 설정시에 주의할 점 : str 같은 이미 있는 함수를 변수로 설정할시에는 str()같은 것은 사용못함

  ```python
  str = 'ssafy'
  str() #불가능
  sum = ~~~~~
  sum() #불가능
  ```

* set() 하면 집합으로 된다. 연산자 &(교집합) -(차집합) 사용 가능

* def 함수 할때 마지막에  return이 있어야 한다. 없으면 None이 뜬다.

  ```python
  #.sort()는 return 없음 sorted()는 return 있음
  a = sorted([3,2,1])
  b = [3,2,1].sort()
  print(a,b) 
  #결과값 : [1,2,3] None
  ```

* sudo pip3 install flask 

* export FLASK_APP=app.py

* from flask import Flask ,jsonify

* app = Flask(__name__)

* @app.route("/")

* def index():

  return 'Happy Hacking'



flask run



flask run -h 0.0.0.0 -p 8080



run preview 클릭 running aplication



오른쪽 상단

pop out into new window



ctrl + c



@app.route("/")

def index():

return 'happy hacking'

@app.route ("/hi")

def hi():

return 'hello ssafy'

/hi하면 not found



f6 끄고 키는거? 



@app.route("/pick_lotto")

def pick_lotto():

return  'hmmmm'



#random.sample(range(1,46),6)



export FLASK_ENV=development

이러면 저장할때마다 자동으로 껐다 켜짐

flask run -h 0.0.0.0 -p 8080



list는 바로 못 보여줌

jsonify( )

@app.route("/get_lotto")

def get_lotto():

data = {

'numbers':[1,2,3,4,5],

'bonus' : 7

}

주소창 get_lotto

