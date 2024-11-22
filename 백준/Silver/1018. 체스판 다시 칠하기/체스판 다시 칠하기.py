n, m = map(int, input().split())
board = []

for _ in range(n):
  board.append(input())

white_start = ['WBWBWBWB', 'BWBWBWBW'] * 4 # (0,0) 좌표가 흰색 부터 시작인 경우 올바른 보드판 
black_start = ['BWBWBWBW', 'WBWBWBWB'] * 4 # (0,0) 좌표가 검은색 부터 시작인 경우 올바른 보드판 

need_change = 64

# (n-7)*(m-7)이 보드에서 나올수 있는 8*8 크기이다.
for i in range(n - 7):
  for j in range(m - 7):
    white_cnt = 0 # 흰색 패턴에서 찾은 잘못된 수
    black_cnt = 0 # 검은색 패턴에서 찾은 잘못된 수
    
    # (i, j) 좌표로 시작하는 가능한 모든 보드격자를 검사한다.
    for k in range( 8):
      for l in range(8):
        if board[i + k][j + l] != white_start[k][l]: # 흰색 시작인 보드판의 케이스에서 잘못된 경우
          white_cnt += 1
        if board[i + k][j + l] != black_start[k][l]: # 검은색 시작인 보드판의 케이스에서 잘못된 경우
          black_cnt += 1
    
    # 보드 검사가 한번 끝나면 바꿔야될 최소값을 구한다
    need_change = min(need_change, white_cnt, black_cnt)

print(need_change)