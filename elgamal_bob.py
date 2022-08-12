from math_files.fast_powering import successive_squaring
from termcolor import colored


# converts string s to decimal int m
# string s stores secret
def decimal(s: str, p: int):
    # store case-sensitivity in binary number
    case = ""
    for i in s:
        if i.islower():
            case += "0"
        else:  # upper or space
            case += "1"

    s_upper = s.upper()
    exp = 0
    m = 0

    for i in s_upper[::-1]:
        i = ord(i)  # convert to ASCII code
        if 65 <= i <= 90:
            m += 27 ** exp * (i - 64)
        elif i == 32:  # ASCII codes for space
            # space is 0 in base 27
            m += 0
        else:
            raise Exception("Unsupported character... no punctuation except spaces allowed")
        exp += 1

    print(f"m: {m}")
    assert 2 <= m <= p - 1, "Message too large/small"

    return m, case

def encrypt(p: int, g: int, m: int, A: int, k: int):
    c1 = successive_squaring(g, k, p)
    c2 = (m * successive_squaring(A, k, p)) % p

    return c1, c2


print("STEP 1: BOB RECEIVES INPUTS")
pga = input("Bob receives (p g A) from Alice: ")
p, g, A = tuple(int(val) for val in pga.split())

print("\nSTEP 2: BOB MAKES DECISIONS")
k = int(input("Bob chooses an arbitrary number k: "))
s = input(colored("SECRET MESSAGE: ", "green"))

print("\nSTEP 3: BOB SENDS OUTPUTS")
m, case = decimal(s, p)
c1, c2 = encrypt(p, g, m, A, k)
print("Bob", colored("sends", "red"), "to Alice (c1 c2 case) =", colored(f"\n{c1} {c2} {case}", "red"))
