import sys

n = int(sys.stdin.readline())

arr = []

for i in range(n):
  arr.append(int(sys.stdin.readline()))

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
    if left[l] < right[r]:
      merged.append(left[l])
      l += 1
    else:
      merged.append(right[r])
      r += 1
    
  merged.extend(left[l:])
  merged.extend(right[r:])
  
  return merged

sorted_nums = sort(arr)

for n in sorted_nums:
  print(n)