# Ex1
import math
r = float(input('Enter circle radius:')) ;
Circle_area = math.pi * r**2;
print('The area of the circle is: %0.2f' %Circle_area);

# Ex2
Celsius = float(input('Enter the temperature in Celsius? ')) ;
Farenheit = (Celsius * 1.8) + 32
print(' %0.2f (C) = %0.2f (F)' %(Celsius, Farenheit) );

# Ex3
num = int(input('Please enter a number: '))
flag = False

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

# Ex4
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

# Ex5
my_colors = ["Red", "Green", "Blue"];
user_color = input('What is yout favorite color? ');
if user_color in my_colors:
  index = my_colors.index(user_color);
  print(f"Yout color is at index {index} in my list ")
else:
  print('Sorry, I could not find your color')

# Ex6
r1 = list(range(0,7))
r2 = list(range(1,11,3))
r3 = list(range(5,0,-1))
r4 = list(range(6,-3,-2))
print(r1);
print(r2);
print(r3);
print(r4);

# Ex7
def remove_dollar_sign(s):
    return s.replace("$", "")

input_str = "Price is $100$!"
print(remove_dollar_sign(input_str))

# Ex8
listnum = [1,4,5,-1,10]
def extract_even(l):
  return [x for x in l if x % 2 == 0]

if extract_even(listnum):
  print(f" {extract_even(listnum)}")

# Ex9
n = int(input('Please enter a number: '))
def facto(n):
  if n == 0 or n == 1:
    return 1
  return n * facto(n-1)

if facto(n):
  print('Factorial of %d is %d' %(n, facto(n)))

# Ex10
def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

print(get_divisors(12))  # Output: [1, 2, 3, 4, 6, 12]

# Ex11
import math

x0 = float(input('Enter vertical value of A: '))
y0 = float(input('Enter horizontal value of A: '))
A = [x0, y0]

x1 = float(input('Enter vertical value of B: '))
y1 = float(input('Enter horizontal value of B: '))
B = [x1, y1]

def d_2points(A, B):
    return math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)

if d_2points(A, B):
    print(f'Distance between A and B is: {d_2points(A, B)}')
else:
    print('Distance between A and B is: 0.0')

# Ex12
def print_pattern(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("* ", end="")
            else:
                print("  ", end="") 
        print()  # Move to the next line after each row

# 4x5 rectangle of asterisks
print_pattern(4, 5)