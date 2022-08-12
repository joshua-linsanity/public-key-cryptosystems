from random import randint
from math_files.fast_powering import successive_squaring

# run fermat primality test "strength" times
# returns prime number p
def fermat(p: int, strength: int):
    # this is a cop-out
    if p == 2:
        return True

    for i in range(strength):
        # find random int 1 < a < p - 1
        a = randint(2, p - 1)

        # test if fermat's theorem holds true
        # see if a**p % p == a
        if not successive_squaring(a, p, p) == a:
            return False

    return True
