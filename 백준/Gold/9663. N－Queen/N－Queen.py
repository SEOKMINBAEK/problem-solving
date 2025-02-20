"""
2차원 배열의 체스판을 만들지 않고, 각 행의 퀸이 놓인 열의 위치만 기록한다.
"""

N = int(input())
cnt = 0

# 같은 열, 대각선 상에 퀸이 존재하는지 검사
def is_valid(queens, row, col):
  for r, c in enumerate(queens):
    if c == col or abs(c - col) == abs(r - row):
      return False
  
  return True

def backtracking(row, queens):
  global cnt
  
  if row == N: # 모든 행에 퀸을 놓은 경우
    cnt += 1
    return
  
  for col in range(N):
    if is_valid(queens, row, col):
      backtracking(row + 1, queens + [col])

backtracking(0, [])

print(cnt)