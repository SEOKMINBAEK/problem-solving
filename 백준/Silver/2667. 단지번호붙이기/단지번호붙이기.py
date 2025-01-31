n = int(input())
mtx = [[] for _ in range(n)]
answer = { 'building': 0, 'household': [] }

for i in range(n):
  for c in input():
    mtx[i].append(int(c))

for i in range(n):
  for j in range(n):
    if mtx[i][j] == 0:
      continue
    
    mtx[i][j] = 0
    answer['building'] += 1
    queue = [(i, j)]
    
    for cur in queue:
      # 위에 집이 존재하는 경우
      if cur[0] > 0 and mtx[cur[0] - 1][cur[1]] == 1:
        mtx[cur[0] - 1][cur[1]] = 0
        queue.append((cur[0] - 1, cur[1]))
      
      # 아래에 집이 존재하는 경우
      if cur[0] < n - 1 and mtx[cur[0] + 1][cur[1]] == 1:
        mtx[cur[0] + 1][cur[1]] = 0
        queue.append((cur[0] + 1, cur[1]))
      
      # 왼쪽에 집이 존재하는 경우
      if cur[1] > 0 and mtx[cur[0]][cur[1] - 1] == 1:
        mtx[cur[0]][cur[1] - 1] = 0
        queue.append((cur[0], cur[1] - 1))
      
      # 오른쪽에 집이 존재하는 경우
      if cur[1] < n - 1 and mtx[cur[0]][cur[1] + 1] == 1:
        mtx[cur[0]][cur[1] + 1] = 0
        queue.append((cur[0], cur[1] + 1))
    
    answer['household'].append(len(queue))

print(answer['building'])

for cnt in sorted(answer['household']):
  print(cnt)