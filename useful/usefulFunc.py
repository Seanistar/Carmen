
t2 = {'FtoK':lambda deg_f:273+(deg_f-32)*5/9, 'CtoK':lambda deg_c:273+deg_c}

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

def f_reduce(f, seq, init):
    result = init
    for a in seq:
        result = f(result, a)
    return result

def f_map_low(f, seq):
    result = ()
    for a in seq:
        result += (f(a), )
    return result
        
def f_map(f, seq):
    for a in seq:
        yield f(a)

cat = lambda s: f_reduce(lambda x,y: x+y, s, "")

def combinations(n, seq):
    if n == 0:
        yield ()
    elif len(seq) == 0:
        pass
    else:
        first, rest = seq[0], seq[1:]
        for a in combinations(n, rest):
            yield a
        for a in combinations(n-1, rest):
            yield (first,) + a

def concat(X, Y):
    for a in X:
        yield a
    yield " "
    for b in Y:
        yield b

def f_zip(X, Y):
    it = iter(Y)
    for x in X:
        y = next(it, None)
        if y == None:
            return
        else:
            yield (x, y)
            
counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
def find_two_smallest(L):
    if L[0] < L[1]:
        min1, min2 = 0, 1
    else:
        min2, min1 = 1, 0

    for i in range(2, len(L)):
        if L[i] < L[min1]: # is new minimum?
            min2 = min1
            min1 = i
        elif L[i] < L[min2]:
            min2 = i

    return (min1, min2)

def find_smallest(L):
    min_idx, min_value = 0, L[0]
     
    for i in range(1, len(L)):
        if L[i] < min_value:
            min_value = L[i]
            min_idx = i
            
    print "smallest index is: %d and value is : %d" % (min_idx, min_value)

# calculate taking times to find 'v'(value) from the 'L'(list)            
def time_it(f, L, v = None):
    import time
    
    t1 = time.time()
    if v != None: f(v, L)
    else: f(L)
    t2 = time.time()

    return (t2 - t1) * 1000

def binary_search(v, L):
    i, j = 0, len(L) - 1 # left, right margin position

    while i != j + 1:
        m = (i + j) / 2
        if L[m] < v:
            i = m + 1
        else:
            j = m - 1

    if 0 <= i < len(L) and L[i] == v:
        return i
    else:
        return -1
    
#print (time_it(lambda x, y: y.index(x), 5000, range(100001)))
#print find_two_smallest(counts)
#find_smallest(counts)
#print cat(filter(lambda x: x.startswith("John"), ["John host", "Johnhan", " Johon", "John ks"]))
#print tuple(f_map(lambda x: x*x, (2,3,5,7,11)))
#print f_map_low(lambda x: x*x, (2,3,5,7,11))
#print fibonacci(33)
#print factorial(5)
#t2['FtoK'](32)
#tc = TalkingCalculator()
#tc.calculate('10 * 2 + 3')
#tc.talk()
