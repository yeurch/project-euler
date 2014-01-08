# Lexicographic permutations
# Problem 24
#
# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
#        012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import time
from math import factorial

start = time.time()

target = 1000000
num_digits = 10
result = ''

digits = [i for i in range(num_digits)]

for i in range(num_digits):
    digit_index = (target-1) // factorial(num_digits - (i+1)) % len(digits)
    result += str(digits[digit_index])
    digits.pop(digit_index)

print ('Solution is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
