# Generates primes up to a limit employing Sieve of Eratosthenes
def primes(limit):
    n = limit+1  # get primes up to limit n
    p = []       # list of primes p
    m = set()    # set of (not prime) multiples m
    for i in range(2, n):  # for i from 2 to n-1
        if i in m:         # if i is in the set m, it's a multiple and not prime
            continue       # so skip
        p.append(i)        # since i is not a multiple, it must be prime, store it
        for j in range(i*2, n, i):  # for all multiples of the prime i
            m.add(j)                # store each multiple (cannot be prime) in set m
    return p                        # return primes up to n

# command line interface
while(1):
    print(primes(int(input('Find primes up to: '))))
