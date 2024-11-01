values = input().split(' ')
a, b = map(int, values)

if a > b:
  print('>')
elif a < b:
  print('<')
else:
  print('==')