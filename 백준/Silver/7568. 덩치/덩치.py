n = int(input())
li = []

for _ in range(n):
  li.append(tuple(map(int, input().split())))

rank_li = []

for w, h in li:
  bigger = list(filter(lambda v: v[0] > w and v[1] > h, li))
  rank_li.append(str(len(bigger) + 1))

print(' '.join(rank_li))