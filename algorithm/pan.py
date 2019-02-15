import sys
sys.stdin = open("sample_input.txt", "r")

def moving_left(crd):
    if crd[0] == 0:
        return None
    else:
        return [crd[0]-1 , crd[1]]

def moving_right(crd):
    if crd[0] == 3:
        return None
    else:
        return [crd[0]+1 , crd[1]]

def moving_up(crd):
    if crd[1] == 0:
        return None
    else:
        return [crd[0] , crd[1]-1]

def moving_down(crd):
    if crd[1] == 3:
        return None
    else:
        return [crd[0]-1 , crd[1]+1]


location_list = []
for x in range(4):
    for y in range(4):
        location_list += [[x,y]]
print(location_list)

T = int(input())
for t in range(T):
    square = [[], [], [], []]
    for i in range(4):
        square[i] = list(map(int, input().split()))
    print(square)
    seven_dict = {}
    for location in location_list:
        result = str(square[location[0]][location[1]])
        #뒤에 숫자 6개 붙이기
        for i in range(6):





        # for I in range(7):\
        print(result)




    # for start in start_list:


print(f"#{t} {len(seven_dict)}")