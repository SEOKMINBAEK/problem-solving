import sys
input = sys.stdin.readline

def round(n):
  is_negative = n < 0
  abs_n = abs(n)
  f = abs_n - int(abs_n)
  return int(n) if f < 0.5 else int(n) - 1 if is_negative else int(n) + 1

n = int(input())
dic = {}
arr = []
sum = 0

for _ in range(n):
  num = input().rstrip()
  sum += int(num)
  arr.append(int(num))
  
  if dic.get(num):
    dic[num] += 1
  else:
    dic[num] = 1

arr.sort()
mode_v = max(dic.items(), key=lambda v: v[1])[1]
modes = list(filter(lambda v: v[1] == mode_v, dic.items()))
modes.sort(key=lambda v: int(v[0]))
maxi = max(dic.items(), key=lambda v: int(v[0]))
mini = min(dic.items(), key=lambda v: int(v[0]))

avg = round(sum / n)
mid = arr[n // 2]
mode = modes[1 if len(modes) > 1 else 0][0]
range = int(maxi[0]) - int(mini[0])
print(avg)
print(mid)
print(mode)
print(range)