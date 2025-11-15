def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number to check: "))
if is_prime(num):
    print("Prime")
else:
    print("Not prime")

limit = int(input("Generate primes up to: "))
primes = [x for x in range(2, limit+1) if is_prime(x)]
print("Primes:", primes)
