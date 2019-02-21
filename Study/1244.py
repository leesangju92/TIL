import sys
sys.stdin = open("1244.txt", "r")


def value_check(number):
    ten = len(number) - 1
    value = 0
    for num in number:
        value += int(num) * (10**ten)
        ten -= 1
    return value


def switch(number, N, n=0):
    if n == N:
        return number
    else:
        max_value = value_check(number)
        result = number
        for i in range(len(number)):
            for j in range(i + 1, len(number)):
                number[i], number[j] = number[j], number[i]
                value = value_check(number)
                if value > max_value:
                    max_value = value
                    result = number[:]
                number[i], number[j] = number[j], number[i]
        n += 1
        return switch(result, N, n)

def switch(number, N):
    new_numbers_list = [number]
    max_value, result = value_check(number), []
    for n in range(N):
        numbers_list, new_numbers_list = new_numbers_list, []
        for numbers in numbers_list:
            for i in range(len(numbers)):
                for j in range(i + 1, len(numbers)):
                    numbers[i], numbers[j] = numbers[j], numbers[i]
                    value = value_check(numbers)
                    if numbers not in new_numbers_list:
                        new_numbers_list += [numbers]
                    numbers[i], numbers[j] = numbers[j], numbers[i]
    return new_numbers_list

T = int(input())
for test_case in range(3):
    numberN = list(map(str, input().split()))
    number = []
    for char in numberN[0]:
        number += [char]
    N = int(numberN[1])
    print(switch(number, N))


