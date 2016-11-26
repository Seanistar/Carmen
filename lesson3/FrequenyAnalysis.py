# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible 
# algorithm or even language of the clear text message, one could perform 
# frequency analysis. This process could be described as simply counting 
# the number of times a certain symbol occurs in the given text. 
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains 
# the lowercase letters a-z. 
# As output you should return a list of the normalized frequency 
# for each of the letters a-z. 
# The normalized frequency is simply the number of occurrences, i, 
# divided by the total number of characters in the message, n.

from collections import defaultdict, Counter
def freq_analysis(message):
    ## using mapReduce
    collector = defaultdict(list)
    for char, count in mapper(message):
        collector[char].append(count)

    freq_list = { output[0]:output[1]
                  for char, count in collector.iteritems()
                  for output in reducer(char, count) }

    ## using Counter class
    #freq_list = Counter(message)
    
    result = []
    for n in range(ord('a'), ord('z')+1):
        if chr(n) in freq_list:
            value = freq_list[chr(n)]
            result.append(float(value)/len(message))
        else: result.append(0.0)
    
    return result

def mapper(inputs):
    for char in inputs:
        yield (char, 1)

def reducer(char, counts):
    yield (char, sum(counts))


#Tests

print freq_analysis("abcd")
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis("adca")
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]
