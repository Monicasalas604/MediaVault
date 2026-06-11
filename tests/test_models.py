import pytest

from models import Book, MediaItem, Movie, Series


def test_book_get_type():
    book = Book("Dune", "Sci-Fi", "Planned", 4.5, "Good", "Frank Herbert", 500)
    assert book.get_type() == "Book"


def test_movie_get_type():
    movie = Movie(
        "Inception", "Sci-Fi", "Completed", 5.0, "Great", "Christopher Nolan", 148
    )
    assert movie.get_type() == "Movie"


def test_series_get_type():
    series = Series("Dark", "Sci-Fi", "Completed", 5.0, "Excellent", "Baran bo Odar", 3)
    assert series.get_type() == "Series"


def test_mark_completed():
    book = Book("Dune", "Sci-Fi", "Planned", 4.5, "Good", "Frank Herbert", 500)

    book.mark_completed()

    assert book.status == "Completed"


def test_update_rating_valid():
    book = Book("Dune", "Sci-Fi", "Planned", 4.0, "Good", "Frank Herbert", 500)

    book.update_rating(5.0)

    assert book.rating == 5.0


def test_rating_validator_accepts_valid_rating():
    MediaItem.RatingValidator.validate(3.5)


def test_rating_validator_rejects_high_rating():
    with pytest.raises(ValueError):
        MediaItem.RatingValidator.validate(6.0)


def test_rating_validator_rejects_low_rating():
    with pytest.raises(ValueError):
        MediaItem.RatingValidator.validate(-1.0)
