from __future__ import division
import pprint

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
    #{ "id": 10, "name": "Jen" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j]["id"])
    users[j]["friends"].append(users[i]["id"])

total_connections = sum(len(user["friends"]) for user in users)
#print total_connections
avg_connections = total_connections / len(users)
#print avg_connections

num_friends_by_id = [(user["id"], len(user["friends"])) for user in users]
sorted(num_friends_by_id, key=lambda (user_id, num_friends): num_friends, reverse=True)
#print num_friends_by_id

def is_friend(user, id):
    return 1 if id in user["friends"] else 0

mx_friends = [[is_friend(user,j) for j,_ in enumerate(users)] for i,user in enumerate(users)]
#pprint.pprint(mx_friends)

def get_foaf_ids_bad(id):    
    foaf_ids = []
    friends = mx_friends[id]

    for fid,val in enumerate(friends):
        if val:
            foaf_ids += users[fid]["friends"]

    return set(n for n in foaf_ids if n != id)
    #return [users[fid]["friends"] for fid,val in enumerate(mx_friends[id]) if val]

# mutual friends
from collections import Counter
def not_the_same(user, other_user):
    return user['id'] != other_user['id']

# if other_user is not in user['friends'], he is not considered as a friend
def not_friends(user, other_user):
    return all(not_the_same(users[fid], other_user) for fid in user['friends'])

def foaf_ids(user):
    return Counter(foaf
                   for fid in user['friends']
                   for foaf in users[fid]['friends']
                   if not_the_same(user,users[foaf]) and not_friends(user,users[foaf]))

#print foaf_ids(users[3])

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

from collections import defaultdict

# 1. indentify the interest of the user
# 2. find out who other users have each interest
# 3. count how many times other users appear 
user_ids_by_interest = defaultdict(list)
interest_by_user_ids = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    interest_by_user_ids[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(interested_user_id
                   for interest in interest_by_user_ids[user['id']]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user['id'])

#print most_common_interests_with(users[0])
words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print word, count
