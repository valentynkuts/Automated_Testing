package books

import (
	"Laboratorium_13/config"
	"errors"
	"gopkg.in/mgo.v2/bson"
	"unsafe"
)

type Book struct {
	Isbn   string  // `json:"isbn" bson:"isbn"`
	Title  string  // `json:"title" bson:"title"`
	Author string  // `json:"author" bson:"author"`
	Price  float64 // `json:"price" bson:"price"`
}

func GetBooks() ([]Book, error) {
	bks := []Book{}
	err := config.Books.Find(bson.M{}).All(&bks)
	if err != nil {
		//log.Fatal(err)
		return nil, err
	}
	return bks, nil
}

func GetBooks1(bks []Book) ([]Book, error) {
	err := config.Books.Find(bson.M{}).All(&bks)
	if err != nil {
		return nil, err
	}
	return bks, nil
}

func InsertBook(bk Book) error {
	if (Book{} == bk) {
		return errors.New("No Data in the Book")
	}
	// insert values
	err := config.Books.Insert(bk)
	if err != nil {
		return err
	}
	return nil
}

func DeleteBook(isbn string) error {
	if isbn == "" {
		return errors.New("Empty String")
	}
	err := config.Books.Remove(bson.M{"isbn": isbn})
	if err != nil {
		return err
	}
	return nil
}

func GetOneBook(isbn string) (Book, error) {
	bk := Book{}
	if isbn == "" {
		return bk, errors.New("Empty String")
	}
	err := config.Books.Find(bson.M{"isbn": isbn}).One(&bk)
	if err != nil {
		return bk, err
	}
	return bk, nil
}

func UpdateBook(bk Book) error {
	//the empty struct itself takes no memory
	if unsafe.Sizeof(bk) == 0 {
		return errors.New("No Data in the Book")
	}
	//if bk.Isbn == "" || bk.Title == "" || bk.Author == "" || bk.Price == 0{
	//	return errors.New("No Data in the Book")
	//}

	err := config.Books.Update(bson.M{"isbn": bk.Isbn}, &bk)
	if err != nil {
		return err
	}
	return nil
}
