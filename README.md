# Fibonacci of large numbers

This repo contains using an algorithm to find the nth fibonacci number using Python and Go, where n is really large.

I did three different experiments:

1. Python
2. Go with standard "math/big" library
3. Go with GMP library (the [GNU Multiple Precision Arithmetic library](https://gmplib.org/))

I noticed that with this particular algorithm, that when using n = 30000000 (or, 30 million), that Python took the longest to calculate and print the number. It took almost 9 minutes to run on my PC.

However, with the Go using the standard "math/big" library, it took 6.845 seconds. Then replacing the "math/big" library with the GMP library, I brought that number down to 1.751 seconds.



To use the GMP library, I did the following:

1. Download the *.tar.lz file from the GMP official website: https://gmplib.org/.
    * In my case, I used `gmp-6.2.1.tar.lz`
2. Extract it by doing the following on Linux:

> sudo apt install lzip
> sudo apt install m4
> tar --lzip -xvf gmp
> cd gmp-6.2.1
> ./configure
> make
> make install

3. Install [this Go wrapper](https://github.com/ncw/gmp) for the GMP library.
> go get github.com/ncw/gmp
> cd /path/to/current/working/directory
> nano main.go
> [Replace `import "math/big"` with `import big "github.com/ncw/gmp"`]
> go mod init main
> go mod tidy
> go build main.go

4. Run it!

> time ./main

