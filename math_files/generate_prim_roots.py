import random
from math_files.fast_powering import successive_squaring


def find_prim_roots(p: int):
    # generate a random number 1 < g < p - 1
    # avoid i = 1 and i = p - 1 because g**i = 1 always

    while True:
        # test if g is primitive root
        g = random.randint(2, p - 1)
        primitive = True

        for i in range(1, p - 1):
            if successive_squaring(g, i, p) == 1:
                primitive = False
                break

        if primitive:
            return g
        else:
            continue

# Does not find primitive root (compromise security). But still generates results much more quickly. 
def find_fake_prim_roots(p: int):
    # generate a random number 1 < g < p - 1
    # avoid i = 1 and i = p - 1 because g**i = 1 always

    while True:
        # test if g is primitive root
        g = random.randint(2, p - 1)

        for i in range(1, p - 1):
            if successive_squaring(g, i, p) == 1:
                break
            else:
                return g