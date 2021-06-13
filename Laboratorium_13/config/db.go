package config

import (
	"fmt"
	"gopkg.in/mgo.v2"
)

// database
var DB *mgo.Database

// collections
var Books *mgo.Collection

func init() {
	// get a mongo sessions
	s, err := mgo.Dial("mongodb://book:book001@localhost:27017/bookstore")
	if err != nil {
		panic(err)
	}

	if err = s.Ping(); err != nil {
		panic(err)
	}
    //use database "bookstore"
	DB = s.DB("bookstore")
	//use collection "books"
	Books = DB.C("books")

	fmt.Println("You connected to your mongo database.")
}
