import sys
input = sys.stdin.readline

n = int(input())

if n:
  opinion = []

  for _ in range(n):
    opinion.append(int(input()))

  opinion.sort()

  trim = len(opinion) * 0.15
  trim = int(trim) if (trim - int(trim)) < 0.5 else int(trim) + 1

  avg_li = opinion[trim:n - trim]
  avg = sum(avg_li) / len(avg_li)
  avg = int(avg) if (avg - int(avg)) < 0.5 else int(avg) + 1

  print(avg)
else:
  print(0)