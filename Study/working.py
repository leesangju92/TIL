import sys
sys.stdin = open("working.txt", "r")

for test_case in range(1, 11):
    
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    work_map = [[] for _ in range(V+1)]
    before_work = [ 0 for _ in range(V+1)]
    starts = [ i for i in range(1, V+1)]
    for i in range(E):
        work_map[arr[2*i]] += [arr[2*i+1]]
        before_work[arr[2*i+1]] += 1
        starts = list(set(starts) - set([arr[2*i+1]]))

    visited = []
    course = []
    while len(visited) < V:
        for start in starts:
            if start not in visited:
                visited += [start]
                course += [start]
                next_work = start
                while len(course) > 0:
                    for work in work_map[next_work]:
                        if before_work[work] == 1 and work not in visited:
                            visited += [work]
                            course += [work]
                            next_work = work
                            break
                        elif before_work[work] > 1:
                            before_work[work] -= 1
                            work_map[next_work] = list(set(work_map[next_work]) - set([work]))
                        elif work in visited:
                            continue
                    if len(work_map[next_work]) == 0:
                        course.pop(-1)
                        if len(course) > 0:
                            next_work = course[-1]   
                    elif work_map[next_work][-1] in visited:
                        course.pop(-1)
                        if len(course) > 0:
                            next_work = course[-1]  
            else:
                continue
    print(f"#{test_case}", end=" ")
    for number in visited:
        if number == visited[-1]:
            print(number)
        else:
            print(number, end=" ")

