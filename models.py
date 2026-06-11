from abc import ABC, abstractmethod


# Creation of the basic media item class and its subclasses for books, movies, and series.
class MediaItem(ABC):

    class RatingValidator:  # Validate the ratings
        @staticmethod
        def validate(rating: float) -> None:
            if rating < 0 or rating > 5:
                raise ValueError("Rating must be between 0 and 5.")

    def __init__(self, title: str, genre: str, status: str, rating: float, review: str):
        self.title = title
        self.genre = genre
        self.status = status
        self.rating = rating
        self.review = review

    @abstractmethod
    def get_type(self) -> str:
        pass

    def mark_completed(self) -> None:
        self.status = "Completed"

    def update_rating(self, rating: float) -> None:
        MediaItem.RatingValidator.validate(rating)
        self.rating = rating


class Book(MediaItem):
    def __init__(
        self,
        title: str,
        genre: str,
        status: str,
        rating: float,
        review: str,
        author: str,
        total_pages: int,
    ):
        super().__init__(title, genre, status, rating, review)
        self.author = author
        self.total_pages = total_pages

    def get_type(self) -> str:
        return "Book"


class Movie(MediaItem):
    def __init__(
        self,
        title: str,
        genre: str,
        status: str,
        rating: float,
        review: str,
        director: str,
        duration: int,
    ):
        super().__init__(title, genre, status, rating, review)
        self.director = director
        self.duration = duration

    def get_type(self) -> str:
        return "Movie"


class Series(MediaItem):
    def __init__(
        self,
        title: str,
        genre: str,
        status: str,
        rating: float,
        review: str,
        creator: str,
        seasons: int,
    ):
        super().__init__(title, genre, status, rating, review)
        self.creator = creator
        self.seasons = seasons

    def get_type(self) -> str:
        return "Series"
