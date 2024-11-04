max = -1
offset = (0, 0)

for i in range(0, 9):
  row = list(map(int, input().split()))
  
  for j in range(0, 9):
    if row[j] > max:
      max = row[j]
      offset = (i + 1, j + 1)

print(max)
print("%d %d" % (offset[0], offset[1]))