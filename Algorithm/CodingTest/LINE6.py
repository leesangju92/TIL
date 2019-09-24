import sys
sys.stdin = open("LINE6.txt", "r")

N, align = input().split()

max_height = 0
number_list = []
for n in range(int(N)):
    size, numbers = input().split()
    max_height = max(max_height, 2*int(size)-1)
    number_list.append([int(size), numbers])

if align == "TOP":
    for mh in range(max_height):
        for number in number_list:
            for num in number[1]:
                if mh == 0:
                    if num in ["0", "2", "3", "5", "7", "8", "9"]:
                        print(number[0] * "#", end=" ")
                    elif num == "1":
                        print((number[0]-1) * "." + "#", end=" ")
                    elif num == "4":
                        print("#" + (number[0]-2) * "." + "#", end=" ")
                    elif num == "6":
                        print("#" + (number[0]-1) * ".", end=" ")
                elif mh < number[0] - 1:
                    if num in ["1","2","3", "7"]:
                        print((number[0] - 1) * "." + "#", end=" ")
                    elif num in ["4", "8", "9", "0"]:
                        print("#" + (number[0] - 2) * "." + "#", end=" ")
                    else:
                        print("#" + (number[0] - 1) * ".", end=" ")
                elif mh == number[0] - 1:
                    if num in ["1", "7"]:
                        print((number[0] - 1) * "." + "#", end=" ")
                    elif num == "0":
                        print("#" + (number[0] - 2) * "." + "#", end=" ")
                    else:
                        print(number[0] * "#", end=" ")
                elif mh < 2*number[0] - 2:
                    if num in ["1", "3", "4", "5", "7", "9"]:
                        print((number[0] - 1) * "." + "#", end=" ")
                    elif num in ["8", "0", "6"]:
                        print("#" + (number[0] - 2) * "." + "#", end=" ")
                    else:
                        print("#" + (number[0] - 1) * ".", end=" ")
                elif mh == 2*number[0] - 2:
                    if num in ["2", "3", "5", "6", "8", "0"]:
                        print(number[0] * "#", end=" ")
                    else:
                        print((number[0]-1) * "." + "#", end=" ")
                else:
                    print(number[0]*".", end=" ")
        print()

elif align == "BOTTOM":
    for mh in range(max_height):
        for number in number_list:
            for num in number[1]:
                h = max_height - 2*(number[0] - 1) - 1
                if mh < h:
                    print(number[0] * ".", end=" ")
                elif mh == h:
                    if num in ["0", "2", "3", "5", "7", "8", "9"]:
                        print(number[0] * "#", end=" ")
                    elif num == "1":
                        print((number[0]-1) * "." + "#", end=" ")
                    elif num == "4":
                        print("#" + (number[0]-2) * "." + "#", end=" ")
                    elif num == "6":
                        print("#" + (number[0]-1) * ".", end=" ")
                elif mh < h + number[0] - 1:
                    if num in ["1","2","3", "7"]:
                        print((number[0] - 1) * "." + "#", end=" ")
                    elif num in ["4", "8", "9", "0"]:
                        print("#" + (number[0] - 2) * "." + "#", end=" ")
                    else:
                        print("#" + (number[0] - 1) * ".", end=" ")
                elif mh == h + number[0] - 1:
                    if num in ["1", "7"]:
                        print((number[0] - 1) * "." + "#", end=" ")
                    elif num == "0":
                        print("#" + (number[0] - 2) * "." + "#", end=" ")
                    else:
                        print(number[0] * "#", end=" ")
                elif mh < h + 2*number[0] - 2:
                    if num in ["1", "3", "4", "5", "7", "9"]:
                        print((number[0] - 1) * "." + "#", end=" ")
                    elif num in ["8", "0", "6"]:
                        print("#" + (number[0] - 2) * "." + "#", end=" ")
                    else:
                        print("#" + (number[0] - 1) * ".", end=" ")
                elif mh == h + 2*number[0] - 2:
                    if num in ["2", "3", "5", "6", "8", "0"]:
                        print(number[0] * "#", end=" ")
                    else:
                        print((number[0]-1) * "." + "#", end=" ")
        print()


elif align == "MIDDLE":
    for mh in range(max_height):
        for number in number_list:
            for num in number[1]:
                h = (max_height - 2*(number[0] - 1) - 1)//2
                if mh < h:
                    print(number[0] * ".", end=" ")
                elif mh == h:
                    if num in ["0", "2", "3", "5", "7", "8", "9"]:
                        print(number[0] * "#", end=" ")
                    elif num == "1":
                        print((number[0]-1) * "." + "#", end=" ")
                    elif num == "4":
                        print("#" + (number[0]-2) * "." + "#", end=" ")
                    elif num == "6":
                        print("#" + (number[0]-1) * ".", end=" ")
                elif mh < h + number[0] - 1:
                    if num in ["1","2","3", "7"]:
                        print((number[0] - 1) * "." + "#", end=" ")
                    elif num in ["4", "8", "9", "0"]:
                        print("#" + (number[0] - 2) * "." + "#", end=" ")
                    else:
                        print("#" + (number[0] - 1) * ".", end=" ")
                elif mh == h + number[0] - 1:
                    if num in ["1", "7"]:
                        print((number[0] - 1) * "." + "#", end=" ")
                    elif num == "0":
                        print("#" + (number[0] - 2) * "." + "#", end=" ")
                    else:
                        print(number[0] * "#", end=" ")
                elif mh < h + 2*number[0] - 2:
                    if num in ["1", "3", "4", "5", "7", "9"]:
                        print((number[0] - 1) * "." + "#", end=" ")
                    elif num in ["8", "0", "6"]:
                        print("#" + (number[0] - 2) * "." + "#", end=" ")
                    else:
                        print("#" + (number[0] - 1) * ".", end=" ")
                elif mh == h + 2*number[0] - 2:
                    if num in ["2", "3", "5", "6", "8", "0"]:
                        print(number[0] * "#", end=" ")
                    else:
                        print((number[0]-1) * "." + "#", end=" ")
                else:
                    print(number[0] * ".", end=" ")

        print()
