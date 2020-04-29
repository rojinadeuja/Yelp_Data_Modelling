# Yelp_Data_Modelling
Data Modelling on the data set by Yelp

### Dataset: Yelp Open Dataset [https://www.yelp.com/dataset]

The Yelp dataset is a subset of our businesses, reviews, and user data for use in personal, educational, and academic purposes. 
Available as JSON files, use it to teach students about databases, to learn NLP, or for sample production data while you learn how to make mobile apps.

### To prepare the data:
Get the mongodb dump files from : [https://unl.box.com/s/0zjl0n1sl46zgkinqscrtn5m6519zaz4]

OR

Get the data from [https://www.yelp.com/dataset/download]

Run the scripts in the order:
1. import_script.ps1 
2. 00_data_preprocessing.js
3. 01_part1_embed_reviews_on_business.py
4. 01_part2_business_with_reviews.js

The data is now ready for processing.

### Helper scripts (if required):
1. csv_to_json.py
2. json_to_mongodb.py

Author: Rojina Deuja
Last Update: 04-28-2020
