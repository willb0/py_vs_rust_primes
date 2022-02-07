import streamlit as st
import pandas as pd
import subprocess
import os
import altair

BASE_URL = "http://0.0.0.0:{}/primes/{}"
RUST_OUT = os.getcwd() + '/data/rustout.csv'
PY_OUT = os.getcwd() + '/data/pyout.csv'


st.title('Warp(rust) vs FastAPI(python) prime generator comparison')

with st.form(key='info'):
    num_reqs = int(st.sidebar.slider('Number of requests',0,100000))
    num_conc = int(st.sidebar.slider('Number of concurrent connections',0,100))
    num_primes = int(st.sidebar.slider('Calculate primes below this number',0,9999))
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    rust_str = f'ab -k -c {num_conc} -n {num_reqs} -e {RUST_OUT} {BASE_URL.format(3030,num_primes)}'
    py_str = f'ab -k -c {num_conc} -n {num_reqs} -e {PY_OUT} {BASE_URL.format(80,num_primes)}'
    print(rust_str,py_str)
    subprocess.run(rust_str.split())
    subprocess.run(py_str.split())
    rust_df = pd.read_csv('data/rustout.csv')
    py_df = pd.read_csv('data/pyout.csv')
    print(rust_df.columns)
    st.altair_chart(altair.Chart(rust_df).mark_line().encode(x='Percentage served',y='Time in ms'))
    st.altair_chart(altair.Chart(py_df).mark_line().encode(x='Percentage served',y='Time in ms'))
