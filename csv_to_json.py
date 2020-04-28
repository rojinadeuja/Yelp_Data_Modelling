##################################################
## {A script that converts csv files to json files and saves it on disk}
##################################################
## Author: {Rojina Deuja}
## Last Updated: {04-27-2020}
##################################################

#Import necessary modules
import json
import pymongo
import pandas as pd
myclient = pymongo.MongoClient()
#Read csv file into pandas dataframe
df = pd.read_csv('csv_filename',encoding = 'utf8')
#Covert to json and save to disk
df.to_json('json_filename')                              