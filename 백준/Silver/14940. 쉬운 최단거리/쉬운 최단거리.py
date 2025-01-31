# 백준 14940

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mtx = [[] for _ in range(n)]
answer = [[-1 for _ in range(m)] for _ in range(n)]
queue = []

for i in range(n):
  for j, c in enumerate(input().rstrip().split()):
    if c == '2':
      queue.append((i, j, 0)) # 목적지부터 BFS 탐색
      answer[i][j] = 0 # 목적지는 0으로 고정
    
    if c == '0':
      answer[i][j] = 0 # 벽은 0으로 고정
    
    mtx[i].append(int(c))

for cur in queue:
  i, j, distance = cur
  
  # 위로 갈 수 있는 경우
  if i > 0:
    if answer[i - 1][j] == -1 and mtx[i - 1][j] == 1: # 방문하지 않은 좌표가 1인 경우
      answer[i - 1][j] = distance + 1
      queue.append((i - 1, j, distance + 1))
  
  # 아래로 갈 수 있는 경우
  if i < n - 1:
    if answer[i + 1][j] == -1 and mtx[i + 1][j] == 1: # 방문하지 않은 좌표가 1인 경우
      answer[i + 1][j] = distance + 1
      queue.append((i + 1, j, distance + 1))
  
  # 왼쪽으로 갈 수 있는 경우
  if j > 0:
    if answer[i][j - 1] == -1 and mtx[i][j - 1] == 1: # 방문하지 않은 좌표가 1인 경우
      answer[i][j - 1] = distance + 1
      queue.append((i, j - 1, distance + 1))
  
  # 오른쪽으로 갈 수 있는 경우
  if j < m - 1:
    if answer[i][j + 1] == -1 and mtx[i][j + 1] == 1: # 방문하지 않은 좌표가 1인 경우
      answer[i][j + 1] = distance + 1
      queue.append((i, j + 1, distance + 1))

for row in answer:
  print(' '.join(map(str, row)))