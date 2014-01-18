# Self powers
# Problem 48

# The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
#
# Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

import time

start = time.time()

result = str(sum([x**x for x in range(1,1001)]))[-10:]

print('Result is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
