from models import Book, Movie, Series
from database import DatabaseManager


# Creation of the watchlist manager class and all its operations
class WatchlistManager:
    def __init__(self, database: DatabaseManager):
        self.database = database

    def add_book(self, title, genre, status, rating, review, author, pages) -> None:
        book = Book(title, genre, status, rating, review, author, pages)
        self.database.add_media(book)

    def add_movie(
        self, title, genre, status, rating, review, director, duration
    ) -> None:
        movie = Movie(title, genre, status, rating, review, director, duration)
        self.database.add_media(movie)

    def add_series(
        self, title, genre, status, rating, review, creator, seasons
    ) -> None:
        series = Series(title, genre, status, rating, review, creator, seasons)
        self.database.add_media(series)

    def get_watchlist(self):
        return self.database.get_all_media()

    def delete_item(self, media_id: int) -> None:
        self.database.delete_media(media_id)

    def change_status(self, media_id: int, status: str) -> None:
        self.database.update_status(media_id, status)

    def change_rating(self, media_id: int, rating: float) -> None:
        self.database.update_rating(media_id, rating)
