# MediaVault

MediaVault is a personal media tracking application developed in Python that allows users to manage and organize their books, movies, and TV series in a single watchlist.

The project follows Object-Oriented Programming principles and includes a Streamlit frontend, a Flask API backend, SQLite database integration, automated tests, and distributable Python packages.

---

## Features

### Add Media Items

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

### View Watchlist

Users can view their media collection grouped by:

* Books
* Movies
* Series

### Update Existing Items

Users can modify previously stored media entries.

### Database Storage

All media information is stored in an SQLite database.

### REST API

The Flask backend provides API endpoints that allow the Streamlit frontend to communicate with the database.

---

## Technologies Used

* Python 3
* Streamlit
* Flask
* SQLite
* Requests
* Pytest
* Pylint

---

## Project Structure

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

## Installation

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

## Running the Application

### Start the Flask Backend

```bash
python api.py
```

### Start the Streamlit Frontend

Open a second terminal and run:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## Running Tests

Execute:

```bash
pytest
```

---

## Distributable Packages

This project includes distributable packages generated using Python packaging standards.

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

## Screenshots

Application screenshots can be found in the `screenshots` folder.

---

## Author
Monica Salas
Computer Science, Leipzig Campus
ID: 100005574

Programming Lab Final Project

---

