# Summation of primes
# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import time
from yeurch.primes import prime_sieve

start = time.time()
ceiling = 2000000
summation = 0

for p in prime_sieve(ceiling):
    summation += p

print ('Sum of primes is {}'.format(summation))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
