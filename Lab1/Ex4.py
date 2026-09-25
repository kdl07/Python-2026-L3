# Ex4
# A perfect number is divisible of its sum of its divisor
def perfect(n):
  if n < 1:
    return False
  else:
    div_sum = sum(i for i in range (1,n) if n % i == 0)
    return div_sum == n

n = int(input('Please enter a number: '))
if perfect(n):
  print('%d is a perfect number' %n)
else:
  print('%d is not a perfect number' %n)