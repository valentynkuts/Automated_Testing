package main

import (
	"Laboratorium_13/books"
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestGetBooks(t *testing.T) {
	_, err := books.GetBooks()

	if err != nil {
		t.Errorf("GetBooks() return Error ")
	}
}

func TestInsertBooks(t *testing.T) {
	//bks := []books.Book{}
	bks1, _ := books.GetBooks()
	myBks := []books.Book{
		{Isbn: "171-1505255607", Title: "The Time Machine", Author: "H. G. Wells", Price: 5.99},
		{Isbn: "272-2503261960", Title: "Wind Sand \u0026 Stars", Author: "Antoine", Price: 24.99},
		{Isbn: "373-3503261961", Title: "West With The Night", Author: "Beryl Markham", Price: 14.99},
		{Isbn: "474-4503261961", Title: "C++", Author: "Stroustrup Bjarne", Price: 12.45}}

	lenMyBks := len(myBks)
	for i := 0; i < lenMyBks; i++ {
		books.InsertBook(myBks[i])
	}

	bks2, _ := books.GetBooks()
	res := len(bks2) - len(bks1)
	if res != lenMyBks {
		t.Errorf("Result is %d, but must be %d", res, lenMyBks)
	}
}

func TestGetOneBook(t *testing.T) {
	b, _ := books.GetOneBook("171-1505255607")

	assert.Equal(t, b.Isbn, "171-1505255607")
	assert.Equal(t, b.Title, "The Time Machine")
	assert.Equal(t, b.Author, "H. G. Wells")
	assert.Equal(t, b.Price, 5.99)

}

func TestUpdateBook(t *testing.T) {
	ub := books.Book{Isbn: "474-4503261961", Title: "MongoDB", Author: "Dayley Brad", Price: 11.70}
	books.UpdateBook(ub)

	b, _ := books.GetOneBook("474-4503261961")

	assert.Equal(t, b.Title, "MongoDB")
	assert.Equal(t, b.Author, "Dayley Brad")
	assert.Equal(t, b.Price, 11.70)

}

func TestDeleteBook(t *testing.T) {
	bks1, _ := books.GetBooks()
	books.DeleteBook("373-3503261961")
	bks2, _ := books.GetBooks()

	res := len(bks1) - len(bks2)

	assert.Equal(t, res, 1)

}
