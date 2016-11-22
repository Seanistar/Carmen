from collections import defaultdict
    
documents = ["data science", "big data", "science fiction"]

# mapper: convert documents into sets has key-value pair
def wc_mapper(doc):
    ''' yield (word, 1) whenever find any word '''
    #import tokenize as tkn
    for word in tokenize(document): # readline().split() ?
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

'''''' generalize mapreduce ''''''
def reduce_values_using(fn_aggregation, key, values):
    ''' aggregate pairs of key-value by applying aggregation_fn to the values'''
    yield (key, fn_aggregation(values))

def vales_reducer(fn_aggregation):
    ''' create a reducer function that do a func (value -> output) mapping into (key, value) -> (key, output)'''
    from functools import partial
    return partial(reduce_values_using, fn_aggregation)

sum_reducer = values_reducer(sum)
max_reducer = values_reducer(max)
min_reducer = values_reducer(min)
count_distinct_reducer = values_reducer(lambda values: len(set(values)))

'''''' analyze user document ''''''
import datetime
{ "id":1,
  "username": "joelgrus",
  "text": "is anyone interested in a data science book?",
  "created_at": datetime.datetime(2013, 12, 21, 11, 47, 0),
  "liked_by": ["data_guy", "data_gal", "mike"] }

# find which day in a week people talk the most about 'data science'?
def date_science_day_mapper(status_update):
    if "date science" in status_update["text"].lower():
        day_of_week = status_update["created_at"].weekday()
        yield(day_of_week, 1)

    data_science_days = map_reduce(status_updates, data_science_day_mapper, sum_reducer)

# find what kind of word each user often use the most?
def words_per_user_mapper(status_update):
    user = status_update["username"]

    for word in tokenize(status_update["text"]):
        yield (user, (word, 1))

def most_popular_word_reducer(user, words_and_counts):
    ''' return word that total frequency is highest from arrays composed pairs (word, frequency)'''
    from collections import Counter
    word_counts = Counter()
    for word, count in words_and_counts:
        word_counts[word] += count

    word, count = word_counts.most_common(1)[0]
    yield (user, (word, count))

user_words = map_reduce(status_updates, words_per_user_mapper, word_popular_word_reducer)

# enable to count those who give 'like' to each user's feed
def liker_mapper(status_update):
    user = status_update["username"]
    for liker in status_udpate["liked_by"]:
        yield (user, liker)

distinct_liker_per_user = map_reduce(status_updates, liker_mapper, count_distinct_reducer)

'''''' calculate matrix ''''''
A = [ [3, 2, 0], [0, 0, 0] ]
B = [ [4, -1, 0], [10, 0, 0], [0, 0, 0] ]



    
    
