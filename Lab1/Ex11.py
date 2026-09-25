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