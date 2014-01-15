# Convergents of e
# Problem 65

# The square root of 2 can be written as an infinite continued fraction.
#   √2 = 1 + (1 / (2 + 1 / (2 + (1 / 2 + (1 / 2 + ... )))))	
#
# The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates
# that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].
#
# It turns out that the sequence of partial values of continued fractions for
# square roots provide the best rational approximations. Let us consider the
# convergents for √2.
#
#    1 + 1/2                         = 3/2	
#    1 + 1/(2 + 1/2)                 = 7/5
#    1 + 1/(2 + 1/(2 + 1/2))         = 17/12
#    1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29
#
# Hence the sequence of the first ten convergents for √2 are:
#   1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
#
# What is most surprising is that the important mathematical constant,
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
#
# The first ten terms in the sequence of convergents for e are:
#    2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
#
# The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.
#
# Find the sum of digits in the numerator of the 100th convergent of the
# continued fraction for e.

import time
from math import exp
from yeurch.rational import Rational

start = time.time()

result = 0

def calculate_series(a,seq,max_depth=10,depth=0):
	# print ('Entering depth', depth)
	if depth == 0:
		result = Rational(a, 1) + calculate_series(a,seq,max_depth,1)
	elif depth >= max_depth:
		b = seq[(depth-1) % len(seq)]
		#result = 1 / b
		result = Rational(1, b)
	else:
		b = seq[(depth-1) % len(seq)]
		#result = 1 / (b + calculate_series(a,seq,max_depth,depth+1))
		result = Rational(1,1) /  (Rational(b,1) + calculate_series(a,seq,max_depth,depth+1))
	# print('Returning from depth {} with value {}.'.format(depth, result))
	return result
	
seq = []
for x in range(1,35):
	seq.extend([1,2*x,1])

result = sum([int(l) for l in str(calculate_series(2,seq,99).n)])

print ('Solution is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
