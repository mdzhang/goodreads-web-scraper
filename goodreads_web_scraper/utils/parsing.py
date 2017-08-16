import re


def extract_id_from_book_show_link(link):
    """Given a relative url to a book detail page, parse the book's id."""
    match = re.search('/book/show/(?P<id>\d+)-?.*', link)
    return match.group('id') if match else None
