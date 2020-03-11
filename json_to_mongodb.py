import pymongo
import json

#Set up the MongoClient and the connection to the default host (localhost) and port (27017)
client = pymongo.MongoClient("mongodb://localhost:27017/")

#Create database
db = client['yelp_database'] 

#Create collection checkins------------------------------------------------
checkins = db['checkin'] 

#Read from json file into a list
checkin_list =[]
for line in open('Data\yelp_academic_dataset_checkin.json', encoding="utf8"):
    checkin_list.append(json.loads(line))

#Delete all rows in collection
checkins.delete_many({})
#Insert list into collection
checkins.insert_many(checkin_list)

print("\nInserting checkins completed!")
# #Query the collection
# cursor = checkins.find({})

# #Print first five rows to check if inserted
# i=1
# for document in cursor:
#     if(i<5):
#         print(document)
#         i=i+1

#Create collection businesses--------------------------------------------------
businesses = db['business'] 

#Read from json file into a list
business_list =[]
for line in open('Data\yelp_academic_dataset_business.json', encoding="utf8"):
    business_list.append(json.loads(line))

#Delete all rows in collection
businesses.delete_many({})
#Insert list into collection
businesses.insert_many(business_list)
print("\nInserting businesses completed!")

#Create collection reviews------------------------------------------------------
reviews = db['review'] 

#Read from json file into a list
review_list =[]
for line in open('Data\yelp_academic_dataset_review.json', encoding="utf8"):
    review_list.append(json.loads(line))

#Delete all rows in collection
reviews.delete_many({})
#Insert list into collection
reviews.insert_many(review_list)
print("\nInserting reviews completed!")

#Create collection tips---------------------------------------------------------
tips = db['tip'] 

#Read from json file into a list
tip_list =[]
for line in open('Data\yelp_academic_dataset_tip.json', encoding="utf8"):
    tip_list.append(json.loads(line))

#Delete all rows in collection
tips.delete_many({})
#Insert list into collection
tips.insert_many(tip_list)
print("\nInserting tips completed!")

#Create collection users--------------------------------------------------------
users = db['user'] 

#Read from json file into a list
user_list =[]
for line in open('Data\yelp_academic_dataset_user.json', encoding="utf8"):
    user_list.append(json.loads(line))

#Delete all rows in collection
users.delete_many({})
#Insert list into collection
users.insert_many(user_list)
print("\nInserting users completed!")

#Close connection
client.close()


