# Write a program to generate prime numbers with the help of a function to test prime or not.

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5) + 1):  # check up to sqrt(num)
        if num % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage
upper_limit = int(input("Enter the upper limit to generate prime numbers: "))
print(f"Prime numbers up to {upper_limit}:", generate_primes(upper_limit))


user_prime_number_check = int(input("Enter a number to check if it's prime: "))

print(is_prime(user_prime_number_check))

if is_prime(user_prime_number_check):
    print(f"{user_prime_number_check} is a prime number.")
else:
    print(f"{user_prime_number_check} is not a prime number.")



