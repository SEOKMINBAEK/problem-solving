n = int(input())

table = [0] * (n + 1)

for i in range(2, n + 1):
  if i <= 3:
    table[i] = 1
  
  mini = table[i - 1]
  
  if i % 2 == 0:
    mini = min(mini, table[i // 2])
  
  if i % 3 == 0:
    mini = min(mini, table[i // 3])
  
  table[i] = mini + 1

print(table[n])