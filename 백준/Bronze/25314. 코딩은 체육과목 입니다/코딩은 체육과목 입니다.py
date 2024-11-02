n = int(input())

q, r = divmod(n, 4)
q = q + 1 if r != 0 else q

for i in range(0, q):
  print("long", end=" ")

print("int")