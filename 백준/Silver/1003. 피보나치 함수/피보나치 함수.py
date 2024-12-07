import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  
  table = [(1, 0), (0, 1)]
  
  for i in range(2, n + 1):
    table.append((table[i - 1][0] + table[i - 2][0], table[i - 1][1] + table[i - 2][1]))

  cnt_0, cnt_1 = table[n]
  print(cnt_0, cnt_1)