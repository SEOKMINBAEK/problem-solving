import sys
input = sys.stdin.readline

is_primes = [True] * 1299710

is_primes[0], is_primes[1] = False, False

for i in range(2, int(1299709 ** 0.5) + 1):
  if is_primes[i]:
    for j in range(i * 2, 1299710, i):
      is_primes[j] = False

primes = [ i for i in range(1299710) if is_primes[i] ]

T = int(input())

for _ in range(T):
  k = int(input())
  
  if k in primes:
    print(0)
    continue
  
  l, r = 0, len(primes) - 1
  l_prime = 0
  r_prime = primes[r - 1]
  
  # 시작할 소수 찾기
  while l <= r: # 판별할 소수가 없을 떄까지
    mid = (l + r) // 2
    
    if primes[mid] < k: # 현재 소수가 찾는 값보다 작은 경우
      l_prime = primes[mid]
      l = mid + 1
    else: # 현재 소수가 찾는 값보다 큰 경우
      r_prime = primes[mid]
      r = mid - 1
  
  print(r_prime - l_prime)