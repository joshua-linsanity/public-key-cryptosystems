# public-key-cryptosystems

For cryptography programs I created during Carnegie Mellon's SAMS program.

## SUGGESTIONS

1. RSA has faster encryption than Elgamal. However, Elgamal has faster decryption than RSA.
2. If time is an issue, Fermat will run much faster than Miller-Rabin.
    - If Fermat is chosen, primes with hundreds of digits can be used.
        - Fermat's primality test can also be run several times (e.g., 40) without a problem.
    - If Miller-Rabin is chosen, primes with more than 5 to 10 digits will crash the computer.
        - Miller-Rabin's primality test can only be run a few times (from tests on my computer, about 5).
        - However, each Miller-Rabin test gives better odds than Fermat that the input number is prime.
3. Short message (<10 words) work best. For these, 10^2 digits is probably the largest order of magnitude for primes (with Fermat).
4. All tuples need to be copy-pasted and sent to the other person. These will be highlighted in red.


## Handouts

../theoretical contains handouts (source: Dr. Alisa Nu'man from Spelman and Dr. Elisa Bellah from CMU) that explain the concepts behind each. 
