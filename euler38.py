# Pandigital multiples
# Problem 38

# Take the number 192 and multiply it by each of 1, 2, and 3:
#
#   192 × 1 = 192
#   192 × 2 = 384
#   192 × 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We
# will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
# and 5, giving the pandigital, 918273645, which is the concatenated product
# of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as
# the concatenated product of an integer with (1,2, ... , n) where n > 1?

import time

start = time.time()

def is_pandigital(s):
    if len(s) != 9:
        return False
    for x in range(1,10):
        if not str(x) in s:
            return False
    return True

candidates = []
for x in range(1,10000):
    concat = ''
    for i in range(1,10):
        concat += str(x*i)
        if is_pandigital(concat):
            candidates.append(int(concat))
            break
        if len(concat) > 9:
            break

result = max(candidates)
print('Result is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
