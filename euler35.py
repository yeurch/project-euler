# Circular Primes
# Problem 35

# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100:
#     2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

import time
from yeurch.primes import prime_sieve

start = time.time()

primes = prime_sieve(1000000)

def cycles(p):
    sp = str(p)
    for i in range(len(sp)):
        yield int(sp[i:]+sp[:i])

result = 0
for i in range(1000000):
    is_circular_prime = True
    for c in cycles(i):
        if c not in primes:
            is_circular_prime = False
            break
    if is_circular_prime:
        result += 1


print ('Solution is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
