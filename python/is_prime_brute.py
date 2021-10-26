# A function that receives a number of integers (T) and a integer (n) to see if its prime or not
#Brute solution
def isPrime(n):
    if n<=1:
        return False
    for i in range(2, n):
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
