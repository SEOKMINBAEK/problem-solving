t = int(input())

for _ in range(t):
  n = int(input())
  dic = {}
  
  for _ in range(n):
    v, k = input().split()
    
    if k in dic:
      dic[k] += 1
    else:
      dic[k] = 2
  
  cnt = 1
  
  for k in dic:
    cnt *= dic[k]
  
  print(cnt - 1)