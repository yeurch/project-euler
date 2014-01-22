# Distinct primes factors
# Problem 47

# The first two consecutive numbers to have two distinct prime factors are:
#
#    14 = 2 × 7
#    15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors
# are:
#
#   644 = 2**2 × 7 × 23
#   645 = 3 × 5 × 43
#   646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime
# factors. What is the first of these numbers?

import time
from yeurch.primes import prime_factors

start = time.time()

n = 2
streak = 0
target = 4
while streak < target:
    factors = set(prime_factors(n))
    #print ('{} has {} distinct prime factors'.format(n,len(factors)))
    if len(factors) == target:
        streak += 1
    else:
        streak = 0
    n += 1

result = n - target

print('Solution is', result)
print('Time taken: {0:.3f}s'.format(time.time() - start))
