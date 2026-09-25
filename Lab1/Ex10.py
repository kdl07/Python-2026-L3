# Ex10
def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

print(get_divisors(12))  # Output: [1, 2, 3, 4, 6, 12]