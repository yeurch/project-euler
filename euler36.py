# Double-base palindromes
# Problem 36

# The decimal number, 585 = 10010010012 (binary), is palindromic in both
# bases.
#
# Find the sum of all numbers, less than one million, which are palindromic
# in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include
# leading zeros.)

import time

start = time.time()

result = sum([n for n in range(1,1000000) if str(n) == str(n)[::-1] and bin(n)[2:] == bin(n)[2:][::-1]])

print('Result is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
