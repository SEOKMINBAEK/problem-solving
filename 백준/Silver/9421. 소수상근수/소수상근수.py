# n 이하의 수로 범위 설정
n = int(input())
is_primes = [True] * (n + 1)
is_primes[0], is_primes[1] = False, False

# 소수로만 범위 설정
for i in range(2, n + 1):
  if is_primes[i]: # i가 소수가 아니면
    for j in range(i * 2, n + 1, i): # i의 배수를 모두 False 처리
      is_primes[j] = False

primes = [i for i in range(n + 1) if is_primes[i]]

# 상근수 검사
for i in primes:
  visited = { 1 }
  calc = i
  
  while calc not in visited:
    visited.add(calc)
    tot = 0
    
    for char in str(calc):
      tot += int(char) ** 2
    
    calc = tot
  
  if calc == 1:
    print(i)