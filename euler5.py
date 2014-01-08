# SMALLEST MULTIPLE
#
# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

max_divisor = 20

result = max_divisor
while True:
    isOk = True
    for i in range(1,max_divisor):
        if result % i > 0:
            isOk = False
            break
    if isOk:
        break
    result += max_divisor

print ('Smallest multiple is {}'.format(result))
