# A function that receives a number of integers (T) and a integer (n) to see if its prime or not
#Optimized solution
import math

def isPrime(n):
    if n<=1:
        return False
    sqrt_n = math.sqrt(n)
    if sqrt_n.is_integer():
        return False    
    for i in range(2, int(sqrt_n)+1):
        if n % i == 0:
            return False
    return True


T = int(input("Number of integers: "))
for i in range(T):
    n = int(input("Integer: "))
    if isPrime(n):
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")
