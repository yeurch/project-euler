# Consecutive prime sum
# Problem 50

# The prime 41, can be written as the sum of six consecutive primes:
#
#           41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime below
# one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a
# prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?

import time
from yeurch.primes import prime_sieve

start = time.time()

primes = tuple(prime_sieve(1000000))
print (len(primes))

result = 21 # Existing solution, given in the question

for i in range(len(primes)):
    l = result + 1
    while True:
        if i + l > len(primes):
            break
        s = sum(primes[i:i+l])
        if s > 1000000:
            break
        if s in primes:
            result = l
            print('Chain of {} primes yields {}'.format(l, s))
        l += 1

result = 0

print('Solution is', result)
print('Time taken: {0:.3f}s'.format(time.time() - start))
