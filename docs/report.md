# MediaVault Technical Report

## 1. Introduction

MediaVault is a personal media tracking application developed in Python as the final project for the Programming Lab course.

The application allows users to manage books, movies, and television series in a single platform. Users can add new media items, view their watchlist, update information, assign ratings, and delete entries when they are no longer needed.

The project was designed to demonstrate object-oriented programming principles, database management, frontend and backend development, and software testing.

---

## 2. Project Objectives

The main objectives of the project were:

* Apply object-oriented programming concepts.
* Develop a graphical user interface.
* Implement persistent data storage.
* Create a REST API for communication between application layers.
* Follow a modular software architecture.
* Implement automated testing.

---

## 3. System Architecture

MediaVault follows a layered architecture that separates responsibilities into different components.

```text
Streamlit Frontend
        ↓
Flask REST API
        ↓
WatchlistManager
        ↓
DatabaseManager
        ↓
SQLite Database
```

### Frontend Layer

The frontend was developed using Streamlit. It provides a simple and interactive user interface that allows users to manage their media collection.

### Backend Layer

The backend was developed using Flask. It exposes REST API endpoints that process requests coming from the frontend.

### Business Logic Layer

The WatchlistManager class contains the application's business logic. It is responsible for creating media objects and coordinating operations between the frontend and the database.

### Data Access Layer

The DatabaseManager class handles all communication with the SQLite database, including inserting, retrieving, updating, and deleting records.

---

## 4. Object-Oriented Design

Object-oriented programming was a central aspect of the project.

### Abstract Base Class

The MediaItem class serves as an abstract base class containing attributes shared by all media types:

* title
* genre
* status
* rating
* review

The class also defines common behavior such as updating ratings and marking an item as completed.

### Inheritance

Three subclasses inherit from MediaItem:

#### Book

Additional attributes:

* author
* total_pages

#### Movie

Additional attributes:

* director
* duration

#### Series

Additional attributes:

* creator
* seasons

Inheritance reduces code duplication and improves maintainability.

### Validation

A nested RatingValidator class validates ratings and ensures that values remain within the accepted range of 0 to 5.

---

## 5. Database Design

The project uses SQLite as its database management system.

SQLite was selected because it is lightweight, easy to configure, and suitable for desktop-sized applications.

The application stores all media types in a single table called media.

### Database Schema

| Column     | Type    |
| ---------- | ------- |
| id         | INTEGER |
| type       | TEXT    |
| title      | TEXT    |
| genre      | TEXT    |
| status     | TEXT    |
| rating     | REAL    |
| review     | TEXT    |
| creator    | TEXT    |
| extra_info | INTEGER |

The creator field stores authors, directors, or creators depending on the media type.

The extra_info field stores pages, duration, or seasons.

This design allows different media types to be stored efficiently within a single table.

---

## 6. REST API Design

The Flask backend exposes several endpoints.

### GET Endpoints

* GET /
* GET /health
* GET /media

### POST Endpoints

* POST /books
* POST /movies
* POST /series

### PUT Endpoints

* PUT /media/<id>/status
* PUT /media/<id>/rating

### DELETE Endpoint

* DELETE /media/<id>

The API enables communication between the Streamlit frontend and the database layer.

---

## 7. Features Implemented

The final version of MediaVault includes:

### Media Management

* Add books
* Add movies
* Add series
* View media collection
* Update status
* Update ratings
* Delete entries

### Technical Features

* Object-oriented architecture
* REST API communication
* SQLite persistence
* Logging
* Error handling
* Automated testing

---

## 8. Testing

The project includes automated testing using pytest.

Testing was performed on:

* Model classes
* Rating validation
* Business logic
* Database operations
* API endpoints

The tests verify that the application behaves correctly under normal and exceptional conditions.

Automated testing improves reliability and helps detect bugs early during development.

---

## 9. Challenges and Solutions

One challenge encountered during development was connecting the Streamlit frontend with the Flask backend.

This was solved by implementing REST API endpoints and using HTTP requests to exchange data between both components.

Another challenge was storing multiple media types in a single database table. This was addressed by using generic fields that adapt to the selected media type.

The project also required maintaining a clean separation between user interface logic, business logic, and database operations. This was achieved through the layered architecture.

---

## 10. Conclusion

MediaVault successfully fulfills the objectives of the project.

The application combines object-oriented programming, database management, API development, testing, and user interface design into a single system.

The final result is a functional and maintainable application that demonstrates the software engineering concepts learned throughout the Programming Lab course.
