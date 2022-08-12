from math_files.generate_prime import find_prime
from math_files.modular_inverse import extended_euclidean, inverse_mod
from math_files.fast_powering import successive_squaring
from termcolor import colored

# convert message (case: str) to int m and str case
# returns m, case
def decimal(s: str, N: int):
    # store case-sensitivity in binary number
    case = ""
    for i in s:
        if i.islower() == True:
            case += "0"
        else:  # upper or space
            case += "1"

    s_upper = s.upper()
    exp = 0
    m = 0

    for i in s_upper[::-1]:
        i = ord(i)  # convert to ASCII code
        if i >= 65 and i <= 90:
            m += 27 ** exp * (i - 64)
        elif i == 32:  # ASCII code for space
            # space is 0 in base 27
            m += 27 ** exp * 0
        else:
            raise Exception("Unsupported character... no punctuation except spaces allowed")
        exp += 1

    assert (m >= 2) and (m <= N - 1), "Message too large/small"

    return m, case


# returns c
def encrypt(N: int, e: int, m: int):
    c = successive_squaring(m, e, N)

    return c


print("STEP 1: GET INPUTS")
s = input("Bob's secret message: ")
N = int(input("Bob receives N from Alice: "))
e = int(input("Bob receives e from Alice: "))

print("\nSTEP 2: ENCRYPT")
m, case = decimal(s, N)
c = encrypt(N, e, m)
print(f"Bob sends", colored(f"c", "red"), "to Alice:", colored(f"{c}", "red"))
print(f"Bob sends", colored(f"case", "red"), "to Alice:", colored(f"{case}", "red"))
