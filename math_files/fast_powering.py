def binary(n):
    empty = ""

    while True:
        empty += str(n % 2)
        n //= 2

        if n // 2 == 0:
            empty += str(n)
            break

    return empty[::-1]


def successive_squaring(a, b, p):
    # calculate a**b mod p
    str_b = binary(b)
    product = 1
    remainder = 1

    # reverse of binary(b)
    for idx, digit in enumerate(str_b[::-1]):
        digit = int(digit)

        # base case
        if idx == 0:
            remainder = a % p
            product *= remainder ** digit
        else:
            remainder = remainder ** 2 % p
            product *= remainder ** digit
            product %= p

    return product
