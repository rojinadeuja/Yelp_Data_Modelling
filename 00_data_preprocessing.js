/*************************************************
** {A script to prepare the yelp_database}
**************************************************
** Author: {Rojina Deuja}
** Last Updated: {04-27-2020}
*************************************************/

// Set up a new connection to yelp_database and store it in the global db variable to yelp_database
db = connect("localhost:27017/yelp_database");

// Print all items in a collection
cursor = db.topic.find();
while ( cursor.hasNext() ) {
   printjson( cursor.next() );
}

/*
 To Run:
 mongo 00_data_preprocessing.js
 */