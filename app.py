#Frontend Streamlit app for MediaVault - Personal Watchlist Tracker

import logging

import requests
import streamlit as st

API_URL = st.secrets.get("API_URL", "http://127.0.0.1:5000")

logging.basicConfig(
    filename="mediavault.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

st.set_page_config(page_title="MediaVault", page_icon=":clapper:")

st.title("Personal MediaVault")
st.subheader("Movie, Book, and Series Watchlist Tracker")
st.divider()

menu = st.sidebar.selectbox("Menu", ["Add Item", "View Watchlist", "Update Item"])


def get_media_items():
    """Get all media items from the Flask API."""
    response = requests.get(f"{API_URL}/media", timeout=5)
    response.raise_for_status()
    return response.json()


def display_items(media_items):
    """Display media items in Streamlit."""
    for item in media_items:
        st.write("---")
        st.write(f"**ID:** {item[0]}")
        st.write(f"**Title:** {item[2]}")
        st.write(f"**Genre:** {item[3]}")
        st.write(f"**Status:** {item[4]}")
        st.write(f"**Rating:** {item[5]}/5")
        st.write(f"**Review:** {item[6]}")
        st.write(f"**Creator / Author / Director:** {item[7]}")

        if item[1] == "Book":
            st.write(f"**Pages:** {item[8]}")
        elif item[1] == "Movie":
            st.write(f"**Duration:** {item[8]} minutes")
        elif item[1] == "Series":
            st.write(f"**Seasons:** {item[8]}")


if menu == "Add Item":
    st.subheader("Add New Media")

    media_type = st.selectbox("Type", ["Book", "Movie", "Series"])
    title = st.text_input("Title")
    genre = st.text_input("Genre")
    status = st.selectbox("Status", ["Planned", "In Progress", "Completed", "Dropped"])
    rating = st.slider("Rating", min_value=0.0, max_value=5.0, value=0.0, step=0.5)
    review = st.text_area("Review")

    if media_type == "Book":
        author = st.text_input("Author")
        pages = st.number_input("Pages", min_value=1)

        if st.button("Add Book"):
            try:
                response = requests.post(
                    f"{API_URL}/books",
                    json={
                        "title": title,
                        "genre": genre,
                        "status": status,
                        "rating": rating,
                        "review": review,
                        "author": author,
                        "pages": int(pages),
                    },
                    timeout=5,
                )
                response.raise_for_status()
                logging.info("Added book: %s by %s", title, author)
                st.success("Book added successfully!")

            except requests.exceptions.RequestException as error:
                logging.error("API error adding book: %s", error)
                st.error("Could not connect to the API. Make sure Flask is running.")
            except ValueError as error:
                logging.error("Validation error adding book: %s", error)
                st.error(str(error))

    elif media_type == "Movie":
        director = st.text_input("Director")
        duration = st.number_input("Duration in minutes", min_value=1)

        if st.button("Add Movie"):
            try:
                response = requests.post(
                    f"{API_URL}/movies",
                    json={
                        "title": title,
                        "genre": genre,
                        "status": status,
                        "rating": rating,
                        "review": review,
                        "director": director,
                        "duration": int(duration),
                    },
                    timeout=5,
                )
                response.raise_for_status()
                logging.info("Added movie: %s directed by %s", title, director)
                st.success("Movie added successfully!")

            except requests.exceptions.RequestException as error:
                logging.error("API error adding movie: %s", error)
                st.error("Could not connect to the API. Make sure Flask is running.")
            except ValueError as error:
                logging.error("Validation error adding movie: %s", error)
                st.error(str(error))

    elif media_type == "Series":
        creator = st.text_input("Creator")
        seasons = st.number_input("Number of seasons", min_value=1)

        if st.button("Add Series"):
            try:
                response = requests.post(
                    f"{API_URL}/series",
                    json={
                        "title": title,
                        "genre": genre,
                        "status": status,
                        "rating": rating,
                        "review": review,
                        "creator": creator,
                        "seasons": int(seasons),
                    },
                    timeout=5,
                )
                response.raise_for_status()
                logging.info("Added series: %s created by %s", title, creator)
                st.success("Series added successfully!")

            except requests.exceptions.RequestException as error:
                logging.error("API error adding series: %s", error)
                st.error("Could not connect to the API. Make sure Flask is running.")
            except ValueError as error:
                logging.error("Validation error adding series: %s", error)
                st.error(str(error))


elif menu == "View Watchlist":
    st.header("Your Watchlist")

    try:
        items = get_media_items()

        if not items:
            st.info("No items added yet.")
        else:
            books = [item for item in items if item[1] == "Book"]
            movies = [item for item in items if item[1] == "Movie"]
            series = [item for item in items if item[1] == "Series"]

            with st.expander("📚 Books", expanded=False):
                if books:
                    display_items(books)
                else:
                    st.info("No books added yet.")

            with st.expander("🎬 Movies", expanded=False):
                if movies:
                    display_items(movies)
                else:
                    st.info("No movies added yet.")

            with st.expander("📺 Series", expanded=False):
                if series:
                    display_items(series)
                else:
                    st.info("No series added yet.")

    except requests.exceptions.RequestException as error:
        logging.error("API error loading media: %s", error)
        st.error("Could not load media items. Make sure the Flask API is running.")


elif menu == "Update Item":
    st.header("Update or Delete Item")

    try:
        items = get_media_items()

        if items:
            st.info("Use the item ID shown in the View Watchlist page.")
        else:
            st.info("No items available to update or delete.")

    except requests.exceptions.RequestException as error:
        logging.error("API error loading update page: %s", error)
        st.error("Could not load media items. Make sure the Flask API is running.")

    media_id = st.number_input("Enter Item ID", min_value=1)

    new_status = st.selectbox(
        "New Status", ["Planned", "In Progress", "Completed", "Dropped"]
    )

    if st.button("Update Status"):
        try:
            response = requests.put(
                f"{API_URL}/media/{int(media_id)}/status",
                json={"status": new_status},
                timeout=5,
            )
            response.raise_for_status()
            logging.info("Updated status for item %s to %s", media_id, new_status)
            st.success("Status updated successfully!")

        except requests.exceptions.RequestException as error:
            logging.error("API error updating status: %s", error)
            st.error("Could not update status. Make sure the Flask API is running.")

    new_rating = st.slider(
        "New Rating", min_value=0.0, max_value=5.0, value=0.0, step=0.5
    )

    if st.button("Update Rating"):
        try:
            response = requests.put(
                f"{API_URL}/media/{int(media_id)}/rating",
                json={"rating": new_rating},
                timeout=5,
            )
            response.raise_for_status()
            logging.info("Updated rating for item %s to %s", media_id, new_rating)
            st.success("Rating updated successfully!")

        except requests.exceptions.RequestException as error:
            logging.error("API error updating rating: %s", error)
            st.error("Could not update rating. Make sure the Flask API is running.")

    if st.button("Delete Item"):
        try:
            response = requests.delete(f"{API_URL}/media/{int(media_id)}", timeout=5)
            response.raise_for_status()
            logging.info("Deleted item with ID: %s", media_id)
            st.warning("Item deleted.")

        except requests.exceptions.RequestException as error:
            logging.error("API error deleting item: %s", error)
            st.error("Could not delete item. Make sure the Flask API is running.")