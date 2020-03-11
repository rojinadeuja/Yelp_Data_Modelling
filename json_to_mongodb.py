import pymongo
import json

#Set up the MongoClient and the connection
client = pymongo.MongoClient("mongodb://localhost:27017/") #Connection will be established to the default host (localhost) and port (27017)

#Create database
db = client['yelp_database'] 

#Create collection
checkins = db['checkin'] 

#Read from json file into a list
checkin_list =[]
for line in open('yelp_academic_dataset_checkin.json', 'r'):
    checkin_list.append(json.loads(line))

#Delete all rows in collection
checkins.delete_many({})
#Insert list into collection
checkins.insert_many(checkin_list)

#Query the collection
cursor = checkins.find({})

#Print first five rows to check if inserted
i=1
for document in cursor:
    if(i<5):
        print(document)
        i=i+1
        
#Close connection
client.close()