# API-Endpoints-with-Database-Interaction
Building 3 API Endpoints with Database Interaction, for library management with python

## Introduction
The Library Management API is a basic Flask application that provides three API endpoints to perform CRUD operations on books in a library. The application interacts with a SQLite database to store book information.

## Features
- Retrieve all books from the library
- Add a new book to the library
- Update details of a specific book

## Adding a book
$headers = @{ 'Content-Type' = 'application/json' }
$body = @{
    'title' = 'New Book Title'
    'author' = 'New Author'
    'genre' = 'New Genre'
} | ConvertTo-Json

$response = Invoke-WebRequest -Uri 'http://127.0.0.1:5000/api/books' -Method Post -Headers $headers -Body $body

Write-Output "Status Code: $($response.StatusCode)"
Write-Output "Response Content: $($response.Content)"


run this script in terminal to add a book
