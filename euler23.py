# Non-abundant sums
# Problem 23

# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors
# of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
# number.
#
# A number n is called deficient if the sum of its proper divisors is less
# than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the
# sum of two abundant numbers.

import time

start = time.time()

HARD_LIMIT = 28123

divisor_cache = {}
def divisors_of(n):
    if n in divisor_cache:
        return divisor_cache[n]
    result = set([1])

    sqrt = int(n**0.5)
    for i in range(2,sqrt+1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    divisor_cache[n] = result
    return result
    
def is_abundant(n):
    return n < sum(divisors_of(n))

abundants = []
for i in range(12,HARD_LIMIT):
    if is_abundant(i):
        abundants.append(i)

arr = [0] * (HARD_LIMIT + 1)
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        if abundants[i] + abundants[j] > HARD_LIMIT:
            break
        arr[abundants[i] + abundants[j]] = 1

result = sum([x for x in range(1,HARD_LIMIT + 1) if arr[x] == 0])    

print ('Solution is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
