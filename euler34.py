# Digit Canceling Fractions
# Problem 33

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial
# of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import time, math

start = time.time()

factorials = [math.factorial(x) for x in range(10)]

def is_digit_factorial(x):
    return x == sum([factorials[int(i)] for i in str(x)])

n = 1
while 10**n-1 < n*factorials[9]:
    n += 1
max_num = n * factorials[9]

result = sum([x for x in range(10,max_num+1) if is_digit_factorial(x)])

print ('Solution is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
