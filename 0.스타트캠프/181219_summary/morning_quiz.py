import operator

# 1. 평균을 구하기
my_score = [79,84,66,93]

sum_one = 0

for score in my_score:
    sum_one += score 

my_average = sum_one / len(my_score)

print(my_average)
#float

your_score = {
    "수학" : 87,
    "국어" : 83,
    "영어" : 76,
    "도덕" : 100
}
#float
[{ "수학": 87 }, {"국어": 83 }]
sum_two = 0

# for subject in your_score:
#      sum_two += your_score[subject]

#your_score.items()와 your_score.values()로 나오는것은 형태만 리스트이며 순서로 꺼낼 순 없다
#합계를 구하는 함수 : sum() 딕셔너리-리스트 형태변환 메소드 : xxx.items() , xxx.values() 

# 참고 : your_score_average = sum(your_score.values())/len(your_score)

for key,value in your_score.items():
    sum_two += value

your_score_average = sum_two / len(your_score)

print(your_score_average)

import operator

cities_temp = {
    '서울' : [-6, -10, 5],
    '대전' : [-3, -5, 2],
    '광주' : [0, -5, 10],
    '구미' : [2, -2, 9]
}


# for city in cities_temp:   한손으로 key만 꺼내요
#     temperatures = cities_temp[city]
#     avg_temperature = round(sum(cities_temp[city])/len(temperatures),2)
#     print(city, avg_temperature)
#     print(city + ':' + str(avg_temperature))
#     print('{0} : {1}', format(city, avg_temperature))


for city in cities_temp:
    temp_sum = sum(cities_temp[city])
    print(city, ':' ,round(temp_sum/len(cities_temp[city]),2))

temp_hot = {}
temp_cold = {}
temp_hot_list =[]
temp_cold_list = []


for city, temp in cities_temp.items():
    temp_hot[city] = max(temp)

print(temp_hot)

for city, temp in cities_temp.items():
    temp_cold[city] = min(temp)

print(temp_cold)


for key,value in cities_temp.items():    #양손으로 key,value 둘다 꺼내요
    temp_order_hot = max(value)
    temp_hot_list.append(temp_order_hot)

temp_hot_list.sort(reverse=True)

hottest_temp = temp_hot_list[0]


for key,value in cities_temp.items():
    temp_order_cold = min(value)
    temp_cold_list.append(temp_order_cold)

temp_cold_list.sort()

coldest_temp = temp_cold_list[0]

for city, temp in temp_hot.items():
    if temp == hottest_temp:
        print('가장 더웠던 도시는 :',city)

for city, temp in temp_cold.items():
    if temp == coldest_temp:
        print('가장 추웠던 도시는 :',city)


#all_temp에 모든 기온을 모은다
all_temp = []
for city, value in cities_temp.items():
    all_temp += value
#all_temp에서 highest/lowest를 찾는다
highest = max(all_temp)
lowest = min(all_temp)
print(highest, lowest)
#cities_temp에서 highest/lowest가 속한 도시를 찾는다
hottest = []
coldest = []
for key, value in cities_temp.items():
    if highest in value:
        hottest.append(key)
    if lowest in value:
        coldest.append(key)

# hottest = ''
# coldest = ''
# for key, value in cities_temp.items():
#     if highest in value:
#         hottest = key
#     if lowest in value:
#         coldest = key