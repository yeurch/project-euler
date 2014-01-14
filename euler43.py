# Sub-string divisibility
# Problem 43

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up
# of each of the digits 0 to 9 in some order, but it also has a rather
# interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we
# note the following:
#
#    d2d3d4=406 is divisible by 2
#    d3d4d5=063 is divisible by 3
#    d4d5d6=635 is divisible by 5
#    d5d6d7=357 is divisible by 7
#    d6d7d8=572 is divisible by 11
#    d7d8d9=728 is divisible by 13
#    d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

import time
from itertools import permutations

start = time.time()

primes = [0,3,0,7,11,13,17]
# We zeroed out two and five, as they're dealt with in initial filter below

perms = [''.join(x) for x in permutations('0123456789') if
         x[0] != '0' and
         x[3] in '24680' and
         x[5] in '50']

for n,p in enumerate(primes):
    if p > 0: perms = [x for x in perms if int(x[n+1:n+4]) % p == 0]

result = sum([int(x) for x in perms])
print('Result is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
