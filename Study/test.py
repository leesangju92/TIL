for t in range(2):
   test_case = int(input())
   data = []
   Max, j = 0, 1

   for i in range(100):
       data.append(input())

   for m in range(100):
       while j <= 100:
           for i in range(100-j+1):
               text = data[m][i:i+j]
               if text[::-1] == text:
                   print(text, text[::-1])
                   if Max < len(text):
                       print(len(text))
                       Max = len(text)
           j += 1
       print(f'#{t+1} {Max}')