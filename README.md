# MediaVault

A personal media tracking application written in Python that allows users to manage books, movies, and television series through a Streamlit interface connected to a Flask REST API and SQLite database.

## Features

### Media Management

* Add books
* Add movies
* Add series
* View all saved media
* Update media status
* Update ratings
* Delete media entries

### Technical Features

* Object-Oriented Programming
* SQLite database persistence
* Flask REST API
* Streamlit graphical interface
* Logging
* Error handling
* Automated testing with pytest

---

## Requirements

* Python 3.x
* Streamlit
* Flask
* Requests
* Pytest

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

### Start the Backend

```bash
python api.py
```

The API will run on:

```text
http://127.0.0.1:5000
```

### Start the Frontend

Open a second terminal:

```bash
streamlit run app.py
```

---

## Project Structure

```text
MediaVault
│
├── app.py
├── api.py
├── database.py
├── models.py
├── services.py
│
├── tests
│   ├── test_models.py
│   ├── test_services_database.py
│   └── test_api.py
│
├── docs
│   ├── report.md
│   └── test_report.md
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Key Classes

| Class            | Responsibility                                     |
| ---------------- | -------------------------------------------------- |
| MediaItem        | Abstract base class for all media types            |
| Book             | Represents books and stores author and pages       |
| Movie            | Represents movies and stores director and duration |
| Series           | Represents series and stores creator and seasons   |
| DatabaseManager  | Handles all SQLite database operations             |
| WatchlistManager | Handles business logic and media management        |

---

## API Endpoints

### GET

```text
/
/health
/media
```

### POST

```text
/books
/movies
/series
```

### PUT

```text
/media/<id>/status
/media/<id>/rating
```

### DELETE

```text
/media/<id>
```

---

## Running Tests

Run all tests:

```bash
python -m pytest
```

Run coverage:

```bash
python -m pytest --cov=.
```

The tests cover:

* Media models
* Rating validation
* Database operations
* Business logic
* Flask API endpoints

---

## Possible Future Improvements

* Search media by title
* Statistics dashboard
* User accounts
* Export watchlists to CSV
* Media cover images
* Genre filtering
* Sorting by rating or status


## Author
Monica Salas
Computer Science, Leipzig Campus
ID: 100005574

Programming Lab Final Project

---

