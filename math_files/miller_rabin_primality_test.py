from random import randint
from math_files.fast_powering import successive_squaring


# returns True if probably prime
# returns False if not prime
def miller_rabin(p: int, strength: int):
    if p == 2:
        return True

    # STEP 1
    k = 0
    q = 0
    left_hand_side = p - 1

    # Rewrite p - 1 = 2**k * q
    while True:
        left_hand_side //= 2
        k += 1

        # if left_hand_side is odd
        if left_hand_side % 2 != 0:
            q = left_hand_side
            break

    # Loop many times
    for i in range(strength):

        # Check for Miller-Rabin witnesses
        a = randint(1, p - 1)

        val = p - 1  # (= 2**k * q)

        if successive_squaring(a, q, p) == 1:
            pass
        else:
            # initialize
            counter = 0
            x = 0

            while True:
                # Base Case
                if counter == 0:
                    x = successive_squaring(a, q, p)
                # redefine x
                else:
                    x = x ** 2 % p

                # check if x is -1 mod p
                if x % p == p - 1:
                    break

                # check if last case
                if not counter < p:
                    return False

                counter += 1

    return True
