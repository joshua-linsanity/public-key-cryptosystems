# finds u, v such that au + nv = gcd(a, n)
# returns gcd, u, v as tuple
# Written by DarthBaguette
# def extended_euclidean(x: int, y: int):
    # number of steps in the euclidean algorithm
    # steps = 0

    # # how many multiples of the larger number are there? 
    # # i.e., if gcd(a, b) = au + bv, and a > b, then multiples = u
    # multiples = 0

    # # track the multiples of {a} in the previous two remainders
    # multiple_one = 0
    # multiple_two = 0

    # # these will stay unchanged
    # global_larger = max([x, y])
    # global_smaller = min([x, y])

    # # these will be modified by the loop
    # mutable_larger = global_larger
    # mutable_smaller = global_smaller

    # while True: 
    #     steps += 1

    #     remainder = mutable_larger % mutable_smaller
    #     whole = mutable_larger // mutable_smaller

    #     # change multiples
    #     # initialize
    #     if steps <= 2:
    #         multiple_one = 1
    #         multiple_two = whole
    #     elif remainder != 0:
    #         multiples = multiple_one + multiple_two * whole

    #         temp = multiple_one
    #         multiple_one = multiple_two
    #         multiple_two = temp + multiple_two * whole

    #     if remainder != 0:
    #         mutable_larger = mutable_smaller
    #         mutable_smaller = remainder
    #         pass
    #     else:
    #         if steps == 2:
    #             multiples = multiple_one
    #         elif steps == 3:
    #             multiples = multiple_one * multiple_two
    #         if steps % 2 != 0:
    #             multiples *= -1
    #         gcd = mutable_smaller
    #         u = multiples
    #         v = int((mutable_smaller - global_larger * multiples) / global_smaller)

    #         return gcd, u, v

# Simplified version
# Credits: https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/
def extended_euclidean(a: int, n: int):
    # base case
    if a == 0:
        return n, 0, 1

    gcd, u1, v1 = extended_euclidean(n % a, a)

    # Update x and y using results of recursive call
    u = v1 - (n // a) * u1
    v = u1

    return gcd, u, v

# solving ax = b (mod n)
# special case b = 1, n is prime, g is prim root
# thus x = ub (mod p) = u (mod p)
def inverse_mod(a: int, n: int):
    u = extended_euclidean(a, n)[1]
    return u % n
