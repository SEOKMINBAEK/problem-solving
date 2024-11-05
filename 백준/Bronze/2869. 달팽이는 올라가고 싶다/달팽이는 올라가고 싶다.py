import math

up, down, height = map(int, input().split())
one_day_going = up - down
day = 1

if one_day_going < height:
  day += math.ceil((height - up) / one_day_going)

print(day)