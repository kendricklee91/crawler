from pymongo import MongoClient

# insert function
def insertWebtoon(dicWebtoon):
    conn = MongoClient('localhost', 27017)
    db = conn['naver']
    collection = db['webtoon']

    collection.insert({"day": dicWebtoon['day'], # day
                       'webtoon': dicWebtoon['webtoon']  # title and url of webtoon
                       })
    conn.close()

# select function
def selectWebtoon():
    conn = MongoClient('localhost', 27017)
    db = conn['naver']
    collection = db['webtoon']

    for i in collection.find():
        print(i)
    conn.close()

