import sys
sys.stdin = open("input.txt", "r")  #해당 파일로부터 input 받음
# sys.stdout = open("output.txt", "w") #해당 파일로 출력하여 저장


for case in range(10):
    result = 0
    locations = int(input())
    height_list = list(map(int, input().split()))
    for location in range(2, locations - 2):
        left = 0
        right = 0
        if height_list[location] > height_list[location - 2] and height_list[location] > height_list[location-1]:
            if height_list[location - 1] > height_list[location - 2]:
                left = height_list[location] - height_list[location - 1]
            else:
                left = height_list[location] - height_list[location - 2]
        if height_list[location] > height_list[location + 2] and height_list[location] > height_list[location+1]:
            if height_list[location + 1] > height_list[location + 2]:
                right = height_list[location] - height_list[location + 1]
            else:
                right = height_list[location] - height_list[location + 2]
        if left > 0 and right > 0:
            if left > right:
                result += right
            else:
                result += left
    print(f"#{case+1} {result}")