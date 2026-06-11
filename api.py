"""Flask REST API for MediaVault."""

from flask import Flask, jsonify, request

from database import DatabaseManager
from services import WatchlistManager

app = Flask(__name__)

database = DatabaseManager()
manager = WatchlistManager(database)


@app.get("/")
def home():
    """Return a welcome message."""
    return jsonify({"message": "Welcome to the MediaVault API"})


@app.get("/health")
def health():
    """Check if the API is running."""
    return jsonify({"status": "ok"})


@app.get("/media")
def get_media():
    """Return all media items."""
    return jsonify(manager.get_watchlist())


@app.post("/books")
def add_book():
    """Add a book."""
    data = request.get_json()

    manager.add_book(
        data["title"],
        data["genre"],
        data["status"],
        float(data["rating"]),
        data["review"],
        data["author"],
        int(data["pages"]),
    )

    return jsonify({"message": "Book added successfully"}), 201


@app.post("/movies")
def add_movie():
    """Add a movie."""
    data = request.get_json()

    manager.add_movie(
        data["title"],
        data["genre"],
        data["status"],
        float(data["rating"]),
        data["review"],
        data["director"],
        int(data["duration"]),
    )

    return jsonify({"message": "Movie added successfully"}), 201


@app.post("/series")
def add_series():
    """Add a series."""
    data = request.get_json()

    manager.add_series(
        data["title"],
        data["genre"],
        data["status"],
        float(data["rating"]),
        data["review"],
        data["creator"],
        int(data["seasons"]),
    )

    return jsonify({"message": "Series added successfully"}), 201


@app.put("/media/<int:media_id>/status")
def update_status(media_id: int):
    """Update media status."""
    data = request.get_json()

    manager.change_status(
        media_id,
        data["status"],
    )

    return jsonify({"message": "Status updated successfully"})


@app.put("/media/<int:media_id>/rating")
def update_rating(media_id: int):
    """Update media rating."""
    data = request.get_json()

    manager.change_rating(
        media_id,
        float(data["rating"]),
    )

    return jsonify({"message": "Rating updated successfully"})


@app.delete("/media/<int:media_id>")
def delete_media(media_id: int):
    """Delete a media item."""
    manager.delete_item(media_id)

    return jsonify({"message": "Item deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)