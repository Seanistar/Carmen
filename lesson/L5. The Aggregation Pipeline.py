from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.examples

def most_tweets():
    result = db.tweets.aggregate([
        { "$group": { "_id" : "$user.screen_name",
                      "count": { "$sum" : 1 } } },
        { "$sort" : { "count" : -1 } } ])
    return result

if __name__ == '__main__':
    result = most_tweets()
    pprint.pprint(list(result))
    # should use list when below error incurr
    # <pymongo.command_cursor.CommandCursor object at 0x033B6690>
