# kirjasto-backend 📚

# Description
This is the backend repo for the Digitalents Academy Library Application 📚 Kirjasto is a Digitalents Academy project made by the workshop interns in collaboration. The main repositiory for the project is at [digitalents-academy/kirjasto](https://github.com/digitalents-academy/kirjasto)

# Authors
Boris ([BorisHiltunen](https://github.com/BorisHiltunen))

Siim ([shiimu](https://github.com/shiimu))

# Tools and Libraries
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [MongoDB](https://www.mongodb.com/)
- [flask-restful](https://flask-restful.readthedocs.io/en/latest/)

# Api endpoints:

Localhost:8000/

<b>GET</b>
- Status
- Status/id
- Books

<b>POST</b>
- Loan

POST, PUT and DELETE currently require all of the arguments listed below

<b>available</b> - lists all the books available for loaning. <br />
arguments: name, writer, year, isbn, rating, about, tags, description

<b>borrowed</b> - lists all the books that are currently being loaned out. <br />
arguments: name, writer, year, isbn, rating, about, tags, description, borrower

<b>comments</b> - lists all the comments. <br />
arguments: commenter, message
