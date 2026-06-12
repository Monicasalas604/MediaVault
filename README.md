# MediaVault

MediaVault is a personal media tracking application developed in Python that allows users to manage and organize their books, movies, and TV series in a single watchlist.

The project follows Object-Oriented Programming principles and includes a Streamlit frontend, a Flask API backend, SQLite database integration, automated testing, static code analysis, and distributable Python packages.

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

---

## View Watchlist

Users can view their media collection grouped by:

* Books
* Movies
* Series

---

## Update Existing Items

Users can modify previously stored media entries, including:

* Status
* Rating

---

## Database Storage

All media information is stored in an SQLite database.

---

## REST API

The Flask backend provides API endpoints that allow the Streamlit frontend to communicate with the database.

Supported operations include:

* Creating media items
* Retrieving media items
* Updating media information
* Deleting media items

---

# Object-Oriented Programming Concepts

The project demonstrates the use of:

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
* MyPy
* Black

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
│   ├── test_api.py
│   ├── test_models.py
│   └── test_services_database.py
│
├── README.md
├── requirements.txt
├── report.md
├── test_report.md
├── pyproject.toml
└── .gitignore
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/Monicasalas604/MediaVault.git
cd MediaVault
```

---

## Virtual Environment Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows Command Prompt

```bash
.venv\Scripts\activate
```

### Git Bash

```bash
source .venv/Scripts/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

## Start the Flask Backend

Open a terminal and run:

```bash
python api.py
```

---

## Start the Streamlit Frontend

Open a second terminal and run:

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

# Running Tests

Execute all automated tests:

```bash
python -m pytest
```

The project includes:

* API Tests
* Model Tests
* Database Tests

A total of 26 automated tests verify the application's functionality.

---

# Code Quality

The project uses several tools to improve code quality and maintainability.

## Pytest

Run automated tests:

```bash
python -m pytest
```

---

## Pylint

Run static code analysis:

```bash
python -m pylint api.py app.py database.py models.py services.py
```

---

## MyPy

Run type checking:

```bash
python -m mypy api.py database.py models.py services.py
```

---

## Black

Check code formatting:

```bash
python -m black --check .
```

Format code automatically:

```bash
python -m black .
```

---

# Documentation

Additional project documentation:

* report.md
* test_report.md

These files describe the project implementation, testing process, and development decisions.

---

# Distributable Packages

The project uses modern Python packaging standards through `pyproject.toml`.

To build the package:

```bash
python -m build
```

Generated files are stored in the `dist/` directory:

* Source Distribution (.tar.gz)
* Wheel Distribution (.whl)

---

# Author

Monica Salas

Computer Science Student

SRH University Leipzig Campus

Student ID: 100005574

Programming Lab Final Project

