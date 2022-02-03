from typing import List


def get_primes_below_n(n:int) -> List[int]:
    '''
    Return a list of the primes below an integer n
    '''
    primes = []
    for i in range(1,n):
        prime = True
        for j in range(2,int(i**0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            primes.append(i)
    return primes
