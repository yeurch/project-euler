# Digit Canceling Fractions
# Problem 33

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
# is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less
# than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

import time
from yeurch.rational import Rational

start = time.time()
	    
def prod(factors):
    result = 1
    for f in factors:
        result *= f
    return result

def is_weird(numerator,denominator):
    if numerator % 10 == 0 and denominator % 10 == 0:
        return False  # eliminate trivial case where both divide by 10
                    
    numerator_digits = [int(x) for x in str(numerator)]
    denominator_digits = [int(x) for x in str(denominator)]
                    
    if numerator_digits == denominator_digits[::-1]:
        return False # eliminate trivial case where both have same digits

    if numerator_digits[0] in denominator_digits:
        denominator_digits.remove(numerator_digits[0])
        numerator_digits.pop(0)
    elif numerator_digits[1] in denominator_digits:
        denominator_digits.remove(numerator_digits[1])
        numerator_digits.pop(1)

    if len(numerator_digits) == 1 and denominator_digits[0] != 0:
        return Rational(numerator, denominator) == Rational(numerator_digits[0], denominator_digits[0])
    return False
    
fractions = [(n,d) for n in range(10,100) for d in range(n+1,100) if is_weird(n,d)]

product = Rational(prod([x[0] for x in fractions]), prod([x[1] for x in fractions]))
result = product.d

print('Fractions:', fractions)

print ('Solution is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
