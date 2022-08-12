# public-key-cryptosystems
For cryptography programs I created during Carnegie Mellon's SAMS program.

SUGGESTIONS
1. RSA has faster encryption than Elgamal. However, Elgamal has faster decryption than RSA.
2. If time is an issue (it is), choose Fermat instead of Miller-Rabin. It's much faster.
    - If Fermat is chosen, primes with hundreds of digits can be used.
        - Fermat's primality test can also be run several times (e.g., 40) without a hitch.
    - If Miller-Rabin is chosen, primes with more than 5 to 10 digits will crash the computer.
        - Miller-Rabin's primality test can only be run a few times (e.g., 5).
        - However, each Miller-Rabin test gives better odds than Fermat that the input number is prime.
3. Short message (<10 words) work best. For these, 100 digit primes are approximately the max (with Fermat).
4. All tuples need to be copy-pasted and sent to the other person. These will be highlighted in red.


# HOW TO USE ELGAMAL
Alice (elgamal_alice.py) starts off. She will be receiving the message.
Part A
1. Alice chooses number of digits in her prime number p.
2. Alice chooses whether to use Fermat (0) or Miller-Rabin (1) primality test.
3. Alice chooses how many times to run the primality test.

Part B
1. Alice receives tuple (c1 c2 case) from Bob, without parentheses.
2. Alice now decodes the secret message.

Bob (elgamal_bob.py) ends. He will be sending the message.
Part A
1. Bob receives tuple (p g A) from Alice, without parentheses.

Part B
1. Bob chooses an arbitrary number k.
2. Bob chooses his secret message.
Part C
1. Bob sends tuple (c1 c2 case) to Alice.
