import sys
sys.stdin = open("1240.txt", "r")

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    if N <= 5 or M <= 56:
        print(f"#{t} 0")
        continue
    password_codes = []
    for n in range(N):
        password_codes += [input()]
    for code in password_codes:
        if int(code) != 0:
            password_code = str(int(code))
            swap_count = 0
            previous = password_code[0]
            first_code_length = 0
            for i in password_code:
                if i != previous:
                    swap_count += 1
                    previous = i
                if swap_count == 3:
                    break
                first_code_length += 1
            if first_code_length < 8:
                password_code = "0"*(7-first_code_length) + password_code
            final_code = []
            for n in range(8):
                transfer = password_code[7*n:7*n+7]
                if transfer == "0001101":
                    final_code += [0]
                elif transfer == "0011001":
                    final_code += [1]
                elif transfer == "0010011":
                    final_code += [2]
                elif transfer == "0111101":
                    final_code += [3]
                elif transfer == "0100011":
                    final_code += [4]
                elif transfer == "0110001":
                    final_code += [5]
                elif transfer == "0101111":
                    final_code += [6]
                elif transfer == "0111011":
                    final_code += [7]
                elif transfer == "0110111":
                    final_code += [8]
                else:
                    final_code += [9]
            answer = (final_code[0]+final_code[2]+final_code[4]+final_code[6])*3 + final_code[1]+final_code[3]+ final_code[5] + final_code[7]
            if answer % 10 == 0:
                print(f"#{t}",sum(final_code))
                break
            else:
                print(f"#{t}",0)
                break