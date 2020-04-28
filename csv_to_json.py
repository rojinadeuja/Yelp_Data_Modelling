import json
import pymongo
import pandas as pd
myclient = pymongo.MongoClient()

df = pd.read_csv('Data\yelp_academic_dataset_review_10000.csv',encoding = 'utf8')   # loading csv file
df.to_json('Data\yelp_academic_dataset_review_10000.json')                               # saving to json file