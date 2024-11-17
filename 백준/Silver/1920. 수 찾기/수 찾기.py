import sys
input = sys.stdin.readline

n = int(input())
n_arr = list(map(int, input().split()))
n_arr.sort()

m = int(input())
m_arr = map(int, input().split())

def bs(value, front = 0, rear = n):
  mid = front + ((rear - front) // 2)
  if front == mid and n_arr[mid] != value:
    return 0
  
  if value > n_arr[mid]:
    return bs(value, mid, rear)
  elif value < n_arr[mid]:
    return bs(value, front, mid)
  else:
    return 1

for v in m_arr:
  print(bs(v))