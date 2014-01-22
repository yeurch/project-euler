def prime_sieve(n):
    total = 0
    primes = set({})
    for i in range(2,n+1):
        primes.add(i) # initialise our set of potential primes
    for p in range(2,n+1):
        if p in primes:
            if p > n**0.5:  # if we're over n**0.5 there must already by a smaller prime factor, so will arleady be crossed out
                break
            for j in range(p*p, n+1, p): # as above, we can start at p^2 as otherwise there must already by a smaller prime factor
                if j in primes:
                    primes.remove(j)
    return primes

def prime_iterator():
    current = 1
    while True:
        current += 1
        while True:
            for i in range(2, current // 2 + 1):
                if current % i == 0:
                    current += 1
                    break
            else:
                break
        yield current

def is_prime(n):
	if n < 1:
		return False
	max_check = int(n**0.5)+1
	i = 2
	while True:
		if n % i == 0:
			return False
		i += 1
		if i > max_check:
			break
	return True
		
def prime_factors(n):
    if n < 1:
        raise ValueError('fact() argument should be >= 1')
    if n == 1:
        return []  # special case
    res = []
    # iterate over all even numbers first.
    while n % 2 == 0:
        res.append(2)
        n //= 2
    # try odd numbers up to sqrt(n)
    limit = (n+1)**0.5
    i = 3
    while i <= limit:
        if n % i == 0:
            res.append(i)
            n //= i
            limit = (n+i)**0.5
        else:
            i += 2
    if n != 1:
        res.append(n)
    return res