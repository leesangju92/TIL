import sys
sys.stdin = open("1247.txt", "r")



def distance(locations, route, N):
    distance_btw = 0
    for n in range(N-1):
        distance_btw += (abs(locations[route[n]][0] - locations[route[n+1]][0]) + abs(locations[route[n]][1] - locations[route[n+1]][1]))
    distance_btw += abs(locations[0][0] - locations[route[0]][0]) + abs(locations[0][1] - locations[route[0]][1] ) + abs(locations[1][0] - locations[route[-1]][0] ) + abs(locations[1][1] - locations[route[-1]][1] )
    return distance_btw



def permutation(customers, N, k=0):
    global routes
    if k == N:
        result = case[:]
        routes.append(result)
    else:
        for i in customers:
            case[k] = i
            permutation(list(set(customers)-set([i])), N, k+1)

                
T = int(input())
for test_case in range(1,11):
    N = int(input())
    locations = [0]*(N+2)
    arr = list(map(int, input().split()))
    for n in range(N+2):
        locations[n] = [arr[2*n], arr[2*n+1]]
    customers = [ i for i in range(2, N+2)]
    routes = []
    case = [0]*N
    permutation(customers, N)
    min_distance = distance(locations ,routes[0], N)
    for route in routes:
        if distance(locations ,route, N) < min_distance:
            min_distance = distance(locations ,route, N)
    print(f"#{test_case} {min_distance}")



    


    # for customer in customers:
    #     routes += [[customer]]
    # for i in range(N-1):
    #     new_routes = []
    #     for route in routes:
    #         new_route = []
    #         new_customers = list(set(customers)-set(route))
    #         # print(new_customers)
    #         for customer in new_customers:
    #             new_route += [route + [customer]]  
    #         new_routes += new_route
    #     routes = new_routes   



    
    #12345를 5!의 경우의 수를 뽑는 방법.
