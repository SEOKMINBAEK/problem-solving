time = input().split(' ')
h, m = map(int, time)

if m >= 45:
  m -= 45
else:
  m = (m + 60) - 45
  h = (h - 1) if h > 0 else 23

print(h, m)