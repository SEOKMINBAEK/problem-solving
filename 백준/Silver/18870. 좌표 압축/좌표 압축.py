N = int(input())
offset = [[None, i] for i in range(N)]

for i, val in enumerate(map(int, input().split())):
  offset[i][0] = val

offset.sort()

results = []
mini = offset[0][0]
min_val = 0

for val in offset:
  if val[0] > mini:
    min_val += 1
  
  mini = val[0]
  val[0] = min_val

offset.sort(key=lambda x: x[1])
print(' '.join(str(x[0]) for x in offset))