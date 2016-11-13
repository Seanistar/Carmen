# n ** 0.5
def f_sqrt(n):
    g = 1.0 # guess
    while abs(n - g * g) > .0001:
        g = g - (g * g - n) / (2 * g)
    return g

# n ** 0.5 with tolerance
def f_sqrt2(n, t):
    g = 1.0
    while abs(n - g * g) > t: # tolerance
        g = g - (g * g - n) / (2 * g)
    return g

# n ** 2
def f_power(x, n = 0):
    if n == 0: return 1
    p = 1
    while n > 0:
        p *= x; n -= 1
    return p

# n!
def f_factorial(n = 1):
    if n == 1: return 1 # basis case
    else: return n * f_factorial(n-1)

# fib using yield
def f_fibonacci(n):
    c, a = 0, 1 # current, after
    for i in range(n):
        yield a
        c, a = a, c + a
    #return c

fibStored = {}
# fibonacci by memoization version
def m_fib(n): 
    if n in fibStored:
        return fibStore[n]
    elif n == 0 or n == 1:
        return 1
    else:
        result = m_fib(n-2) + m_fib(n-1)
        fibStored[n] = result
        return result

# exp(x) (x**2 / n!)
def f_exp(x, n = 1):
    if n == 1: return x+1
    s = 1.0
    while n > 0:
        s += (f_power(x,n) / f_factorial(n)); n -= 1
    return s

# collatz algorithm
def f_collatz(n):
    yield n
    while n != 1:
        if n % 2 == 0: n = n / 2
        else: n = 3 * n + 1
        yield n
