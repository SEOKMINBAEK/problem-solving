import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, m = map(int, input().split())
mtx = [[None for _ in range(m)] for _ in range(n)]
offset = (0, 0)
cnt = 0

def dfs(x, y):
  global cnt
  
  if x < 0 or x >= m or y < 0 or y >= n:
    return
  
  if mtx[y][x] == 'X':
    return
  
  if mtx[y][x] == 'P':
    cnt += 1
  
  mtx[y][x] = 'X'
  
  dfs(x - 1, y)
  dfs(x + 1, y)
  dfs(x, y - 1)
  dfs(x, y + 1)

for i in range(n):
  for j, char in enumerate(input().rstrip()):
    if char == 'I':
      offset = (j, i)
    
    mtx[i][j] = char

dfs(offset[0], offset[1])

print(cnt or 'TT')