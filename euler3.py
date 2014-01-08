# LARGEST PRIME FACTOR
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

from yeurch.primes import prime_iterator


number = 600851475143
primefactors = set({})

result = 0
for p in prime_iterator():
    while number % p == 0:
        number = number // p
        primefactors.add(p)
        result = p
    if p > number:
        break

print ('Solution is {0}'.format(result))

