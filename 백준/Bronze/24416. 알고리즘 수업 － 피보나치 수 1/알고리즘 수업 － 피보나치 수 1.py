n = int(input())

table = [0] * (n + 1)

for i in range(1, n + 1):
  if i <= 2:
    table[i] = 1
  else:
    table[i] = table[i - 1] + table[i - 2]

print(table[n], n - 2)