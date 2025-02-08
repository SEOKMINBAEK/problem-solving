a, b = map(int, input().split())

b = min(b, 10000000)

is_primes = [True] * (b + 1)
is_primes[0], is_primes[1] = False, False

for i in range(2, int(b ** 0.5) + 1):
  if is_primes[i]:
    for j in range(i * 2, b + 1, i):
      is_primes[j] = False

primes = [str(i) for i in range(a, b + 1) if is_primes[i]]

for prime in primes:
  if prime == prime[::-1]:
    print(prime)

print(-1)