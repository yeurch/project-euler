# Pandigital prime
# Problem 41

# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
# also prime.
#
# What is the largest n-digit pandigital prime that exists?

import time
from yeurch.primes import is_prime


def swap(items, a, b):
	items[a], items[b] = items[b], items[a]

def heap_permute(result, items, n):
    if n == 1:
        result.append(int(''.join(items)))
    else:
        for i in range(n):
            heap_permute(result, items, n-1)
            if n % 2 == 1:
                swap(items, 0, n-1)
            else:
                swap(items, i, n-1)

if __name__ == '__main__':
    start = time.time()
    
    # Note that 9 and 8 digit pangigitals can't be prime
    #
    # That's because of the divisibility rule of 3.
    # A number is divisible by 3 if, and only if, the sum of its digits is
    # divisible by 3.
    #    1+2+3+4+5+6+7+8+9 = 45, and 45 is divisible by 3
    #    1+2+3+4+5+6+7+8 = 36, and 36 is divisible by 3
    
    for num_digits in range(7,0,-1):
        permutations = []
        items = [str(x) for x in range(1,num_digits+1)]
        heap_permute(permutations, items, num_digits)
        permutations = sorted(permutations)[::-1]
        
        max_prime = 0
        for x in permutations:
            if is_prime(x):
                max_prime = x
                break
        if max_prime > 0:
            print ('Maximum pandigital prime is', max_prime)
            break
        else:
            print ('No prime pandigitals of length {} found'.format(num_digits))
    
    print('Time taken was {:.3f}s'.format(time.time() - start))
