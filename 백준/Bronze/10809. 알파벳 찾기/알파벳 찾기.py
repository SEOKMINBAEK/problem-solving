string = input()

alpha = [chr(n) for n in range(ord('a'), ord('z') + 1)]
result = []

for c in alpha:
  idx = string.find(c)
  result.append(str(idx))

print(" ".join(result))