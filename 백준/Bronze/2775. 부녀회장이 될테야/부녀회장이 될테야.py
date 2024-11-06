t = int(input()) * 2

for idx in range(0, t):
  if idx % 2 == 0:
    k = int(input())
  else:
    n = int(input())

    apt = [[f for f in range(0, n + 1)]]
    
    for i in range(1, k + 1): #층
      floor = [0]
      
      for j in range(1, n + 1): #호
        prev = floor[j - 1]
        under = apt[i - 1][j]
        floor.append(prev + under)
      apt.append(floor)
    
    print(apt[i][j])