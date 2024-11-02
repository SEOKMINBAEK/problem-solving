x = int(input())
n = int(input())
total = 0

for i in range(0, n):
  price, count = map(int, input().split())
  total += price * count

print("Yes" if total == x else "No")