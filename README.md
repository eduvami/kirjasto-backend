# kirjasto-backend 📚

# Description
This is the backend repo for the Digitalents Academy Library Application 📚 Kirjasto is a Digitalents Academy project made by the workshop interns in colloboration. The main repositiory for the project is at <link>

# Authors
Boris (https://github.com/BorisHiltunen)
Siim (https://github.com/shiimu)

Api endpoints:

127.0.0.1:8080/

<b>GET, POST, PUT, DELETE</b>

POST, PUT and DELETE currently require all of the arguments listed below

<b>available</b> - lists all the books available for loaning. <br />
arguments: name, writer, year, isbn, rating, about, tags, description

<b>borrowed</b> - lists all the books that are currently being loaned out. <br />
arguments: name, writer, year, isbn, rating, about, tags, description, borrower

<b>comments</b> - lists all the comments. <br />
arguments: commenter, message
