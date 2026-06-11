import sqlite3
from models import Book, Movie, Series


# Creation of the database manager class to handle all interactions with the SQLite database
class DatabaseManager:
    def __init__(self, db_name: str = "mediavault.db"):
        self.db_name = db_name
        self.create_table()

    # Connects the application to the SQLite database and returns the connection object for the queries to be able to be executed
    def connect(self):
        return sqlite3.connect(self.db_name)

    # create the table where the data is going to be stored when the manager is initialized
    def create_table(self) -> None:
        with self.connect() as conn:  # creates connection to the database and ensures it is properly closed after the block is executed
            cursor = conn.cursor()
            # creation of the table columns with the data type
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS media (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type TEXT NOT NULL,
                    title TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    status TEXT NOT NULL,
                    rating REAL NOT NULL,
                    review TEXT,
                    creator TEXT,
                    extra_info INTEGER
                )
            """)
            conn.commit()  # save changes

    # Adds the extra information for each media type
    def add_media(self, media_item: Book | Movie | Series) -> None:
        """Add a media item to the database."""
        if isinstance(media_item, Book):
            creator = media_item.author
            extra_info = media_item.total_pages

        elif isinstance(media_item, Movie):
            creator = media_item.director
            extra_info = media_item.duration

        elif isinstance(media_item, Series):
            creator = media_item.creator
            extra_info = media_item.seasons

        else:
            raise TypeError("Unsupported media type.")

        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO media
                (type, title, genre, status, rating, review, creator, extra_info)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    media_item.get_type(),
                    media_item.title,
                    media_item.genre,
                    media_item.status,
                    media_item.rating,
                    media_item.review,
                    creator,
                    extra_info,
                ),
            )
            conn.commit()

    # Returns the items stored in the database
    def get_all_media(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM media")
            return cursor.fetchall()

    # Deletes the item with the specified ID from the database
    def delete_media(self, media_id: int) -> None:
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM media WHERE id = ?", (media_id,))
            conn.commit()

    # Updates the the item with the specified ID in the database
    def update_status(self, media_id: int, status: str) -> None:
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE media SET status = ? WHERE id = ?", (status, media_id)
            )
            conn.commit()

    def update_rating(self, media_id: int, rating: float) -> None:
        if rating < 0 or rating > 5:
            raise ValueError("Rating must be between 0 and 5.")

        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE media SET rating = ? WHERE id = ?", (rating, media_id)
            )
            conn.commit()
