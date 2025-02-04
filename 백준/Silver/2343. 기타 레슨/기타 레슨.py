import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times = list(map(int, input().split()))

l = 0
maxi = max(times)
r = sum(times)

while l <= r:
  mid = (l + r) // 2
  
  temp = 0
  arr = []
  cnt = 0
  
  for i, time in enumerate(times):
    temp += time
    
    if i == N - 1:
      if temp > mid:
        temp = time
        cnt += 2
      else:
        cnt += 1
    else:
      if temp == mid:
        temp = 0
        cnt += 1
      elif temp > mid:
        temp = time
        cnt += 1
  
  if cnt > M: # 현재 크기로 만든 블루레이 갯수가 M개를 넘으면
    l = mid + 1
  else: # 현재 크기로 만든 블루레이 갯수가 M개를 넘지 않으면
    r = mid - 1

print(l if l > maxi else maxi)