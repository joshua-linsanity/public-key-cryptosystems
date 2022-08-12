from math_files.generate_prime import find_prime
from math_files.modular_inverse import extended_euclidean, inverse_mod
from math_files.fast_powering import successive_squaring
from termcolor import colored


# returns N=pq and encryption exponent e
def key_creation(p: int, q: int):
    # Initialize
    e = 2
    gcd = 0

    # Find e
    while True:
        gcd, u, v = extended_euclidean(e, (p - 1) * (q - 1))
        if gcd == 1:
            break
        else:
            e += 1

    N = p * q

    return N, e


# returns message number m
def decrypt(e: int, p: int, q: int, c: int):
    d = inverse_mod(e, (p - 1) * (q - 1))
    m = successive_squaring(c, d, N)

    return m


# converts m and case into secret message: str
def septemvigesimal(m: int, case: str):
    decrypted_message = ""

    # count from last to first char
    while True:
        remainder = m % 27

        if remainder != 0:
            decrypted_message += chr((remainder + 64))
        else:
            # must be space; remainder = 26
            # 95 is ASCII space code
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


# INPUTS
num_digits_p = int(input("Number of digits in prime p: "))
num_digits_q = int(input("Number of digits in prime q: "))
num_repeats = int(input("Run primality test how many times?: "))
primality_test = int(input("Press 0 for Fermat, 1 for Miller-Rabin: "))
p = find_prime(num_digits_p, num_repeats, primality_test)
q = find_prime(num_digits_q, num_repeats, primality_test)

print("\nSTEP 1: KEY CREATION")
# Publish public keys
N, e = key_creation(p, q)
print(f"Alice sends", colored(f"N", "red"), "to Bob:", colored(f"{N}", "red"))
print(f"Alice sends", colored(f"e", "red"), "to Bob:", colored(f"{e}", "red"))

print("\nSTEP 2: DECRYPTION")
# Compute m
c = int(input("Alice receives c from Bob: "))
m = decrypt(e, p, q, c)

# Convert to message
case = input("Alice receives case from Bob: ")
secret = septemvigesimal(m, case)
print(colored(f"SECRET MESSAGE: {secret}", "green"))
