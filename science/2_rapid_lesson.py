# tip1. finding in a dict faster than in a list such like dict.keys()
word_count = { "machine":3, "statistics":5, "variance":2 }
wc = sorted(word_count.items(), key=lambda (word, count): count, reverse=True)

# tip2. using generator (yield, (for), dict.iteritems())
def lazy_range(n):
    i = 0
    while i < n:
        yield i; i += 1

for i in lazy_range(10):
    pass

lazy_evens_below_20 = (i for i in range(20) if i % 2 == 0)

import re
print all([3 == len(re.split("[ab]", "carbs")),
           "R-D-" == re.sub("[0-9]", "-", "R2D2") ])

# currying, partial function application
def exp(base, power):
    return base**power

from functools import partial
two_to_the = partial(exp, 2) # two_to_the(3) is 8
quare_of = partial(exp, power=2) # square_of(3) is 9

def multiply(x,y): return x*y
def double(x): return 2*x
products = map(multiply, [1,2], [4,5]) # [4, 10]
twice_xs = map(double, [1,2,3,4]) # [2,4,6,8]
list_doubler = partial(map, double) # list_doubler([1,2,3,4]) equal above

# tip3. using enumerator that create a set()
l1 = ['a','b','c']; l2 = [1,2,3]
pairs = zip(l1, l2) # [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

# tip4. an function of higher degree
def add(x, y): return x+y
def doubler_correct(f):
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(add)
g(1,2) # 6
