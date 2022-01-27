use warp::Filter;
mod primes;
#[tokio::main]
async fn main() {
    let hello = warp::path!("primes" / i32)
        .map(|n:i32|{
            let l = primes::primes_under_n(n);
            warp::reply::json(&l)
        });
    warp::serve(hello)
        .run(([127,0,0,1],3030))
        .await;
}
