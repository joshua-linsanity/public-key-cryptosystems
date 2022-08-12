from math_files.fast_powering import successive_squaring
from math_files.generate_prime import find_prime
from math_files.generate_prim_roots import find_prim_roots
from math_files.modular_inverse import inverse_mod
from termcolor import colored
import random

# return p, g
def publish_parameters(n: int, test_ID: int, strength: int):
    

    p = find_prime(n, strength, test_ID)
    g = find_prim_roots(p)

    return p, g


# return A, a
def key_creation(p: int, g: int):
    a = random.randint(1, p - 2)
    print(f"a: {a}")
    A = successive_squaring(g, a, p)

    return A, a


# return m
def decrypt(c1a: int, c2: int, p: int):
    m = (inverse_mod(c1a, p) * c2) % p
    return m


# return secret
def septemvigesimal(m: int, case: str):
    decrypted_message = ""

    # count from last to first char
    while True:
        remainder = m % 27

        if 1 <= remainder <= 26:
            decrypted_message += chr((remainder + 64))
        else:
            # must be space; remainder = 0
            decrypted_message += chr(32)

        # if floor function is 0, then no more digits
        m //= 27
        if m == 0:
            break

    # reverse so it becomes first to last
    not_reversed = decrypted_message[::-1]
    secret = ""

    for idx, val in enumerate(case):
        # default is upper, change to lower
        if val == '0':
            character = not_reversed[idx].lower()
            secret += character
        else:
            secret += not_reversed[idx]
    return secret


print("STEP 1: GENERATION")
# Inputs
num_digits = int(input("Number of digits in prime: "))
primality_test = int(input("Press 0 for Fermat, 1 for Miller-Rabin: "))
num_repeats = int(input("Run primality test how many times?: "))

# Generate
p, g = publish_parameters(num_digits, primality_test, num_repeats)
A, a = key_creation(p, g)
print("Alice", colored("sends", "red"), "to Bob (p g A) =", colored(f"\n{p} {g} {A}", "red"))


print("\nSTEP 2: DECRYPTION")
# Received from Bob
c1c2case = input("Alice receives (c1 c2 case) from Bob: ")

# String tuple
c1, c2, case = tuple(val for val in c1c2case.split())

# Change c1 and c2 to ints
c1 = int(c1)
c2 = int(c2)

# Calculate
c1a = successive_squaring(c1, a, p)
m = decrypt(c1a, c2, p)

# Display secret message
secret = septemvigesimal(m, case)
print(colored(f"SECRET MESSAGE: {secret}", "green"))
