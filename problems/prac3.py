def solve_puzzle (clues):

# 초기 outcome 생성

    outcome = [
        [list(range(1,5)), list(range(1,5)), list(range(1,5)), list(range(1,5))],
        [list(range(1,5)), list(range(1,5)), list(range(1,5)), list(range(1,5))],
        [list(range(1,5)), list(range(1,5)), list(range(1,5)), list(range(1,5))],
        [list(range(1,5)), list(range(1,5)), list(range(1,5)), list(range(1,5))]
        ]

    number_index = 0
    for clue in clues:
        if number_index < 4:
            if type(candidate_1st(clue)) == type(2):
                outcome[0][number_index] = candidate_1st(clue)
            elif len(outcome[0][number_index]) >= len(candidate_1st(clue)):
                outcome[0][number_index] = candidate_1st(clue)
        elif number_index < 8:
            if type(candidate_1st(clue)) == type(2):
                outcome[number_index-4][3] = candidate_1st(clue)
            elif len(outcome[number_index-4][3]) >= len(candidate_1st(clue)):
                outcome[number_index-4][3] = candidate_1st(clue)

        elif number_index < 12:
            if type(candidate_1st(clue)) == type(2):
                outcome[3][11-number_index] = candidate_1st(clue)
            elif len(outcome[3][11-number_index]) >= len(candidate_1st(clue)):
                outcome[3][11-number_index] = candidate_1st(clue)
        else:
            if type(candidate_1st(clue)) == type(2):
                outcome[15-number_index][0] = candidate_1st(clue)
            elif len(outcome[15-number_index][0]) >= len(candidate_1st(clue)):
                outcome[15-number_index][0] = candidate_1st(clue)
        number_index += 1

    candidate_remove(outcome)

# 1차 정리, 4를 위치시킴

    candidate_refine(outcome, 4)  

    candidate_refine(outcome, 4)

# 2차 정리, 3을 위치시킴        

    candidate_2nd(clues, outcome)

    candidate_refine(outcome, 3)

    candidate_ChooseFinal(outcome)

# 3차 정리, 1 또는 2를 위치시킴

    candidate_3rd(clues, outcome)

    candidate_ChooseFinal(outcome)

    candidate_ChooseFinal(outcome)

    candidate_ChooseFinal(outcome)

    candidate_ChooseFinal(outcome)

    return (tuple(outcome[0]), tuple(outcome[1]), tuple(outcome[2]), tuple(outcome[3]))   


def candidate_1st(clue):
    if clue == 4:
        return 1
    elif clue == 3:
        return [1,2]
    elif clue == 2:
        return [1,2,3]
    elif clue == 1:
        return 4
    else:
        return [1,2,3,4]


def candidate_remove(result):
    for line in result:
        order = 0
        for number in line:
            if type(number) == type(4):
                for number_list in line:
                    if type(number_list) == type([]) and number in number_list:
                        number_list.remove(number)
                for n in range(4):
                    if type(result[n][order]) == type([]) and number in result[n][order]:
                        result[n][order].remove(number)
            order += 1


def candidate_refine(outcome, target_number):
    for line in outcome:
        len_check = 0
        target = 0
        for num_list in line:
            if type(num_list) == type([]) and target_number in num_list:
                len_check += 1
                target = line.index(num_list)
        if len_check == 1:
            line[target] = target_number

    candidate_remove(outcome)
        

def candidate_2nd(clues, outcome):
    number_index = 0
    for clue in clues:
        if number_index < 4:
            if clue == 2 and outcome[2][number_index] == 4 and 1 in outcome[0][number_index]:
                outcome[0][number_index].remove(1) 
            elif clue == 2 and outcome[3][number_index] == 4:
                outcome[0][number_index] = 3
        elif number_index < 8:
            if clue == 2 and outcome[number_index-4][1] == 4 and 1 in outcome[number_index-4][3]:
                outcome[number_index-4][3].remove(1) 
            elif clue == 2 and outcome[number_index-4][0] == 4:
                outcome[number_index-4][3] = 3
        elif number_index < 12:
            if clue == 2 and outcome[1][11-number_index] == 4 and 1 in outcome[3][11-number_index]:
                outcome[3][11-number_index].remove(1) 
            elif clue == 2 and outcome[0][11-number_index] == 4:
                outcome[3][11-number_index] = 3
        else:
            if clue == 2 and outcome[15-number_index][2] == 4 and 1 in outcome[15-number_index][0]:
                outcome[15-number_index][0].remove(1) 
            elif clue == 2 and outcome[15-number_index][3] == 4:
                outcome[15-number_index][0] = 3
        number_index += 1
    candidate_remove(outcome)

def candidate_ChooseFinal(outcome):
    for line in outcome:
        i = 0
        for num_list in line:
            if type(num_list) == type([]) and len(num_list) == 1:
                line[i] = num_list[0]
            i += 1
    candidate_remove(outcome)

def candidate_3rd(clues, outcome):
    clue_index = 0
    for clue in clues:
        if clue_index < 4:
            if clue == 2 and outcome[2][clue_index] == 4 and outcome[0][clue_index] == 2:
                outcome[1][clue_index] = 1
            elif clue == 3 and outcome[2][clue_index] == 3 and outcome[3][clue_index] == 4:
                outcome[0][clue_index] = 2
        elif clue_index < 8:
            if clue == 2 and outcome[clue_index-4][1] == 4 and outcome[clue_index-4][3] == 2:
                outcome[clue_index-4][2] = 1
            elif clue == 3 and outcome[clue_index-4][0] == 4 and outcome[clue_index-4][1] == 3:
                outcome[clue_index][3] = 2
        elif clue_index < 12:
            if clue == 2 and outcome[1][11-clue_index] == 4 and outcome[3][11-clue_index] == 2:
                outcome[2][11-clue_index] = 1
            elif clue == 3 and outcome[0][11-clue_index] == 4 and outcome[1][11-clue_index] == 3:
                outcome[3][11-clue_index] = 2
        else:
            if clue == 2 and outcome[15-clue_index][2] == 4 and outcome[15-clue_index][0] == 2:
                outcome[15-clue_index][1] = 1
            elif clue == 3 and outcome[15-clue_index][3] == 4 and outcome[15-clue_index][2] == 3:
                outcome[15-clue_index][0] = 2
        clue_index += 1
    candidate_remove(outcome)




clues = (
( 2, 2, 1, 3,  
  2, 2, 3, 1,  
  1, 2, 2, 3,  
  3, 2, 1, 3 ),
( 0, 0, 1, 2,   
  0, 2, 0, 0,   
  0, 3, 0, 0, 
  0, 1, 0, 0 )
)

print(solve_puzzle(clues[1]))


# ( 2, 2, 1, 3,  
#   2, 2, 3, 1,  
#   1, 2, 2, 3,  
#   3, 2, 1, 3 )




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

# test.describe ("4 by 4 skyscrapers")
# test.it ("should pass all the tests provided")

# test.assert_equals (solve_puzzle (clues[0]), outcomes[0])
# test.assert_equals (solve_puzzle (clues[1]), outcomes[1])
