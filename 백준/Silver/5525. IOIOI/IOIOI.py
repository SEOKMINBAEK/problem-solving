import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()
P = 'I' + 'OI' * N
cnt = 0

for i in range(M - len(P) + 1):
  if S[i] == 'I' and S[i:i + len(P)] == P:
    cnt += 1

print(cnt)