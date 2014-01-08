# Coin sums
# Problem 31

# In England the currency is made up of pound, £, and pence, p, and there are
# eight coins in general circulation:
#
#      1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#
# It is possible to make £2 in the following way:
#
#      1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?

import time

start = time.time()

result= 0

all_coins = [1, 2, 5, 10, 20, 50, 100, 200]

def ways_of_making(n, coins, depth=0, debug=False):
    indent=' '*depth
    if debug: print(indent,'n={}, coins={}'.format(n,coins))
    if n == 0 or len(coins) == 1:
        if debug: print(indent,'returning default of 1')
        return 1
    ways = 0
    top_coin = sorted(coins)[-1]
    max_uses = n // top_coin
    if debug: print(indent,'max_uses={}'.format(max_uses))
    for i in range(max_uses+1):
        ways += ways_of_making(n - i*top_coin, coins[:-1], depth+1, debug)
    if debug: print(indent,'returning', ways)
    return ways

# for i in range(1,201):
#     ways = ways_of_making(i,all_coins)
#     print('There {} {} way{} of making {}p'.format(
#         'is' if ways == 1 else 'are',
#         ways,
#         '' if ways == 1 else 's',
#         i
#     ))
    
result = ways_of_making(200,all_coins)
print('Result is {}'.format(result))

end = time.time()
print ('Time taken: {:.6f}s'.format(end - start))
