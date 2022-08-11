def extended_euclidean(a, n):
    # finds u, v such that au + nv = gcd(a, n)
    # base case
    if a == 0:
        return n, 0, 1

    gcd, u1, v1 = extended_euclidean(n % a, a)

    # Update x and y using results of recursive
    # call
    u = v1 - (n // a) * u1
    v = u1

    return gcd, u, v


def inverse_mod(a, n):
    # solving ax = b (mod n)
    # special case b = 1, n is prime, g is prim root
    # thus x = ub (mod p) = u (mod p)
    gcd, u, v = extended_euclidean(a, n)

    return u % n
