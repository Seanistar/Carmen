# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition_bad(items):
    rep, prev = {}, None
    for item in items:
        if item not in rep:
            rep[item] = 1; prev = item
        else:
            if not prev or prev != item:
                prev = item; rep[item] = 0
            else: # prev is equal to item
                rep[item] += 1
                
    return biggest_value(rep)

def biggest_value(dic):
    BK, BV = (None, None)
    for key, value in dic.iteritems():
        if not BV or value > BV:
            BK, BV = key, value
    return BK

def longest_repetition(items):
    best, best_length, current, current_length = None, 0, None, 0
    for item in items:
        if not current or current != item:
            current = item; current_length = 1
        else: # current is equal to item
            current_length += 1
            
        if not best or current_length > best_length:
            best_length = current_length
            best = current
                
    return best

#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

print longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])
# [2, 2]
