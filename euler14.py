# Longest Collatz sequence
# Problem 14

# The following iterative sequence is defined for the set of positive integers:
#      n → n/2 (n is even)
#      n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
#      13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

import time
start = time.time()

def collatz_length(n, cache):
    if n in cache:
        return cache[n]
    chain = []
    cached_length = 0
    x = n
    while True:
        if x in cache:
            cached_length = cache[x]
            break
        chain.append(x)
        if x == 1:
            break
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3*x + 1

    c = cached_length
    for i in chain[::-1]:
        c += 1
        cache[i] = c
        
    return c

cache = {}
result = 0
result_chain_length = 0

for i in range(1,1000000):
    collatz = collatz_length(i, cache)
    if collatz > result_chain_length:
        print('Maximal result found: {} gives chain of {}'.format(i, collatz))
        result = i
        result_chain_length = collatz

print ('Result is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))


# SAW THE FOLLOWING ELEGANT SOLUTION ON FORUM AFTER SOLVING
#lim = 1000000; chain = {1:1}; maxL = 1
#
#def collatz(i):
#   if i not in chain: chain[i] = 1 + collatz(i/2 if i%2==0 else 3*i+1)
#   return chain[i]
#for i in range(1, lim): maxL = i if (collatz(i) > chain[maxL]) else maxL 
#print "collatz chain of {} is {} terms long.".format(maxL, collatz(maxL))
