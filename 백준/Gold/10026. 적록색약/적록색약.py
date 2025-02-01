import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
mtx = [[] for _ in range(n)]
visited = [[[0, 0] for _ in range(n)] for _ in range(n)]

for i in range(n):
  for char in input().rstrip():
    mtx[i].append(char)

section1 = 0
section2 = 0

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(n):
  for j in range(n):
    if not visited[i][j][0]:
      section1 += 1
      queue1 = deque([(i, j)])
      visited[i][j][0] = 1
      
      while queue1:
        cur_i, cur_j = queue1.popleft()
        char = mtx[cur_i][cur_j]
        for dy, dx in move:
          y = cur_i + dy
          x = cur_j + dx
          if -1 < y < n and -1 < x < n:
            if not visited[y][x][0] and mtx[y][x] == char:
              visited[y][x][0] = 1
              queue1.append((y, x))
    
    if not visited[i][j][1]:
      section2 += 1
      queue2 = deque([(i, j)])
      visited[i][j][1] = 1
      
      while queue2:
        cur_i, cur_j = queue2.popleft()
        char = mtx[cur_i][cur_j]
        for dy, dx in move:
          y = cur_i + dy
          x = cur_j + dx
          if -1 < y < n and -1 < x < n:
            if not visited[y][x][1] and (mtx[y][x] == char or (mtx[y][x] != 'B' and char != 'B')):
              visited[y][x][1] = 1
              queue2.append((y, x))

print(section1, section2)