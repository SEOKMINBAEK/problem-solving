words = input().strip()
space = 0

for c in words:
  if c == ' ':
    space += 1

print(space + 1 if words else space)