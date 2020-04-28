/*************************************************
** {A script to prepare the yelp_database by carrying out data pre-processing}
**************************************************
** Author: {Rojina Deuja}
** Last Updated: {04-27-2020}
*************************************************/

/*
 To Run:
 mongo 00_data_preprocessing.js
 */

// Set up a new connection to yelp_database and store it in the global db variable to yelp_database
db = connect("localhost:27017/yelp_database");

// Count of all items in business
print("The count of rows in collection business: ", db.business.count())

// Remove all business that don't have Restaurant as a category
print(db.business.remove({ "categories" : { $not: /Restaurant/}}))

// Remove all business that have review_count less than 10
print(db.business.remove({ "review_count" : { $lt: 10}}))

// Show final count of business
print("The count of rows in collection business is now: ", db.business.count() )

// Count of all items in review
print("The count of rows in collection review: ", db.review.count())

// Remove all reviews that were not from the year 2018
print(db.review.remove({"date": { $not: /^2018/}}))

// Remove all reviews that have useful vote less than 5
print(db.review.remove({ "useful" : { $not: {$gte: 5}}}))

// Show final count of review
print("The count of rows in collection review is now: ", db.review.count() )
