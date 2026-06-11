# MediaVault

MediaVault is a personal media tracking application developed in Python that allows users to manage and organize their books, movies, and TV series in a single watchlist.

The project follows Object-Oriented Programming principles and includes a Streamlit frontend, a Flask API backend, SQLite database integration, automated testing, and distributable Python packages.

---

# Features

## Add Media Items

Users can add:

* Books
* Movies
* TV Series

Each media item stores:

* Title
* Genre
* Status
* Rating
* Review
* Creator information
* Additional media-specific information

## View Watchlist

Users can view their media collection grouped by:

* Books
* Movies
* Series

## Update Existing Items

Users can modify previously stored media entries.

## Database Storage

All media information is stored in an SQLite database.

## REST API

The Flask backend provides API endpoints that allow the Streamlit frontend to communicate with the database.

---

# Object-Oriented Programming Concepts

The project demonstrates several Object-Oriented Programming principles:

* Classes and Objects
* Encapsulation
* Inheritance
* Polymorphism
* Abstraction

Media items are represented through specialized classes for Books, Movies, and Series, while service and database layers separate business logic from data storage.

---

# Technologies Used

* Python 3
* Streamlit
* Flask
* SQLite
* Requests
* Pytest
* Pylint

---

# Project Structure

```text
MediaVault/
│
├── app.py
├── api.py
├── database.py
├── models.py
├── services.py
│
├── tests/
├── docs/
├── screenshots/
├── dist/
│
├── README.md
├── requirements.txt
├── pyproject.toml
└── .gitignore
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Monicasalas604/MediaVault.git
cd MediaVault
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Application

## Start the Flask Backend

```bash
python api.py
```

## Start the Streamlit Frontend

Open a second terminal and run:

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

# Running Tests

Execute:

```bash
pytest
```

---

# Documentation

Additional project documentation is available in the `docs` folder:

* `report.md`
* `test_report.md`

---

# Distributable Packages

The project is distributed using modern Python packaging standards through `pyproject.toml`.

Generated distributable files:

* `mediavault_monica-1.0.0.tar.gz` (source distribution)
* `mediavault_monica-1.0.0-py3-none-any.whl` (wheel distribution)

These files are located in the `dist/` folder and can be installed or distributed independently of the source code.

Package configuration:

```text
pyproject.toml
```

Generated package files:

```text
dist/
├── mediavault_monica-1.0.0.tar.gz
└── mediavault_monica-1.0.0-py3-none-any.whl
```

To rebuild the package:

```bash
python -m build
```

---

# Author

**Monica Salas**
Computer Science, Leipzig Campus
Student ID: 100005574

Programming Lab Final Project

---
