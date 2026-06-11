"""Tests for the Flask API."""

import pytest

import api


@pytest.fixture
def client(tmp_path):
    """Create a test client with a temporary database."""
    test_db = tmp_path / "test_mediavault.db"

    api.database = api.DatabaseManager(str(test_db))
    api.manager = api.WatchlistManager(api.database)

    api.app.config["TESTING"] = True

    with api.app.test_client() as test_client:
        yield test_client


def test_home_endpoint(client):
    """Test the home endpoint."""
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Welcome to the MediaVault API"}


def test_health_endpoint(client):
    """Test the health endpoint."""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_get_empty_media(client):
    """Test getting media when the database is empty."""
    response = client.get("/media")

    assert response.status_code == 200
    assert response.get_json() == []


def test_add_book_endpoint(client):
    """Test adding a book through the API."""
    book_data = {
        "title": "The Hobbit",
        "genre": "Fantasy",
        "status": "To Read",
        "rating": 8,
        "review": "Good book",
        "author": "J.R.R. Tolkien",
        "pages": 310,
    }

    response = client.post("/books", json=book_data)

    assert response.status_code == 201
    assert response.get_json() == {"message": "Book added successfully"}


def test_add_movie_endpoint(client):
    """Test adding a movie through the API."""
    movie_data = {
        "title": "Inception",
        "genre": "Science Fiction",
        "status": "Watched",
        "rating": 9,
        "review": "Great movie",
        "director": "Christopher Nolan",
        "duration": 148,
    }

    response = client.post("/movies", json=movie_data)

    assert response.status_code == 201
    assert response.get_json() == {"message": "Movie added successfully"}


def test_add_series_endpoint(client):
    """Test adding a series through the API."""
    series_data = {
        "title": "Dark",
        "genre": "Mystery",
        "status": "Watching",
        "rating": 8.5,
        "review": "Very interesting",
        "creator": "Baran bo Odar",
        "seasons": 3,
    }

    response = client.post("/series", json=series_data)

    assert response.status_code == 201
    assert response.get_json() == {"message": "Series added successfully"}


def test_get_media_after_adding_book(client):
    """Test that added media appears in the watchlist."""
    book_data = {
        "title": "The Hobbit",
        "genre": "Fantasy",
        "status": "To Read",
        "rating": 4,
        "review": "Good book",
        "author": "J.R.R. Tolkien",
        "pages": 310,
    }

    client.post("/books", json=book_data)

    response = client.get("/media")
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 1
    assert "The Hobbit" in data[0]
    assert "Book" in data[0]


def test_update_status_endpoint(client):
    """Test updating the status of a media item."""
    book_data = {
        "title": "The Hobbit",
        "genre": "Fantasy",
        "status": "To Read",
        "rating": 8,
        "review": "Good book",
        "author": "J.R.R. Tolkien",
        "pages": 310,
    }

    client.post("/books", json=book_data)

    response = client.put("/media/1/status", json={"status": "Finished"})

    assert response.status_code == 200
    assert response.get_json() == {"message": "Status updated successfully"}


def test_update_rating_endpoint(client):
    """Test updating the rating of a media item."""
    book_data = {
        "title": "The Hobbit",
        "genre": "Fantasy",
        "status": "To Read",
        "rating": 4,
        "review": "Good book",
        "author": "J.R.R. Tolkien",
        "pages": 310,
    }

    client.post("/books", json=book_data)

    response = client.put("/media/1/rating", json={"rating": 4.5})

    assert response.status_code == 200
    assert response.get_json() == {"message": "Rating updated successfully"}


def test_delete_media_endpoint(client):
    """Test deleting a media item."""
    book_data = {
        "title": "The Hobbit",
        "genre": "Fantasy",
        "status": "To Read",
        "rating": 8,
        "review": "Good book",
        "author": "J.R.R. Tolkien",
        "pages": 310,
    }

    client.post("/books", json=book_data)

    response = client.delete("/media/1")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Item deleted successfully"}


def test_media_is_empty_after_delete(client):
    """Test that media is removed after deleting it."""
    book_data = {
        "title": "The Hobbit",
        "genre": "Fantasy",
        "status": "To Read",
        "rating": 8,
        "review": "Good book",
        "author": "J.R.R. Tolkien",
        "pages": 310,
    }

    client.post("/books", json=book_data)
    client.delete("/media/1")

    response = client.get("/media")

    assert response.status_code == 200
    assert response.get_json() == []