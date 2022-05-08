def fib( n ):
    left,    right   = 1, 1
    helper1, helper2 = 0, 0

    binary = bin( n )[2:]
    for i in range( 1, len( binary ) ):
        helper1  = left * ( 2 * right - left )
        helper2  = right * right + left * left

        if binary[ i ] == '0':
            left, right = helper1, helper2
        else:
            left, right = helper2, helper1 + helper2

    return left

if __name__ == '__main__':
    nth_fib_num = 3 * ( 10 ** 7 )
    print( fib( nth_fib_num ) )
