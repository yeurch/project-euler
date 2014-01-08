# SUM SQUARE DIFFERENCE
#
# The sum of the squares of the first ten natural numbers is,
#       12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#       (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

max_int = 100

sum = 0
sq_sum = 0

for i in range(1, max_int + 1):
    sum += i
    sq_sum += i ** 2

result = sum ** 2 - sq_sum


print ('Sum of square difference is {}'.format(result))
