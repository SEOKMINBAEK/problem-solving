import math

n = int(input())

def four_squares(n):
  # 1. 1개의 제곱수로 표현 가능한 경우
  if int(math.sqrt(n)) ** 2 == n:
    return 1
  
  # 2. 2개의 제곱수로 표현 가능한 경우
  for i in range(1, int(math.sqrt(n)) + 1):
    if int(math.sqrt(n - (i ** 2))) ** 2 == n - (i ** 2):
      return 2
  
  # 3. 3개의 제곱수로 표현 가능한 경우
  for i in range(1, int(math.sqrt(n)) + 1):
    for j in range(1, int(math.sqrt(n - (i ** 2))) + 1):
      if int(math.sqrt(n - (i ** 2) - (j ** 2))) ** 2 == n - (i ** 2) - (j ** 2):
        return 3
  
  # 4. 나머지 경우는 4개의 제곱수로 표현 가능한 경우
  return 4

print(four_squares(n))