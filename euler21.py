# Amicable numbers
# Problem 21

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
# 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import time
from math import factorial

start = time.time()

divisor_cache = {}
def divisors_of(n):
    if n in divisor_cache:
        return divisor_cache[n]
    result = set([1])

    sqrt = int(n**0.5)
    for i in range(2,sqrt):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    divisor_cache[n] = result
    return result
    
def is_amicable(n):
    divisor_sum = sum(divisors_of(n))
    if divisor_sum == n:
        return False # by definition, amicable pairs need to be different numbers
    return sum(divisors_of(divisor_sum)) == n

result = sum([i for i in range(1,10000) if is_amicable(i)])

print ('Solution is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
