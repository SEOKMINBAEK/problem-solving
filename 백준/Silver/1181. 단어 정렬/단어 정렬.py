from sys import stdin
input = stdin.readline

n = int(input())
s = set()

for _ in range(n):
  s.add(input().rstrip())

def sort(arr):
  if len(arr) <= 1: return arr
  
  mid = len(arr) // 2
  left = sort(arr[:mid])
  right = sort(arr[mid:])
  
  return merge(left, right)

def merge(left, right):
  l, r = 0, 0
  merged = []
  
  while l < len(left) and r < len(right):
    if len(left[l]) < len(right[r]):
      merged.append(left[l])
      l += 1
    elif len(left[l]) > len(right[r]):
      merged.append(right[r])
      r += 1
    else:
      appended = False
      for i in range(len(left[l])):
        if ord(left[l][i]) < ord(right[r][i]):
          merged.append(left[l])
          l += 1
          appended = True
          break
        elif ord(left[l][i]) > ord(right[r][i]):
          merged.append(right[r])
          r += 1
          appended = True
          break
        else: continue
      
      if not appended:
        merged.append(right[r])
        r += 1
  
  merged.extend(left[l:])
  merged.extend(right[r:])
  
  return merged

arr = list(s)
sorted_arr = sort(arr)

for word in sorted_arr:
  print(word)