N, M = map(int, input().split())
array = []
answer = set()

for i, char in enumerate(input().split()):
  array.append((int(char), i))

def backtracking(arr):
  if len(arr) == M:
    answer.add(tuple([tu[0] for tu in arr]))
    return
  
  for tu in array:
    if tu not in arr:
      backtracking(arr + [tu])

backtracking([])

answer = sorted(list(answer))

for ans in answer:
  print(' '.join(str(x) for x in ans))