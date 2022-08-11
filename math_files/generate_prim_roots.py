import random
from math_files.fast_powering import successive_squaring


# Fake version but much quicker
def find_prim_roots(p):
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

# Real version but much slower
# def find_prim_roots(p):
#     # generate a random number 1 < g < p - 1
#     # avoid i = 1 and i = p - 1 because g**i = 1 always
#
#     while True:
#         # test if g is primitive root
#         g = random.randint(2, p - 1)
#         primitive = True
#
#         for i in range(1, p - 1):
#             if successive_squaring(g, i, p) == 1:
#                 primitive = False
#                 break
#
#         if primitive:
#             return g
#         else:
#             continue
