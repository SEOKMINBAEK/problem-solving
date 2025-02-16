import sys, heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  k = int(input())
  min_heap = []
  max_heap = []
  removed = set()
  insert_cnt = 0
  
  for i in range(k):
    cmd, n = input().rstrip().split()
    n = int(n)
    
    if cmd == 'I':
      insert_cnt += 1
      heapq.heappush(min_heap, (n, i))
      heapq.heappush(max_heap, (-n, i))
    else:
      if len(removed) == insert_cnt:
        continue
      
      while True:
        _, idx = heapq.heappop(max_heap if n == 1 else min_heap)
        
        if idx not in removed:
          removed.add(idx)
          break
  
  if len(removed) == insert_cnt:
    print('EMPTY')
  else:
    while True:
      max_val, idx = heapq.heappop(max_heap)
      if idx not in removed:
        break
    
    while True:
      min_val, idx = heapq.heappop(min_heap)
      if idx not in removed:
        break
    
    print(f"{-max_val} {min_val}")