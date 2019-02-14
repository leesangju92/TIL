def build_data(data):
    move_distance_dict = {x: [0, 0] for x in range(len(data))}
    for location in range(len(data)):
        for floor in range(data[location]):
            if move_distance_dict[floor][0] == 0:
                move_distance_dict[floor][1] = location
            move_distance_dict[floor][0] += 1
    for key in move_distance_dict:
        if move_distance_dict[key][0] == 0:
            return 9 - (move_distance_dict[key - 1][1]) - move_distance_dict[key - 1][0]

data = [7, 4, 2, 0, 0, 6, 0, 7, 0]

print(build_data(data))

arr = [7, 4, 2, 0, 0, 6, 0, 7, 0]
maxH = 0
for i in range(len(arr)):
    height = len(arr)
    cnt = 0
    for j in range(i+1, len(arr)):
        if arr[i] <= arr[j]:
            cnt += 1
    height -= cnt
    maxH = max(height, maxH)
print(maxH)