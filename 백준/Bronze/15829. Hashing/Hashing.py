r = 31
m = 1234567891

l = int(input())
string = input()
sum = 0

for i, c in enumerate(string):
  n = ord(c) - (ord('a') - 1)
  sum += n * (r ** i)

print(sum % m)