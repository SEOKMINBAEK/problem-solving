import sys
input = sys.stdin.readline

m, n = map(int, input().split())
mtx = [[-1 for _ in range(m)] for _ in range(n)]
queue = []

def valid_all_aged():
  for i in range(n):
    for j in range(m):
      if mtx[i][j] == 0:
        return False
  
  return True

for i in range(n):
  for j, char in enumerate(map(int, input().split())):
    if char == 1:
      queue.append((i, j, 0))
    
    mtx[i][j] = char

if valid_all_aged():
  print(0)
  exit()

max_date = 0

for cur in queue:
  row, idx, date = cur
  
  max_date = max(max_date, date)
  
  # 아래칸에 익지 않은 토마토가 존재할 때
  if row > 0 and mtx[row - 1][idx] == 0:
    mtx[row - 1][idx] = date + 1
    queue.append((row - 1, idx, date + 1))
  
  # 윗칸에 익지 않은 토마토가 존재할 때
  if row < n - 1 and mtx[row + 1][idx] == 0:
    mtx[row + 1][idx] = date + 1
    queue.append((row + 1, idx, date + 1))
  
  # 왼쪽칸에 익지 않은 토마토가 존재할 때
  if idx > 0 and mtx[row][idx - 1] == 0:
    mtx[row][idx - 1] = date + 1
    queue.append((row, idx - 1, date + 1))
  
  # 오른쪽칸에 익지 않은 토마토가 존재할 때
  if idx < m - 1 and mtx[row][idx + 1] == 0:
    mtx[row][idx + 1] = date + 1
    queue.append((row, idx + 1, date + 1))

if valid_all_aged():
  print(max_date)
else:
  print(-1)