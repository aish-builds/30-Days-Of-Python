# Level 1 Question 3

def add_all_nums(*nums): #uses unpacking operator to create an iterable object of type tuple (arbitrary arguments)
    sum = 0
    for num in nums:
        if not isinstance(num, (int, float)):
            return f"Invalid input: {num} is not a number."
        sum += num
    return sum

sum = add_all_nums(1,2,3)
print(f"Sum: {sum}")

# Level 1 Question 7

from math import sqrt

def solve_quadratic_eqn(a, b, c):
    if b**2 - (4*a*c) < 0:
        return f"No real solutions."
    elif b**2 - (4*a*c) == 0:
        return f"x = {-b/2*a}"
    else:
        sol_1 = (-b + sqrt(b**2 - (4*a*c)))/2*a
        sol_2 = (-b - sqrt(b**2 - (4*a*c)))/2*a
        return f"x1 = {sol_1}, x2 = {sol_2}"
    
a, b, c = map(float, input("Enter a, b, c (ax² + bx + c = 0): ").split())
print(solve_quadratic_eqn(a, b, c))

