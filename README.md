# py_vs_rust_primes
This repo is an initial exploration of rust for me. I read this [article](https://cantortrading.fi/rust_decimal_str/) on HackerNews, and it caught my interest. As a mainly data science focused person, I don't have too much experience with stuff like rust, systems programming, and tail calls, but that article was enough for me to see if I could speed up some of my FastAPI apps by implementing them in rust.

## Instructions
I will be using the [apache benchmark tool](https://httpd.apache.org/docs/2.4/programs/ab.html) to compare these two API's
Eventually, I'll make a run.sh script that performs all these steps and compares the two, but for now I'll just write setup for each API as I build them

Clone repo: `git clone https://github.com/willb0/py_vs_rust_primes.git`
### Python (FastAPI) 
```
cd fastapi_primes
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python main.py
```
The FastAPI app has one endpoint: GET /primes/{n}, where n is an integer.

If n is less than 2, it will return 'Invalid Number'. Otherwise, it will return a list of primes up to n

ex: `curl http://0.0.0.0:8000/primes/10  = {"primes":[1,2,3,5,7]}`

### Rust (warp)
This assumes you have the cargo toolchain installed
```
cd rust_primes
cargo build && cargo run
```



