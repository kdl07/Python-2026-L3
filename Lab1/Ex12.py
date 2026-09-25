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