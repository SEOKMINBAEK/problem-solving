import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
  x = int(input())
  
  if x:
    heapq.heappush(arr, (abs(x), x))
  else:
    if len(arr):
      print(heapq.heappop(arr)[1])
    else:
      print(0)