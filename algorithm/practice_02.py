def babygin(numbers):
    num_list = [int(number) for number in str(numbers)]
    ordered_dict = { x : 0 for x in range(10)}
    count1 = 0
    print(count1)
    for num in num_list:
        ordered_dict[num] += 1
    print(count1)
    for key in ordered_dict:
        if ordered_dict[key] == 6:
            count1 = 2
            ordered_dict[key] = 0
        if ordered_dict[key] >= 3:
            ordered_dict[key] -= 3
            count1 += 1
        if ordered_dict[key] >= 2:
            if ordered_dict[key+2]:
                if ordered_dict[key+1] >= 1 and ordered_dict[key+2] >= 1:
                    ordered_dict[key] -= 1
                    ordered_dict[key+1] -= 1
                    ordered_dict[key+2] -= 1
                    count1 += 1
        if ordered_dict[key] >= 1:
            if ordered_dict[key + 2]:
                if ordered_dict[key + 1] >= 1 and ordered_dict[key + 2] >= 1:
                    ordered_dict[key] -= 1
                    ordered_dict[key + 1] -= 1
                    ordered_dict[key + 2] -= 1
                    count1 += 1
        print(ordered_dict, count1)
    if count1 == 2:
        return True
    else:
        return False

numbers = 123123

print(babygin(numbers))

# for num in num_list[1:]:
#     if num < ordered_list[0]:
#         ordered_list = [num] + ordered_list
#     elif num >= ordered_list[-1]:
#         ordered_list = ordered_list + [num]
#     else:
#         i = 0
#         for number in ordered_list:
#             if num >= number and ordered_list[i] != ordered_list[i + 1]:
#                 ordered_list = ordered_list[0:i + 1] + [num] + ordered_list[i + 1:]
#             i += 1
#     # print(ordered_list)