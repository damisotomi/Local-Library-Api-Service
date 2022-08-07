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
