import uvicorn
from typing import List
from fastapi import FastAPI
from primes import get_primes_below_n


app = FastAPI()

@app.get('/primes/{n}')
async def primes(n:int = None):
    '''
    A GET endpoint that returns primes below an integer, Invalid if n < 2, and a message if there is no param
    '''
    #logger.info(f'n is {n}')
    if n < 2 or n == None:
        return {'primes':'Invalid Number'}
    else:
        primes = get_primes_below_n(n)
        return {'primes':primes}

if __name__ == "__main__":
    uvicorn.run('main:app',host="0.0.0.0",port=8000,reload=True)


