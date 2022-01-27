pub fn primes_under_n(n: i32) -> Vec<i32> {
    let mut primes = Vec::new();
    for i in 1..n {
        let mut bool = true;
        //println!("{}",i.to_string());
        let upper = ((i as f64).sqrt().trunc() + 1.0) as i32;
        //println!("upper bound is {}",upper.to_string());
        for j in 2..upper {
            //println!("{}",(i%j).to_string());
            if i % j == 0 {
                bool = false;
                break;
            }
        }
        if bool == true {
            //println!("{} is a prime number",i.to_string());
            primes.push(i);
        }
    }
    //print_int_vec(primes);
    return primes;
}
