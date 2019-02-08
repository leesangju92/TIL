clues = ( 2, 2, 1, 3,  
  2, 2, 3, 1,  
  1, 2, 2, 3,  
  3, 2, 1, 3 )


def solve_puzzle (clues):
    answer=[
        [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]],
        [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]],
        [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]],
        [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]],
        ]
    i = 0
    for clue in clues:
        if i < 4:
            if clue == 1:
                answer[0][i] = 4
        elif i < 8:
            if clue == 1:
                answer[i-4][3] = 4
        elif i < 12:
            if clue == 1:
                answer[3][11-i] = 4
        else:
            if clue == 1:
                answer[15-i][0] = 4
        i += 1

    for num_set in answer:
        a = 0
        for num_list in num_set:
            if num_list != 4:
                a += 1
            else:
                for num_list1 in num_set:
                    if type(num_list1) == type([]) and 4 in num_list1:
                        num_list1.remove(4)
                for n in range(3):
                    if type(answer[n][a]) == type([]) and 4 in answer[n][a]:
                        answer[n][a].remove(4)
                            





    #      if type(num_list) == type([]):
    #             num_list.remove(4)

    # exist_check = []
    # for line in answer:
    #     if 4 in line:
    #         exist_check.append(line.index(4))

    # last = set([0,1,2,3]) - set(exist_check)
    # last1 = list(last)       
    # for line in answer:
    #     if 4 not in line:
    #         line[last1[0]] = 4


    # i = 0
    # for clue in clues:
    #     if i < 4:
    #         if clue == 2 and answer[3][i] == 4:
    #             answer[0][i] = 3
    #     elif i < 8:
    #         if clue == 2 and answer[i-4][0] == 4 : 
    #             answer[i-4][3] = 3
    #     elif i < 12:
    #         if clue == 2 and answer[0][11-i] == 4 :
    #             answer[3][11-i] = 3
    #     else:
    #         if clue == 2 and answer[15-i][3] == 4:
    #             answer[15-i][0] = 3
    #     i += 1


    
    return answer

print(solve_puzzle(clues))



# outcomes = (
# ( ( 1, 3, 4, 2 ),       
#   ( 4, 2, 1, 3 ),       
#   ( 3, 4, 2, 1 ),
#   ( 2, 1, 3, 4 ) ),
# ( ( 2, 1, 4, 3 ), 
#   ( 3, 4, 1, 2 ), 
#   ( 4, 2, 3, 1 ), 
#   ( 1, 3, 2, 4 ) )
# )
