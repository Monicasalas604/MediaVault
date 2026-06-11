import pytest

from database import DatabaseManager
from services import WatchlistManager


@pytest.fixture
def manager(tmp_path):
    test_db = tmp_path / "test_mediavault.db"
    database = DatabaseManager(str(test_db))
    return WatchlistManager(database)


def test_add_book_with_manager(manager):
    manager.add_book("Dune", "Sci-Fi", "Planned", 4.5, "Good", "Frank Herbert", 500)

    items = manager.get_watchlist()

    assert len(items) == 1
    assert items[0][1] == "Book"


def test_add_movie_with_manager(manager):
    manager.add_movie(
        "Inception",
        "Sci-Fi",
        "Completed",
        5.0,
        "Great",
        "Christopher Nolan",
        148,
    )

    items = manager.get_watchlist()

    assert len(items) == 1
    assert items[0][1] == "Movie"


def test_add_series_with_manager(manager):
    manager.add_series("Dark", "Sci-Fi", "Completed", 5.0, "Excellent", "Baran", 3)

    items = manager.get_watchlist()

    assert len(items) == 1
    assert items[0][1] == "Series"


def test_change_status_with_manager(manager):
    manager.add_book("Dune", "Sci-Fi", "Planned", 4.5, "Good", "Frank Herbert", 500)
    item_id = manager.get_watchlist()[0][0]

    manager.change_status(item_id, "Completed")
    updated_item = manager.get_watchlist()[0]

    assert updated_item[4] == "Completed"


def test_change_rating_with_manager(manager):
    manager.add_book("Dune", "Sci-Fi", "Planned", 4.5, "Good", "Frank Herbert", 500)
    item_id = manager.get_watchlist()[0][0]

    manager.change_rating(item_id, 5.0)
    updated_item = manager.get_watchlist()[0]

    assert updated_item[5] == 5.0


def test_delete_item_with_manager(manager):
    manager.add_book("Dune", "Sci-Fi", "Planned", 4.5, "Good", "Frank Herbert", 500)
    item_id = manager.get_watchlist()[0][0]

    manager.delete_item(item_id)

    assert len(manager.get_watchlist()) == 0


def test_invalid_rating_raises_error(manager):
    manager.add_book("Dune", "Sci-Fi", "Planned", 4.5, "Good", "Frank Herbert", 500)
    item_id = manager.get_watchlist()[0][0]

    with pytest.raises(ValueError):
        manager.change_rating(item_id, 6.0)