import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = [[None for _ in range(C)] for _ in range(R)]

for i in range(R):
  for j, char in enumerate(input().rstrip()):
    board[i][j] = (char, 0)

result = 0

def dfs(i, j, dist, visited):
  if board[i][j][1] >= dist:
    return
  
  global result
  result = max(result, dist)
  
  visited = visited.copy()
  visited.add(board[i][j][0])
  
  if i > 0 and board[i - 1][j][0] not in visited:
    dfs(i - 1, j, dist + 1, visited)
  if i < R - 1 and board[i + 1][j][0] not in visited:
    dfs(i + 1, j, dist + 1, visited)
  if j > 0 and board[i][j - 1][0] not in visited:
    dfs(i, j - 1, dist + 1, visited)
  if j < C - 1 and board[i][j + 1][0] not in visited:
    dfs(i, j + 1, dist + 1, visited)

dfs(0, 0, 1, set())

print(result)