# calculates binary number of a base-10 number n
def binary(n: int):
    empty = ""

    while True:
        empty += str(n % 2)
        n //= 2

        if n // 2 == 0:
            empty += str(n)
            break

    return empty[::-1]

# calculate a**b mod p
def successive_squaring(a: int, b: int, p: int):
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
