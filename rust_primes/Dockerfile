# Latest rust image
FROM --platform=linux/arm64 lukemathwalker/cargo-chef:latest-rust-slim-buster AS chef

WORKDIR primes


FROM chef AS planner
COPY . .
RUN cargo chef prepare --recipe-path recipe.json


FROM chef as builder
COPY --from=planner /primes/recipe.json recipe.json

RUN cargo chef cook --release --recipe-path recipe.json

COPY . .
RUN cargo build --release


FROM arm64v8/debian:buster-slim
WORKDIR primes
COPY --from=builder /primes/target/release/rust_primes /usr/local/bin
CMD ["rust_primes"]


