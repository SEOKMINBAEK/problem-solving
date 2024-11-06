nums = []
nums.append(input())
nums.append(input())
nums.append(input())

result = ""

for i, n in enumerate(nums):
  try:
    n = int(n)
    new_num = n + (3 - i)
    
    if new_num % 3 == 0:
      if new_num % 5 == 0:
        result = "FizzBuzz"
      else:
        result = "Fizz"
      break
    elif new_num % 5 == 0:
      result = "Buzz"
      break
    else:
      result = new_num
      break
    
  except:
    continue

print(result)