# Level 3 Question 1

"""
#VERSION 1 (O(√n))
from math import sqrt

def is_prime(n):
    #a prime number only has 2 factors, 1 and itself
    if n == 1:
        return f"1 is neither prime not composite."
    if n == 2:
        return True
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a natural number: "))
print(is_prime(num)
"""

# VERSION 2 (improved - O(√n)) - cuts the number of iterations by approximately half by only checking odd numners
from math import sqrt

def is_prime(n):
    #a prime number only has 2 factors, 1 and itself
    if n == 1:
        return f"1 is neither prime not composite."
    if n == 2:
        return True
    if n % 2 == 0:
        return False 
    for i in range(3, int(sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True

while True:
    num = int(input("Enter a natural number: "))
    if num == 0:
        break
    print(is_prime(num))