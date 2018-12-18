numbers = [1,2,3] #변수 이름은 뜻을 담아서 짓자
family = ['mom',1.64,'dad',1.74,'sister',1.56, True]
mcu = [
['ironman','captain america'],
['deadpool', 'xman'],
['spiderman']
]

family[-1]
family[-3:-1]
family[-3:]
family[:-1]
mcu[0][1]


print(mcu)

#문제 : 리스트 안에 내용들은 쉼표로 구분되어야 한다. 띄어쓰기로는 에러가 발생
numbers = list(range(1,46))
numbers = list(range(100))
numbers[2:5] #[start:end] start는 포함하며 end는 포함하지 않음 0,1,2(3번째)부터 5번째수

x = ['life', 'is', 'short', True, 123, ['you', 'need', 'python']]
my_bool = x[3]
my_bool = x[3:4]
my_bool = x[-3]
