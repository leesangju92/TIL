import sys
sys.stdin = open("1245.txt", "r")


def finding_force(m, location):
    left_force, right_force = 0, 0
    for i in range(m+1):
        left_force += magnetic_list[1][i]/(location-magnetic_list[0][i])**2
    for i in range(M-1, m, -1):
        right_force += magnetic_list[1][i]/(location-magnetic_list[0][i])**2
    return left_force, right_force


T = int(input())
for test_case in range(1, T+1):
    M = int(input())
    arr = list(map(int, input().split()))
    magnetic_list = [0]*2
    for i in range(2):
        magnetic_list[i] = arr[M*i:M+M*i]
    print(f"#{test_case}", end=" ")
    for m in range(M-1):
        min_distance = magnetic_list[0][m]
        max_distance = magnetic_list[0][m+1]
        location = (min_distance + max_distance) / 2
        left_force, right_force = finding_force(m, location)
        while round(min_distance, 12) != round(max_distance, 12):
            if left_force > right_force:
                min_distance = location
                location = (min_distance + max_distance) / 2
            elif left_force < right_force:
                max_distance = location
                location = (min_distance + max_distance) / 2
            elif round(left_force, 13) == round(right_force, 13):
                break
            left_force, right_force = finding_force(m, location)
        print("%.10f" %location, end=" ")
    print()