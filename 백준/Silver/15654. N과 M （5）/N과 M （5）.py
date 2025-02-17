N, M = map(int, input().split())
array = list(map(int, input().split()))
answer = []

def backtracking(arr):
  if len(arr) == M:
    answer.append(arr)
    return
  
  for i in array:
    if i not in arr:
      backtracking(arr + [i])

backtracking([])

answer.sort()

for ans in answer:
  print(' '.join(str(x) for x in ans))