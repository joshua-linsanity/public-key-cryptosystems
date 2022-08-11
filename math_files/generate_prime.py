from random import randint
from math_files.miller_rabin_primality_test import miller_rabin
from math_files.fermat_primality_test import fermat


def find_prime(n, strength, test):
    if test == 0:
        while True:
            # find an n-digit prime
            p = randint(10 ** (n - 1), 10 ** n - 1)

            # check if it's probably prime
            if fermat(p, strength):
                return p
            else:
                pass
    elif test == 1:
        # Run Miller-Rabin primality test
        while True:
            p = randint(10 ** (n - 1), 10 ** n - 1)
            if miller_rabin(p, strength):
                return p
    assert False
