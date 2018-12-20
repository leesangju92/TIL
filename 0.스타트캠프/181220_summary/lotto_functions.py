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
    return {'numbers':numbers, 'bonus':bonus_number}

# 내가 한 방법
# def am_i_lucky(my_numbers, real_numbers):
#     num_check = list(set(my_numbers) & set(real_numbers['numbers']))
#     if len(num_check) == 6:
#         return '1등' 
#     elif len(num_check) == 5 and real_numbers['bonus'] in my_numbers:
#         return '2등'
#     elif len(num_check) == 5:
#         return '3등'
#     elif len(num_check) == 4:
#         return '4등'
#     elif len(num_check) == 3:
#         return '5등'
#     else:
#         return '꽝'


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


my_numbers = pick_lotto()
print(my_numbers)

real_numbers = get_lotto(831)
print(real_numbers)

result = am_i_lucky(pick_lotto(),get_lotto(822))
print(result)

# result = am_i_lucky(my_numbers,real_numbers)
# print(result)

# result = am_i_lucky([1,2,3,4,8,6],{'numbers':[1,2,3,4,5,7], 'bonus':6})
# print(result)


# real_numbers.sort()



    #1,2,3,4,5,6
    #[1,2,3,4,5,6] 7
    #{numbers : [1,2,3,4,5,6], bonus:7}

# first_check = list(my_numbers & real_numbers)
# second_check = list(my_numbers & bonus_number_list)
# final_check = list(my_numbers & real_numbers+bonus_number_list)

# if len(first_check) == 6:
#         print("1등")
# elif len(first_check) == 5 and len(second_check) == 1 :
#         print("2등")     #또는 bonus_number in my_numbers
# elif len(final_check) == 5:
#         print("3등")
# elif len(final_check) == 4:
#         print("4등")
# elif len(final_check) == 3:
#         print("5등")
# else:
#         print("꽝")
