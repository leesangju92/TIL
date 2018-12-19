import requests

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)

lotto_data = response.json()

common_words = 'drwtNo'

real_numbers = []   #이거 꼭 필요하다. (.append를 사용하려면)

# for key in lotto_data:
#     if common_words in key:   # 또는 if 'drwtNo' in key:
#         real_numbers.append(lotto_data[key])

for key,value in lotto_data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)


real_numbers.sort()
bonus_number = lotto_data['bnusNo']
print(real_numbers)

#lotto_data = requests.get(url, verify=False).json()

# real_numbers = [
#     lotto_data['drwtNo1'],
#     lotto_data['drwtNo2'],
#     lotto_data['drwtNo3'],
#     lotto_data['drwtNo4'],
#     lotto_data['drwtNo5'],
#     lotto_data['drwtNo6'],
# ] 모두 주석 처리는 Ctrl + /