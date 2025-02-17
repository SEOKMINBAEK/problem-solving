N, M = map(int, input().split())

def backtracking(arr):
  if len(arr) == M:
    print(' '.join(str(x) for x in arr))
    return
  
  i = 1
  
  while i <= N:
    if len(arr) == 0 or arr[-1] <= i:
      backtracking(arr + [i])
    i += 1

backtracking([])