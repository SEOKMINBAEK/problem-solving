import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
mtx = [[None, float('inf')] for _ in range(101)]

for _ in range(N):
  x, y = map(int, input().split())
  mtx[x][0] = y

for _ in range(M):
  u, v = map(int, input().split())
  mtx[u][0] = v

move = [1, 2, 3, 4, 5, 6]
queue = deque([(1, 1)])

while queue:
  x, cnt = queue.popleft()
  
  if x == 100:
    print(mtx[100][1])
    break
  
  for dx in move:
    nx = x + dx
    
    # 도착한 칸이 100번 이하이고 도착까지 던진 주사위 횟수가 저장된 횟수보다 더 작은 경우
    if nx <= 100 and cnt < mtx[nx][1]:
      mtx[nx][1] = cnt
      queue.append((mtx[nx][0] or nx, cnt + 1))