print("There are %d bananas" % 15)
print("I like %s" % "apple")
print("my name is {}".format("sangju"))
print("{:<10}".format("left"))
print("{:>10}".format("right"))
print("{:^10}".format("middle"))
print("{:=^20}".format("fill"))
print("{:10.3f}".format(1234.56789))
print("{{ why }}".format("string"))

# python >= 3.6
age = 27
print(f"내년 나이는 {age+1}살")

# 내장함수 => method, 문자열 뒤에 "." 붙이고 함수이름
print('Coffee Icecream'.count("c"))
print('Coffee Icecream'.find("c"), "hy".find("z"))

# 문자열, 리스트에 특정 문자 삽입
print("1".join("abcd"), "2".join(["a", "b", "c", "d"]))

# 대문자, 소문자 변환
print("hi".upper(), "HI".lower())

# 공백 제거
print("   hi   ".lstrip(), "   hi   ".rstrip(), "   hi   ".strip())

# 문자열 바꾸기
print("banana is great".replace("banana", "apple"))

# 문자열 나누기
print("banana apple grape melon".split())