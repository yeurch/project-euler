# Champernowne's constant
# Problem 40

# An irrational decimal fraction is created by concatenating the positive
# integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of
# the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

import time

start = time.time()

s = ''
i = 1
while len(s) < 1000000:
    s += str(i)
    i += 1

result = 1
for i in range(0,6):
    result *= int(s[10**i-1])


print('Result is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
