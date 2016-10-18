# exp(x) (x^2/n!)...

def f_exp(x):
    s, n = 1.0, x
    if n == 1: return n + 1
    while n > 0:
        s += (f_power(x,n) / f_factorial(n))
        n -= 1
    return s
    
def f_power(x, n):
    p = 1.0
    if n == 0: return 1
    while n > 0:
        p *= x
        n -= 1
    return p

# p is a result for dividing x into t
def f_log(x, t):
    p = 1
    while True:
        x = x / t
        if x < t:
            break
        #print x
        p += 1
    return p
        
def f_factorial(n):
    f = 1.0
    while n  > 0:
        f *= n
        n -= 1
    return f

if __name__ == '__main__':
    #x = input('input a number what you want to calculate : ')
    #print 'resutl is : %f'%(f_exp(x))
    #print f_log(52816, 16)
    pass
