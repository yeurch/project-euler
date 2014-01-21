# Prime permutations
# Problem 49

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms
# are prime, and, (ii) each of the 4-digit numbers are permutations of
# one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
# primes, exhibiting this property, but there is one other 4-digit
# increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in
# this sequence?

import time
from yeurch.primes import prime_sieve

start = time.time()

primes = [x for x in prime_sieve(10000) if x > 1000]

for i in range(len(primes)-1):
    for j in range(i+1, len(primes)):
        if sorted(str(primes[i])) == sorted(str(primes[j])):
            # We have a candidate permutation ... check the next gap up
            next_val = 2 * primes[j] - primes[i]
            if next_val in primes and sorted(str(next_val)) == sorted(str(primes[i])):
                  result = '{}{}{}'.format(primes[i], primes[j], next_val)
                  print(result)

print('Solution is', result)
print('Time taken: {0:.3f}s'.format(time.time() - start))
