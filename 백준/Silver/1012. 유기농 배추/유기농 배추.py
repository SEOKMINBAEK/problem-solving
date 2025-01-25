import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i, j, mtx):
  if i < 0 or i >= n or j < 0 or j >= m:
    return
  
  if mtx[i][j] == 0:
    return
  
  mtx[i][j] = 0
  
  dfs(i - 1, j, mtx)
  dfs(i + 1, j, mtx)
  dfs(i, j - 1, mtx)
  dfs(i, j + 1, mtx)

t = int(input())

for _ in range(t):
  m, n, k = map(int, input().split())
  mtx = [[0 for _ in range(m)] for _ in range(n)]
  
  for _ in range(k):
    j, i = map(int, input().split())
    mtx[i][j] = 1
  
  cnt = 0
  
  for i in range(n):
    for j in range(m):
      if mtx[i][j] == 1:
        dfs(i, j, mtx)
        cnt += 1
  
  print(cnt)