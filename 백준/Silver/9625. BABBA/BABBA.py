k = int(input())
table = [(1, 0)]

for i in range(1, k + 1):
  if i == 1:
    table.append((0, 1))
  else:
    table.append((table[i - 1][0] + table[i - 2][0], table[i - 1][1] + table[i - 2][1]))

print(table[k][0], table[k][1])