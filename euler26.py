# Reciprocal cycles
# Problem 26

# A unit fraction contains 1 in the numerator. The decimal representation of
# the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
# seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring
# cycle in its decimal fraction part.

import time

start = time.time()

result_len = 0
result = 0

for i in range(999,1,-1):
    if i < result_len:
        break
    cycle=[]
    remainder = 1
    while True:
        remainder = (remainder * 10) % i
        if remainder in cycle:
            break
        cycle.append(remainder)
    if len(cycle) > result_len:
        result_len = len(cycle)
        result = i

print ('Solution is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
