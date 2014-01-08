# Pandigital products
# Problem 32

# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
# through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.

import time
start = time.time()

products = set()
for i in range(1,100):
    j = i+1
    string_product = str(i) + str(j) + str(i*j)
    while len(string_product) <= 10:
        if len(string_product) == 9:
            ok = True
            for x in range(1,10):
                if not str(x) in string_product:
                    ok = False
                    break
            if ok:
                print('{} x {} = {}'.format(i,j,i*j))
                products.add(i*j)
        j += 1
        string_product = str(i) + str(j) + str(i*j)
print('Result is {}'.format(sum(products)))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
