import sys
sys.stdin = open("LINE.txt", "r")


a, b = map(int, input().strip().split(' '))
queue_list = [ 0 for _ in range(b)]
message_list = [ int(input()) for _ in range(a)]

t = 0
while len(message_list) or sum(queue_list):
    t += 1
    for idx in range(len(queue_list)):
        if queue_list[idx] == 0:
            if len(message_list):
                m = message_list.pop(0)
                if m > 0:
                    queue_list[idx] = m - 1
                else:
                    check = False
                    while len(message_list) and not check:
                        new_m = message_list.pop(0)
                        if new_m > 0:
                            check = True
                            queue_list[idx] = new_m - 1

        else:
            queue_list[idx] -= 1
    print(queue_list)
print(t)