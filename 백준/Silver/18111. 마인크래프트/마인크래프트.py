import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
mtx = []

for _ in range(N):
  mtx.append(list(map(int, input().split())))

mini = (float('inf'), 0)

for i in range(0, 257):
  time = 0
  available = B
  
  for row in mtx:
    for block in row:
      if block > i:
        time += (block - i) * 2
        available += (block - i)
      else:
        time += (i - block)
        available -= (i - block)
  
  if available < 0:
    break
  
  if mini[0] > time or (mini[0] == time and mini[1] < i):
    mini = (time, i)

print(mini[0], mini[1])