import math
T = int(input())

for _ in range(T):
  M, N, x, y = map(int, input().split())
  result = -1
  
  for i in range(x, math.lcm(M, N) + 1, M): # M과 N의 최소공배수가 마지막해
    if (i % M or M) == x and (i % N or N) == y:
      result = i
      break
  
  print(result)