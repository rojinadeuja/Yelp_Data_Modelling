##################################################
## {A script that reads json file and inserts it into MongoDB}
##################################################
## Author: {Rojina Deuja}
## Last Updated: {04-27-2020}
##################################################

## To Run:
# Run shell as administrator
# Run the command: Set-ExecutionPolicy RemoteSigned
# Run the script: ./import_script.ps1

# Import data into collection business
mongoimport --db=yelp_database --collection=business --file=Data/yelp_academic_dataset_business.json

# Import data into collection review
mongoimport --db=yelp_database --collection=review --file=Data/yelp_academic_dataset_review.json

# Import data into collection user
mongoimport --db=yelp_database --collection=user --file=Data/yelp_academic_dataset_user.json

# Import data into collection checkin
mongoimport --db=yelp_database --collection=checkin --file=Data/yelp_academic_dataset_checkin.json

# Import data into collection tip
mongoimport --db=yelp_database --collection=tip --file=Data/yelp_academic_dataset_tip.json