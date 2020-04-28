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
mongoimport --db=yelp_database_test --collection=business --file=yelp_academic_dataset_business.json

# Import data into collection review
mongoimport --db=yelp_database_test --collection=review --file=yelp_academic_dataset_review.json