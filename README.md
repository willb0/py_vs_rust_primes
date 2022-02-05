# py_vs_rust_primes
This repo is an initial exploration of rust for me. I read this [article](https://cantortrading.fi/rust_decimal_str/) on HackerNews, and it caught my interest. As a mainly data science focused person, I don't have too much experience with stuff like rust, systems programming, and tail calls, but that article was enough for me to see if I could speed up some of my FastAPI apps by implementing them in rust.

## Instructions
I will be using the [apache benchmark tool](https://httpd.apache.org/docs/2.4/programs/ab.html) to compare these two API's
Eventually, I'll make a run.sh script that performs all these steps and compares the two, but for now I'll just write setup for each API as I build them

Clone repo: `git clone https://github.com/willb0/py_vs_rust_primes.git`

### Docker-compose
If you have docker-compose set up, you can clone the repo and simply type: 
`docker-compose build && docker-compose up`
You'll have FastAPI on 0.0.0.0:80 and warp(rust) on 0.0.0.0:3030

The both have one endpoint: GET /primes/{n}, where n is an integer.
If n is less than 2, it will return 'Invalid Number'(still working on validation in rust). Otherwise, it will return a list of primes up to n
 
ex: `curl http://0.0.0.0:80/primes/10  = {"primes":[1,2,3,5,7]}`

These are the instructions to setup these separate APIs locally:

### Python (FastAPI) 
Docker: 
```
cd fastapi_primes
docker build -t fastapi_primes .
docker run -d -p 80:80 fastapi_primes
```

Normal python 
```
cd fastapi_primes
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 80]
```

### Rust (warp)
Docker: 
```
cd rust_primes
docker build -t rust_primes .
docker run -d -p 3030:3030 rust_primes
```

Normal rust: 
This assumes you have the cargo toolchain installed

```
cd rust_primes
cargo build && cargo run
```



