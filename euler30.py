# Digit fifth powers
# Problem 30

# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:
#
#     1634 = 14 + 64 + 34 + 44
#     8208 = 84 + 24 + 04 + 84
#     9474 = 94 + 44 + 74 + 44
#
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth
# powers of their digits.

import time

start = time.time()

result= 0

power = 5
powers = [i**power for i in range(10)]
print ('Powers:', powers)

max_digits = 1
while int('9'*max_digits) < max_digits * powers[9]:
    max_digits += 1
print ('Max digits:', max_digits)

for i in range(2, int('9'*max_digits)+1):
    total = sum([powers[int(x)] for x in str(i)])
    if total == i:
        result += i
        print(i)

print('Result is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
