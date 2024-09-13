def fib_2(n):
    if n == 0:
        return (1,0)
    if n == 1:
        return (0,1)
    if n%2 == 0 :
        fn,fn2 = fib_2(n//2)
        return (fn*fn+fn2*fn2,2*fn*fn2+fn2*fn2)
    else:
        fn,fn2 = fib_2(n-1)
        return (fn2,fn+fn2)

# Tests
assert fib_2(0) == (1, 0)
assert fib_2(1) == (0, 1)
assert fib_2(2) == (1, 1)
assert fib_2(3) == (1, 2)
assert fib_2(9) == (21, 34)
assert fib_2(4) == (2, 3)

print(fib_2(50)[1]) 