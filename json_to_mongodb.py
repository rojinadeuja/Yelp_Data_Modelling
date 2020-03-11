import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/") #Connection will be established to the default host (localhost) and port (27017)

db = client['yelp_database'] #Create database

checkins = db['checkin'] #Create collection
print(checkins)
 
# dblist = myclient.list_database_names()  #Check if database created
# if "yelp_database" in dblist:
#     print("The database exists.")
# else:
#     print("The database does not exist!")

# mycol = mydb["checkin"]

# collist = mydb.list_collection_names()
# if "checkin" in collist:
#     print("The collection exists.")