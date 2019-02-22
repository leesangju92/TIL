import sys
sys.stdin = open("1244.txt", "r")

def value_check(number):
    ten = len(number) - 1
    value = 0
    for num in number:
        value += int(num) * (10**ten)
        ten -= 1
    return value

def switch(number, N):
    new_numbers_list = [number]
    for n in range(N):
        numbers_list, new_numbers_list = new_numbers_list[:], []
        for numbers in numbers_list:
            for i in range(len(numbers)):
                for j in range(i + 1, len(numbers)):
                    numbers[i], numbers[j] = numbers[j], numbers[i]
                    # value = value_check(numbers)
                    if numbers not in new_numbers_list:
                        new_numbers_list = new_numbers_list + [numbers[:]]
                    numbers[i], numbers[j] = numbers[j], numbers[i]
    max_value, result = value_check(new_numbers_list[0]), new_numbers_list[0]
    for numbers in new_numbers_list:
        if value_check(numbers) > max_value:
            max_value = value_check(numbers)
            result = numbers
    result_str = ""
    for number in result:
        result_str += number
    return result_str

T = int(input())
for test_case in range(10):
    numberN = list(map(str, input().split()))
    number = []
    for char in numberN[0]:
        number += [char]
    N = int(numberN[1])
    print(f"#{test_case+1}",switch(number, N))