import sys
input = sys.stdin.readline

n = int(input())
mtx = []

for _ in range(n):
  mtx.append(list(map(int, input().split())))

def div(mtx, cnt = { 'white': 0, 'blue': 0 }):
  se = set()
  rowlen = len(mtx)
  collen = len(mtx[0])
  
  for row in mtx:
    for val in row:
      se.add(val)
  
  if len(se) > 1:
    div([[mtx[i][j] for j in range(collen // 2)] for i in range(rowlen // 2)], cnt)
    div([[mtx[i][j] for j in range(collen // 2, collen)] for i in range(rowlen // 2)], cnt)
    div([[mtx[i][j] for j in range(collen // 2)] for i in range(rowlen // 2, rowlen)], cnt)
    div([[mtx[i][j] for j in range(collen // 2, collen)] for i in range(rowlen // 2, rowlen)], cnt)
  else:
    if 0 in se:
      cnt['white'] += 1
    else:
      cnt['blue'] += 1
  
  return [cnt['white'], cnt['blue']]

white, blue = div(mtx)

print(white)
print(blue)