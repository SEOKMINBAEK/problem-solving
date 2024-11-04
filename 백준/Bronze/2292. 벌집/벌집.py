n = int(input())

i = 1
max = 1

while True:
  if max < n:
    max += 6 * i
    i += 1
  else:
    break

print(i)