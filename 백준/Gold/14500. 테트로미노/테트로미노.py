import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mtx = []

def shape1(i, j):
  r_0, r_90 = 0, 0
  
  if j <= M - 4:
    r_0 = mtx[i][j] + mtx[i][j + 1] + mtx[i][j + 2] + mtx[i][j + 3]
  
  if i <= N - 4:
    r_90 = mtx[i][j] + mtx[i + 1][j] + mtx[i + 2][j] + mtx[i + 3][j]
  
  return max(r_0, r_90)

def shape2(i, j):
  r_0 = 0
  
  if i <= N - 2 and j <= M - 2:
    r_0 = mtx[i][j] + mtx[i][j + 1] + mtx[i + 1][j] + mtx[i + 1][j + 1]
  
  return r_0

def shape3(i, j):
  r_0, r_90, r_180, r_270 = 0, 0, 0, 0
  r_0_decal, r_90_decal, r_180_decal, r_270_decal = 0, 0, 0, 0
  
  if i <= N - 3 and j <= M - 2:
    r_0 = mtx[i][j] + mtx[i + 1][j] + mtx[i + 2][j] + mtx[i + 2][j + 1]
  
  if i <= N - 3 and j > 0:
    r_0_decal = mtx[i][j] + mtx[i + 1][j] + mtx[i + 2][j] + mtx[i + 2][j - 1]
  
  if i <= N - 2 and j <= M - 3:
    r_90 = mtx[i][j] + mtx[i][j + 1] + mtx[i][j + 2] + mtx[i + 1][j]
  
  if i > 0 and j <= M - 3:
    r_90_decal = mtx[i][j] + mtx[i][j + 1] + mtx[i][j + 2] + mtx[i - 1][j]
  
  if i <= N - 3 and j <= M - 2:
    r_180 = mtx[i][j] + mtx[i][j + 1] + mtx[i + 1][j + 1] + mtx[i + 2][j + 1]
  
  if i <= N - 3 and j > 0:
    r_180_decal = mtx[i][j] + mtx[i][j - 1] + mtx[i + 1][j - 1] + mtx[i + 2][j - 1]
  
  if i > 0 and j <= M - 3:
    r_270 = mtx[i][j] + mtx[i][j + 1] + mtx[i][j + 2] + mtx[i - 1][j + 2]
  
  if i <= N - 2 and j <= M - 3:
    r_270_decal = mtx[i][j] + mtx[i][j + 1] + mtx[i][j + 2] + mtx[i + 1][j + 2]
  
  return max(r_0, r_90, r_180, r_270, r_0_decal, r_90_decal, r_180_decal, r_270_decal)

def shape4(i, j):
  r_0, r_90 = 0, 0
  r_0_decal, r_90_decal = 0, 0
  
  if i <= N - 3 and j <= M - 2:
    r_0 = mtx[i][j] + mtx[i + 1][j] + mtx[i + 1][j + 1] + mtx[i + 2][j + 1]
  
  if i <= N - 3 and j > 0 :
    r_0_decal = mtx[i][j] + mtx[i + 1][j] + mtx[i + 1][j - 1] + mtx[i + 2][j - 1]
  
  if i > 0 and j <= M - 3:
    r_90 = mtx[i][j] + mtx[i][j + 1] + mtx[i - 1][j + 1] + mtx[i - 1][j + 2]
  
  if i <= N - 2 and j <= M - 3:
    r_90_decal = mtx[i][j] + mtx[i][j + 1] + mtx[i + 1][j + 1] + mtx[i + 1][j + 2]
  
  return max(r_0, r_90, r_0_decal, r_90_decal)

def shape5(i, j):
  r_0, r_90, r_180, r_270 = 0, 0, 0, 0
  
  if i <= N - 2 and j <= M - 3:
    r_0 = mtx[i][j] + mtx[i][j + 1] + mtx[i][j + 2] + mtx[i + 1][j + 1]
  
  if i > 0 and i <= N -2 and j <= M - 2:
    r_90 = mtx[i][j] + mtx[i][j + 1] + mtx[i - 1][j + 1] + mtx[i + 1][j + 1]
  
  if i > 0 and j <= M - 3:
    r_180 = mtx[i][j] + mtx[i][j + 1] + mtx[i][j + 2] + mtx[i - 1][j + 1]
  
  if i <= N - 3 and j <= M - 2:
    r_270 = mtx[i][j] + mtx[i + 1][j] + mtx[i + 2][j] + mtx[i + 1][j + 1]
  
  return max(r_0, r_90, r_180, r_270)

for _ in range(N):
  mtx.append(list(map(int, input().split())))

max_sum = 0

for i in range(N):
  for j in range(M):
    max_sum = max(max_sum, shape1(i, j), shape2(i, j), shape3(i, j), shape4(i, j), shape5(i, j))

print(max_sum)