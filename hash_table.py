def make_hashtable(nbuckets):
    table = []
    for unsed in range(0, nbuckets):
        table.append([])
    return table

def hash_string(keyword, buckets):
    num = 0
    for i in range(0,len(keyword)):
        num += ord(keyword[i])
    return num % buckets

def make_hashtable_NOT(nbuckets):
    return [[]]*nbuckets

def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]

def hashtable_add(htable, key, value):
    hashtable_get_bucket(htable, key).append([key, value])              
    return htable

def hashtable_lookup(htable, key):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            return entry
    return None

def hashtable_update(htable, key, value):
    result = hashtable_lookup(htable, key)
    if result != None:
        result[1] = value
    else:
        hashtable_add(htable, key, value)
        #hashtable_get_bucket([key, value])
        

table = make_hashtable(5)
hashtable_add(table, 'udacity', 23)
hashtable_add(table, 'audacity', 17)
hashtable_add(table, 'bodacity', 19)
hashtable_add(table, 'wodacity', 28)
hashtable_add(table, 'udacity', 27)
hashtable_add(table, 'darkcity', 44)

hashtable_update(table, 'bluecity', 32)
print table
#print hashtable_get_bucket(table, 'udacity')
#print hashtable_lookup(table, 'bodacity')




