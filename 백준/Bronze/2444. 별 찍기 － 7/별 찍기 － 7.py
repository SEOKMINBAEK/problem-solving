n = int(input())

for i in range(0, n):
  print((' ' * (n - (i + 1))) + ('*' * (1 + (i * 2))))

for i in range(n - 1 , 0, -1):
  print((' ' * (n - i)) + ('*' * ((i * 2) - 1)))