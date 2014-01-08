# 10001ST PRIME
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
# What is the 10,001st prime number?

from yeurch.primes import prime_iterator

counter = 0

for p in prime_iterator():
    counter += 1
    if counter == 10001:
        print ("Solution is {0}".format(p))
        break
