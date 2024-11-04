n = int(input())

offsets = []
width = 0

for _ in range(0, n): # 색종이의 갯수 만큼 반복
  x, y = map(int, input().split()) # 색종이의 시작 좌표
  temp = []
  
  for i in range(x, x + 10):
    for j in range(y, y + 10):
      temp.append("%d, %d" % (i, j)) # 색종이의 시작좌표부터 종료좌표까지 차지하는 좌표를 리스트에 담는다. 좌표의 갯수는 100개가 된다.
  
  for offset in offsets: # 이전 색종이들의 좌표를 순회하면서,
    for xy in offset: # 각 색종이들이 차지하는 좌표를 불러온다.
      if xy in temp: # 만약 현재 색종이가 차지하는 좌표가 이전 색종이에도 존재한다면
        idx = temp.index(xy)
        del temp[idx] # 해당 좌표를 제거한다.
  
  width += len(temp) # 중복된 좌표가 제거된 현재 색종이가 차지하는 좌표의 갯수를 더한다.
  offsets.append(temp) # 중복 제거된 색종이를 색종이 리스트에 담는다.

print(width)