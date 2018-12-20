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


# my_numbers, real_numbers, bonus_number
# 1등 : my_numbers == real_numbers
# 2등 : real & my가 5개가 같고, my의 나머지 하나가 bonus_number
# 3등 : real & my가 5개가 같다
# 4등 : real & my가 5개가 같다
# 5등 : real & my가 5개가 같다
# 꽝
