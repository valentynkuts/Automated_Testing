# setup

```
go get -u gopkg.in/mgo.v2
```

[https://godoc.org/gopkg.in/mgo.v2](https://godoc.org/gopkg.in/mgo.v2)

[http://labix.org/mgo](http://labix.org/mgo)

# setup database

#### restart mongo
close any open mongo connections, then restart with these commands:
```
mongo
```

in a new tab
```
mongod
```

#### create db
```
use bookstore
```

#### create collection books & insert books
```
db.books.insert([{"isbn":"978-1505255607","title":"The Time Machine","author":"H. G. Wells","price":5.99},{"isbn":"978-1503261960","title":"Wind Sand \u0026 Stars","author":"Antoine","price":14.99},{"isbn":"978-1503261961","title":"West With The Night","author":"Beryl Markham","price":14.99}])

```

#### test
```
db.books.find()
```

#### user setup
```
db.createUser(
  {
    user: "book",
    pwd: "book001",
    roles: [ { role: "readWrite", db: "bookstore" } ]
  }
)
```

#### exit mongo & then start again with auth enabled
```
mongod --auth
```

```
mongo -u "book" -p "book001" --authenticationDatabase "bookstore"
```
#### remove dokuments
```
db.books.remove({})
```
# GO & MONGO

#### db access

```
mongodb://myuser:mypass@localhost:27017/dbToAccess
```

If the port number is not provided for a server, it defaults to 27017.

for our example:
```
mongodb://book:book001@localhost:27017/bookstore
```
[https://godoc.org/gopkg.in/mgo.v2#Dial](https://godoc.org/gopkg.in/mgo.v2#Dial)

#### db.go
Use the ```mgo.Dial``` to create a session. Assign this to the variable ```DB```.


#### models.go
Function for CRUD 

# info about testing
[https://golang.org/pkg/testing/](https://golang.org/pkg/testing/)

# setup

```
go get -u github.com/stretchr/testify
```
[https://github.com/stretchr/testify](https://github.com/stretchr/testify)

# test the application
```
go test -v

```
![result](https://github.com/valentynkuts/tau/blob/main/Laboratorium_13/res.png)
