/*************************************************
** {A script to prepare the yelp_database by carrying out data pre-processing}
**************************************************
** Author: {Rojina Deuja}
** Last Updated: {04-27-2020}
*************************************************/

/*
 To Run:
 mongo 01_part2_business_with_reviews.js
 */

// Set up a new connection to yelp_database and store it in the global db variable to yelp_database
db = connect("localhost:27017/yelp_database");

// Get only those business that have reviews
var business_with_reviews = (db.business.find({"reviews": { $ne : null}}))

// Create a new collection with the business with reviews
db.business_restaurant.insert(business_with_reviews.toArray());
