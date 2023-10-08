"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def checkPrime(num):
    isPrime = True
    counter = 2
    if num == 1:
        isPrime = False
    else:
        while counter < num:
            if num % counter == 0:
                isPrime = False
            counter = counter + 1
    return isPrime 

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError(f"Value of {number_of_primes} provided as input is not a positive number")
    list = []
    currentNum = 1;
    while len(list) < number_of_primes:
        result = checkPrime(currentNum)
        if result == True:
            list.append(currentNum)
        currentNum = currentNum + 1
    return list

print(checkPrime(7))
print(primes(10))
#print(primes(-2))

