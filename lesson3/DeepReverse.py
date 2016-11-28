# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

def deep_reverse_bad(inputs):
    if not is_list(inputs):
        return inputs
    
    n, res = len(inputs), inputs[:]
    for i in range(n/2):
        res[i], res[(n-1)-i] = deep_reverse(inputs[(n-1)-i]), deep_reverse(inputs[i])
        if (i+1 == n/2) and (n%2): # odd median
            res[i+1] = deep_reverse(inputs[i+1])
                    
    return res

def deep_reverse(p):
    if is_list(p):
        result = []
        for i in range(len(p) - 1, -1, -1):
            result.append(deep_reverse(p[i]))
        return result
    else:
        return p
    
#For example,
b = [1, [2, 3], [4, 5]]
print deep_reverse(b)

d = [1, 2, 3, 4]
print deep_reverse(d)

p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
#print p
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2, 3], 4, [5, 6]]
print deep_reverse(q)
#>>> [[6, 5], 4, [3, 2], 1]
#print q
#>>> [1, [2, 3], 4, [5, 6]]
