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


numbers = list(range(1,46)) 

my_numbers = random.sample(numbers,6)

my_numbers.sort()

print(my_numbers)
print(real_numbers)



# my_numbers, real_numbers, bonus_number
# 1등 : my_numbers == real_numbers
# 2등 : real & my가 5개가 같고, my의 나머지 하나가 bonus_number
# 3등 : real & my가 5개가 같다
# 4등 : real & my가 5개가 같다
# 5등 : real & my가 5개가 같다
# 꽝