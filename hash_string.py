def hash_string(keyword, buckets):
    num = 0
    for i in range(0,len(keyword)):
        num += ord(keyword[i])

    return num % buckets

def test_hash_function(func, keys, size):
    results = [0] * size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w, size)
            results[hv] += 1
            keys_used.append(w)
            
    return results

#print hash_string('udacity',12)
        
