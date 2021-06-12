package main

import (
	"Laboratorium_13/books"
	"fmt"
)

func main() {
	bks := []books.Book{}
	//b := books.Book{Isbn: "345-4405255600", Title: "AngularJS", Author: "Dayley Brad", Price: 22.22}

	myBks := []books.Book{
		{Isbn: "171-1505255607", Title: "The Time Machine", Author: "H. G. Wells", Price: 5.99},
		{Isbn: "272-2503261960", Title: "Wind Sand \u0026 Stars", Author: "Antoine", Price: 24.99},
		{Isbn: "373-3503261961", Title: "West With The Night", Author: "Beryl Markham", Price: 14.99},
		{Isbn: "474-4503261961", Title: "C++", Author: "Stroustrup Bjarne", Price: 12.45}}

	books.InsertBook(myBks[0])
	books.InsertBook(myBks[1])
	books.InsertBook(myBks[2])
	books.InsertBook(myBks[3])

	bks, _ = books.GetBooks()
	fmt.Println(bks)

	fmt.Println()

	//b := books.Book{}
	b, _ := books.GetOneBook("272-2503261960")
	//bks, _ = books.GetBooks()
	fmt.Println("book: ", b)

	fmt.Println()

	books.DeleteBook("373-3503261961")
	bks, _ = books.GetBooks()
	fmt.Println(bks)

	fmt.Println()

	ub := books.Book{Isbn: "474-4503261961", Title: "MongoDB", Author: "Dayley Brad", Price: 11.70}
	books.UpdateBook(ub)

	b, _ = books.GetOneBook("474-4503261961")
	//bks, _ = books.GetBooks()
	fmt.Println("book: ", b)

	bks, _ = books.GetBooks()
	fmt.Println(bks)

}
