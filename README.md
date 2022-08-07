# Local-Library-Api-Service
A library Api service that exposes 8 endpoints that allows get, post, put, patch and delete request methods for books, authors, genre and language

Interact with the Api live at https://sotomi-local-library-api.herokuapp.com/

The first 4 endpoints are seen below. This endpoints allows for get and post operations or methods

{
    "books": "https://sotomi-local-library-api.herokuapp.com/books/",
    "authors": "https://sotomi-local-library-api.herokuapp.com/authors/",
    "genre": "https://sotomi-local-library-api.herokuapp.com/genre/",
    "language": "https://sotomi-local-library-api.herokuapp.com/language/"
}

Adding a number to each end point above takes you to the detail page of each instance if it exists where get, put and delete methods are allowed for the instance . E.g 

{
    "books": "https://sotomi-local-library-api.herokuapp.com/books/2",
    "authors": "https://sotomi-local-library-api.herokuapp.com/authors/4",
    "genre": "https://sotomi-local-library-api.herokuapp.com/genre/5",
    "language": "https://sotomi-local-library-api.herokuapp.com/language/6"
}

<p><strong>Detail Explanation of each endpoint </strong></p>
1. Books/
"books": "https://sotomi-local-library-api.herokuapp.com/books/",

This endpoint returns a list of all books in the library as well as the number of copies of each book, number of loaned out books, author for each book, language written in and the genre class.
This endpoint also accepts a post request and allows clients to add to the list of books in the library.

"books": "https://sotomi-local-library-api.herokuapp.com/books/2"
This endpoint will return the detail page of a book instance if it exist. it supports put method for all instances and delete methods for only instances without any copies in the system.

2. Authors/
"authors": "https://sotomi-local-library-api.herokuapp.com/authors/",,

This endpoint returns a list of all authors in the library as well as the number books they have written.
This endpoint also accepts a post request and allows clients to add to the list of authors in the library.

"authors": "https://sotomi-local-library-api.herokuapp.com/authors/4",
This endpoint will return the detail page of an author instance  if it exist. it supports put and delte methods for all instances.

3. Genre/
 "genre": "https://sotomi-local-library-api.herokuapp.com/genre/",

This endpoint returns a list of all book genre in the library as well as the number books that fit this genre 
This endpoint also accepts a post request and allows clients to add to the list of book genre in the library.

 "genre": "https://sotomi-local-library-api.herokuapp.com/genre/5",
This endpoint will return the detail page of an genre instance  if it exist. it supports put and delte methods for all instances.

4. Language/
   "language": "https://sotomi-local-library-api.herokuapp.com/language/"

This endpoint returns a list of all languages the books have been written in as well as the number books written in each particular language
This endpoint also accepts a post request and allows clients to add to the list of languages in the library.

"language": "https://sotomi-local-library-api.herokuapp.com/language/6"
This endpoint will return the detail page of an language instance  if it exist. it supports put and delte methods for all instances.

