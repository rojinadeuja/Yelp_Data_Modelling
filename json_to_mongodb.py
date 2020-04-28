##################################################
## {A script that reads json file and inserts it into MongoDB}
##################################################
## Author: {Rojina Deuja}
## Last Updated: {04-27-2020}
##################################################

# Import necessary modules
import pymongo
import json

# Set up the MongoClient and the connection to the default host (localhost) and port (27017)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create database
db = client['db_name'] 

# Create collection
new_collection = db['collection_name'] 

# Read from json file into a list
data_list =[]
for line in open('json_file_name', encoding="utf8"):
    data_list.append(json.loads(line))

# Delete any existing rows in collection (Execute only if required)
new_collection.delete_many({})

# Insert list into collection
new_collection.insert_many(data_list)
print("Inserting new_collection completed!")

# Query the collection
cursor = new_collection.find({})

# Print first five rows to check if inserted
i=1
for document in cursor:
    if(i<5):
        print(document)
        i=i+1

# Close connection
client.close()


