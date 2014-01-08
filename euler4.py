# LARGEST PALINDROME PRODUCT
#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(number):
    s = str(number)
    return s == s[::-1]

result = 0

max_num = 999
current = max_num

while current > 0:
    current2 = max_num
    while current2 >= 0:
        product = current * current2
        if product > result and is_palindrome(product):
            result = product
        current2 -= 1
    current -= 1

print ('Largest palindrome is {}'.format(result))
