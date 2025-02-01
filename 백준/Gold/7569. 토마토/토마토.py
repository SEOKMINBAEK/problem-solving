import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
mtx = [[[-1 for _ in range(m)] for _ in range(n)] for _ in range(h)]
queue = []

def valid_all_aged():
  for i in range(h):
    for j in range(n):
      for k in range(m):
        if mtx[i][j][k] == 0:
          return False
  
  return True

for i in range(h):
  for j in range(n):
    for k, char in enumerate(map(int, input().split())):
      if char == 1:
        queue.append((i, j, k, 0))
      
      mtx[i][j][k] = char

if valid_all_aged():
  print(0)
  exit()

max_date = 0

for cur in queue:
  floor, row, idx, date = cur
  
  max_date = max(max_date, date)
  
  # 아래층에 익지 않은 토마토가 존재할 때
  if floor > 0 and mtx[floor - 1][row][idx] == 0:
    mtx[floor - 1][row][idx] = date + 1
    queue.append((floor - 1, row, idx, date + 1))
  
  # 윗층에 익지 않은 토마토가 존재할 때
  if floor < h - 1 and mtx[floor + 1][row][idx] == 0:
    mtx[floor + 1][row][idx] = date + 1
    queue.append((floor + 1, row, idx, date + 1))
  
  # 아래칸에 익지 않은 토마토가 존재할 때
  if row > 0 and mtx[floor][row - 1][idx] == 0:
    mtx[floor][row - 1][idx] = date + 1
    queue.append((floor, row - 1, idx, date + 1))
  
  # 윗칸에 익지 않은 토마토가 존재할 때
  if row < n - 1 and mtx[floor][row + 1][idx] == 0:
    mtx[floor][row + 1][idx] = date + 1
    queue.append((floor, row + 1, idx, date + 1))
  
  # 왼쪽칸에 익지 않은 토마토가 존재할 때
  if idx > 0 and mtx[floor][row][idx - 1] == 0:
    mtx[floor][row][idx - 1] = date + 1
    queue.append((floor, row, idx - 1, date + 1))
  
  # 오른쪽칸에 익지 않은 토마토가 존재할 때
  if idx < m - 1 and mtx[floor][row][idx + 1] == 0:
    mtx[floor][row][idx + 1] = date + 1
    queue.append((floor, row, idx + 1, date + 1))

if valid_all_aged():
  print(max_date)
else:
  print(-1)
