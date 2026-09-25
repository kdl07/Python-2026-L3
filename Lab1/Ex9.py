# Ex9

# n = int(input('Please enter a number: '))
# fac = 1
# if n == 0:
#  print('Factorial of 0 is 1')
# elif n < 0:
#  print('Not exist such number like that')
# else:
#  for i in range(1,n+1):
#   fac = fac * i
#  print('Factorial of %d is %d' %(n, fac))
n = int(input('Please enter a number: '))
def facto(n):
  if n == 0 or n == 1:
    return 1
  return n * facto(n-1)

if facto(n):
  print('Factorial of %d is %d' %(n, facto(n)))