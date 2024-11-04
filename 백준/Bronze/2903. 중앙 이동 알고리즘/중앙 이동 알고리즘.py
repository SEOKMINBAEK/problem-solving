n = int(input())
side = 2

for i in range(0, n):
  side = side + (side - 1)

print(side * side)