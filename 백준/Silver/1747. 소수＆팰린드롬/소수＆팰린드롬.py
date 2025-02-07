N = int(input())

nums = [True] * 10000001

nums[0], nums[1] = False, False

for i in range(2, 10000001):
  if nums[i]:
    for j in range(i * 2, 10000001, i):
      nums[j] = False

primes = [str(i) for i in range(10000001) if nums[i] and i >= N]

for prime in primes:
  if prime == prime[::-1]:
    print(prime)
    break