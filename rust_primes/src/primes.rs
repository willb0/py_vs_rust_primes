pub fn primes_under_n(n: i32) -> Vec<i32> {
    let mut primes = Vec::new();
    for i in 1..n {
        let mut bool = true;
        let upper = ((i as f64).sqrt().trunc() + 1.0) as i32;
        for j in 2..upper {
            if i % j == 0 {
                bool = false;
                break;
            }
        }
        if bool == true {

            primes.push(i);
        }
    }
    return primes;
}
