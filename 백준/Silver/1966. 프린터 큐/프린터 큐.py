import sys
input = sys.stdin.readline

case = int(input())

for _ in range(case):
  n, m = map(int, input().split())
  q = list(map(lambda v: [int(v), False], input().split()))
  cnt = 0
  
  q[m][1] = True
  
  while q:
    maxi = max(q, key=lambda v: v[0])
    cur = q.pop(0)
    
    if cur[0] < maxi[0]:
      q.append(cur)
    else:
      cnt += 1
      if cur[1]:
        break
  
  print(cnt)