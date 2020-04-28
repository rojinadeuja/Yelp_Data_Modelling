##################################################
## {A script that embeds the review collection into business collection MongoDB}
##################################################
## Author: {Rojina Deuja}
## Last Updated: {04-27-2020}
##################################################

# Import necessary modules
import pymongo
import json

# Set up the MongoClient and the connection to the default host (localhost) and port (27017)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Open database and collections
db = client['yelp_database'] 
reviews = db['review']
businesses = db['business']

# Find documents from the review collection
myquery = {}
mydoc = reviews.find(myquery) # db.collection.find({})

result = list(mydoc) 
cnt=0
for x in result:
    print("Rows updated:", cnt)
    business_id = x['business_id'] # x is a dict
    myquery = { "business_id": business_id}
    newvalues = {"$push": {"reviews" : x}}
    businesses.update(myquery, newvalues)
    cnt = cnt+1

# Close connection
client.close()


