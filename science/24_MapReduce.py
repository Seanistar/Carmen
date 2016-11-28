from collections import defaultdict, Counter
from functools import partial
#from naive_bayes import tokenize

documents = ["data science", "big data", "science fiction"]

# mapper: convert documents into sets has key-value pair
def wc_mapper(doc):
    ''' yield (word, 1) whenever find any word '''
    #import tokenize as tkn
    #for word in tokenize(document):
    for word in doc.split():
        yield (word, 1)
        
# reducer: summarize all of word counts 
def wc_reducer(word, counts):
    yield (word, sum(counts))

# count word's frequency in the input document using by MapReducer
def word_count(docs):
    collector = defaultdict(list)

    for doc in docs:
        for word, count in wc_mapper(doc):
            collector[word].append(count)

    return [output
            for word, counts in collector.iteritems()
            for output in wc_reducer(word, counts)]

def map_reduce(inputs, mapper, reducer):
    collector = defaultdict(list)

    for input in inputs:
        for key, value in mapper(input):
            collector[key].append(value)

    return [output
            for key, values in collector.iteritems()
            for output in reducer(key, values)]

#word_counts = map_reduce(documents, wc_mapper, wc_reducer)

''' generalize mapreduce '''
def reduce_values_using(fn_aggregation, key, values):
    ''' aggregate pairs of key-value by applying aggregation_fn to the values'''
    yield (key, fn_aggregation(values))

def values_reducer(fn_aggregation):
    ''' create a reducer function that do a func (value -> output) mapping into (key, value) -> (key, output)'''
    return partial(reduce_values_using, fn_aggregation)

sum_reducer = values_reducer(sum)
max_reducer = values_reducer(max)
min_reducer = values_reducer(min)
count_distinct_reducer = values_reducer(lambda values: len(set(values)))

''' analyze user document '''
import datetime
status_updates = [ { "id":1,
                    "username": "joelgrus",
                    "text": "is anyone interested in a data science book?",
                    "created_at": datetime.datetime(2013, 12, 21, 11, 47, 0),
                    "liked_by": ["data_guy", "data_gal", "mike"] },
                   { "id":2,
                    "username": "degulas",
                    "text": "is anyone interested in a data analysis book?",
                    "created_at": datetime.datetime(2014, 11, 28, 10, 15, 0),
                    "liked_by": ["mir", "ksport", "mike"] }
                   ]

# find which day in a week people talk the most about 'data science'?
def date_science_day_mapper(status_update):
    if "date science" in status_update["text"].lower():
        day_of_week = status_update["created_at"].weekday()
        yield(day_of_week, 1)

    data_science_days = map_reduce(status_updates, data_science_day_mapper, sum_reducer)

# find what kind of word each user often use the most?
def words_per_user_mapper(status_update):
    user = status_update["username"]

    #for word in tokenize(status_update["text"]):
    for word in status_update["text"].split():
        yield (user, (word, 1))

def most_popular_word_reducer(user, words_and_counts):
    ''' return word that total frequency is highest from arrays composed pairs (word, frequency)'''
    word_counts = Counter()
    for word, count in words_and_counts:
        word_counts[word] += count

    word, count = word_counts.most_common(1)[0]
    yield (user, (word, count))

user_words = map_reduce(status_updates, words_per_user_mapper, most_popular_word_reducer)

# enable to count those who give 'like' to each user's feed
def liker_mapper(status_update):
    user = status_update["username"]
    for liker in status_update["liked_by"]:
        yield (user, liker)

distinct_liker_per_user = map_reduce(status_updates, liker_mapper, count_distinct_reducer)

##################################
''' calculate matrix '''
A = [ [3, 2, 0], [0, 0, 0] ]
B = [ [4, -1, 0], [10, 0, 0], [0, 0, 0] ]

def matrix_multiply_mapper(m, element):
    """m is the common dimension (columns of A, rows of B)
    element is a tuple (matrix_name, i, j, value)"""
    matrix, i, j, value = element

    if matrix == "A":
        for column in range(m):
            # A_ij is the jth entry in the sum for each C_i_column
            yield((i, column), (j, value))
    else:
        for row in range(m):
            # B_ij is the ith entry in the sum for each C_row_j
            yield((row, j), (i, value))
     
def matrix_multiply_reducer(m, key, indexed_values):
    results_by_index = defaultdict(list)
    for index, value in indexed_values:
        results_by_index[index].append(value)

    # sum up all the products of the positions with two results
    sum_product = sum(results[0] * results[1]
                      for results in results_by_index.values()
                      if len(results) == 2)
                      
    if sum_product != 0.0:
        yield (key, sum_product)


# matrix multiplication

entries = [("A", 0, 0, 3), ("A", 0, 1,  2),
       ("B", 0, 0, 4), ("B", 0, 1, -1), ("B", 1, 0, 10)]
mapper = partial(matrix_multiply_mapper, 3)
reducer = partial(matrix_multiply_reducer, 3)

print "map-reduce matrix multiplication"
print "entries:", entries
print "result:", map_reduce(entries, mapper, reducer)    
    
