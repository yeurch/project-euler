# Square digit chains
# Problem 92

# A number chain is created by continuously adding the square of the digits
# in a number to form a new number until it has been seen before.
#
# For example,
#
#     44 → 32 → 13 → 10 → 1 → 1
#     85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in an
# endless loop. What is most amazing is that EVERY starting number will
# eventually arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?

import time
from yeurch.primes import prime_sieve

start = time.time()

def square_chain(n):
    seen = []
    yield n
    n = sum([int(x)**2 for x in str(n)])
    while n not in seen:
        yield n
        seen.append(n)
        n = sum([int(x)**2 for x in str(n)])
    yield n

def arrives_at(n):
    chain = [x for x in square_chain(n)]
    return 89 if 89 in chain else 1

    
# For 10,000,000, the maximum square sum will be 7*81 = 567
# So if we calculate every chain < 568, then we can do a
# lookup for each number trivially.

ends_at = [arrives_at(x) for x in range(568)]
result = 0
for i in range(10000000):
    if i % 1000000 == 0: print('Processing',i)
    square_sum = sum([int(x)**2 for x in str(i)])
    if ends_at[square_sum] == 89:
        result += 1

# Not particualarly happy with this. Took 59 seconds.

# We could definitely improve by looking at permutations
# of digits, as each permutation of the same digits will
# end up at the same target.

print('Result is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
