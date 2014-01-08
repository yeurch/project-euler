# Goldbach's other conjecture
# Problem 46

# It was proposed by Christian Goldbach that every odd composite number can
# be written as the sum of a prime and twice a square.
#
#     9 = 7 + 2×12
#     15 = 7 + 2×22
#     21 = 3 + 2×32
#     25 = 7 + 2×32
#     27 = 19 + 2×22
#     33 = 31 + 2×12
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of
# a prime and twice a square?

import time
from yeurch.primes import prime_sieve

start = time.time()

max_prime = 100000
max_square = 500

primes = prime_sieve(max_prime)
double_squares = [2*x**2 for x in range(1,max_square)]
odd_composites = [x for x in range(3,max_prime,2) if x not in primes]

result = 0
for i in odd_composites:
    ok = False
    for s in double_squares:
        if i - s  in primes:
            ok = True
            break
    if not ok:
        result = i
        break

if result == 0:
    print('Could not find a solution')
else:
    print('Result is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
