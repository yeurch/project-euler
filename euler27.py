# Quadratic primes
# Problem 27

# Euler discovered the remarkable quadratic formula:
#      n² + n + 41
# It turns out that the formula will produce 40 primes for the consecutive
# values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41
# is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly
# divisible by 41.
#
# The incredible formula  n² − 79n + 1601 was discovered, which produces 80
# primes for the consecutive values n = 0 to 79. The product of the
# coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#     n² + an + b, where |a| < 1000 and |b| < 1000
# where |n| is the modulus/absolute value of n
#     e.g. |11| = 11 and |−4| = 4
#
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.

import time
from yeurch.primes import prime_sieve, is_prime

start = time.time()

# We can factorize to n(n+a) + b

# So when n = 0, b must be prime, so we only need consider prime values for b
# We'll brute force for -1000 < a < 1000 and 0 < b < 1000 and b is prime
# Given our formula and restrictions, the maximum result is dependent on n,
# if we assume that we're going to have no more then 1000 consecutive primes,
# then the maximum value is 1000*(1000+1000)+1000, or 2001000. We'll do a
# prime_sieve to get these values. If my some chance, we exceed it, we'll use
# is_prime to check.

primes = prime_sieve(1000)
result = 0
max_sequence = 0

for a in range(-999,1000):
    for b in primes:
        n = 0
        fn_result = n*(n+a)+b
        while (fn_result < 1000 and (fn_result in primes)) or is_prime(fn_result):
            n += 1
            fn_result = n*(n+a)+b
        if n > max_sequence:
            result = a*b
            max_sequence = n
            print ('Found a sequence of length {}. (a,b)=({},{})'.format(n,a,b))

print ('Solution is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
