# MULTIPLES OF 3 AND 5
#
# If we list all the natural numbers below 10 that are multiples of 3
# or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

factors = (3,5)
s = set({})

for factor in factors:
    x = factor
    while x < 1000:
        s.add(x)
        x += factor
total = 0
for multiple in s:
    total += multiple

print ('Solution is {}'.format(total))
