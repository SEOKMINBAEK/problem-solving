from math import factorial

n, k = map(int, input().split())

numerator = factorial(n)
denominator = factorial(k) * factorial(n -k)

print(numerator // denominator)