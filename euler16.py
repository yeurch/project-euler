# Power digit sum
# Problem 16
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

import time

start = time.time()

power = 2**1000
s = str(power)
total = 0
for c in s:
    total += int(c)

print ('Solution is {}'.format(total))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
