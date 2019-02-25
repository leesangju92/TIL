import sys
sys.stdin = open("1247.txt", "r")



def distance(locations, route, N):
    distance_btw = 0
    for n in range(N-1):
        distance_btw += (abs(locations[route[n]][0] - locations[route[n+1]][0]) + abs(locations[route[n]][1] - locations[route[n+1]][1]))
    distance_btw += abs(locations[0][0] - locations[route[0]][0]) + abs(locations[0][1] - locations[route[0]][1] )
    distance_btw += abs(locations[1][0] - locations[route[-1]][0] ) + abs(locations[1][1] - locations[route[-1]][1] )
    return distance_btw

def start(company):
    visited = []
    course = []
    for next in route[company]:
        course += [next]
        next_customer = next
        for customer in route[next_customer]:
            if customer in course:
                continue
            else:
                course += [customer]
                next_customer = customer
                break
        if len(course) == 5:
            visited += [course]
        print(course)
        print(visited)
        if course in visited:
            course.pop(-1)
    return visited



T = int(input())
for test_case in range(1):
    N = int(input())
    locations = [0]*(N+2)
    arr = list(map(int, input().split()))
    for n in range(N+2):
        locations[n] = [arr[2*n], arr[2*n+1]]
    

    route = [list(range(2,N+2))] + [0] + [ list(set(list(range(2, N+2))) - set([i]) ) for i in range(2, N+2) ]
    visited = []
    courses = []
    print(start(0))
    
    # print(route)

    

    # customers = list(range(2,N+2))
    # routes = []
    # for customer in customers:
    #     routes += [[customer]]
    # for i in range(N-1):
    #     new_routes = []
    #     for route in routes:
    #         new_route = []
    #         new_customers = list(set(customers)-set(route))
    #         print(new_customers)
    #         for customer in new_customers:
    #             new_route += [route + [customer]]  
    #         new_routes += new_route
    #     routes = new_routes


    # min_distance = distance(locations ,routes[0], N)
    # for route in routes:
    #     if distance(locations ,route, N) < min_distance:
    #         min_distance = distance(locations ,route, N)
    # print(f"#{test_case} {min_distance}")

    
    #12345를 5!의 경우의 수를 뽑는 방법.
