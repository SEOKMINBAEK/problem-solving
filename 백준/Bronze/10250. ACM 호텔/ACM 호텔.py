t = int(input())

for _ in range(0, t):
  h, w, n = map(int, input().split())
  
  room = (n // h) + 1
  floor = n % h
  
  if floor == 0:
    floor = h
    room -= 1
  
  floor = str(floor)
  room = str(room) if room > 9 else '0' + str(room)
  
  print("%s%s" % (floor, room))