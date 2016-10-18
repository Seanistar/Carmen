def fibonacci(n):
    current, after = 0, 1
    for i in range(0, n):
        current, after = after, current + after
    return current

def factorial(n):
    if n == 1: return 1
    else: return n * factorial(n-1)

# exp(x) (x^2 / n!)
def f_exp(x, n):
    s = 1.0
    if n == 1: return x+1
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

def f_factorial(n):
    f = 1.0
    while n  > 0:
        f *= n
        n -= 1
    return f



t2 = {'FtoK':lambda deg_f:273+(deg_f-32)*5/9, 'CtoK':lambda deg_c:273+deg_c}

def four():
    x = 0
    while x < 4:
        print('in generator, x =', x)
        yield x
        x += 1

def decorate(func):
    def wrapper_func(*args):
        return func(*args)
    return wrapper_func

class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)
class Talker:
    def talk(self):
        print('value is : ', self.value)
class TalkingCalculator(Calculator, Talker):
    pass


#print fibonacci(33)
#print factorial(5)
#t2['FtoK'](32)
#3 in four()
#@decorate
#def mufunction(parameter):
#    print(parameter)
#tc = TalkingCalculator()
#tc.calculate('10 * 2 + 3')
#tc.talk()
