N, M = map(int, input().split())

def backtracking(arr):
  if len(arr) == M:
    print(' '.join(str(x) for x in arr))
    return
  
  for i in range(1, N + 1):
    if len(arr) == 0 or (i not in arr and arr[-1] < i):
      backtracking(arr + [i])

backtracking([])