# Truncatable primes
# Problem 37

# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain
# prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
# right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from
# left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import time

start = time.time()

def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, 2*i if i > 2 else 2):     # Mark factors non-prime
                a[n] = False

max_length = 7 # Trial and error ... increased until we got no more answers
all_primes = []
primes = {}
for p in primes_sieve(10**max_length):
    p_len = len(str(p))
    if not p_len in primes: primes[p_len] = []
    primes[p_len].append(p)
    all_primes.append(p)

candidates = primes[1]
for l in range(2,max_length+1):
    candidates.extend([x for x in primes[l] if int(str(x)[:-1]) in candidates])

print(candidates)
for c in [x for x in candidates if x >= 10]:
    for i in range(1,len(str(c))):
        if int(str(c)[i:]) not in all_primes:
            candidates.remove(c)
            break

candidates = [c for c in candidates if c >= 10] # remove single-digit primes
print(candidates)

result = sum(candidates)
print('Result is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
