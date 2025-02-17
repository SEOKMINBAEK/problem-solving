N, M = map(int, input().split())
array = list(map(int, input().split()))
answer = set()

def backtracking(arr):
  if len(arr) == M:
    answer.add(tuple(arr))
    return
  
  i = 0
  
  while i < N:
    if len(arr) == 0 or arr[-1] <= array[i]:
      backtracking(arr + [array[i]])
    i += 1

backtracking([])

answer = sorted(list(answer))

for ans in answer:
  print(' '.join(str(x) for x in ans))