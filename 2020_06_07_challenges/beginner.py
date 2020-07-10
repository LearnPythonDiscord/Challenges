"""
Beginner challenge: Take a number and return True if it is Even, False if it is Odd
Challenge 2: Return True if the Number is Prime, False if it isnt
Challenge 3: Return True if the Number is Mersenne prime, False if it isnt
"""
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def check_primes(n):
    return factorial(n-1) % n != 0

def mersenne_prime(n):
    s = 4
    m = (2 ** n) - 1
    for i in range(0,n-2):
        s = ((s**2) - 2) % m
    return s==0

def even_check(n):
    return n%2 ==0 

if __name__ == "__main__":
    n = int(input('Enter number'))
