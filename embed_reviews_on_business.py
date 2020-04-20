import pymongo
import json

#Set up the MongoClient and the connection to the default host (localhost) and port (27017)
client = pymongo.MongoClient("mongodb://localhost:27017/")

#Create database
db = client['yelp_database'] 
reviews = db['review']
businesses = db['business']

#Find documents from the collection
myquery = {}
mydoc = reviews.find(myquery)

result = list(mydoc) #db.collection.find()
cnt=0
for x in result:
    print("Rows updated:", cnt)
    business_id = x['business_id'] #x is a dict
    myquery = { "business_id": business_id}
    newvalues = {"$push": {"reviews" : x}}
    businesses.update(myquery, newvalues)
    cnt = cnt+1

#Close connectioncls
client.close()


