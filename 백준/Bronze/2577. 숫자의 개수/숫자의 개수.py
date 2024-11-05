a = int(input())
b = int(input())
c = int(input())

string = str(a * b * c)

dic = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0,}

for c in string:
  dic[c] += 1

for key in dic:
  print(dic[key])