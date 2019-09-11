class News:
    """Breaking news with title, description, author and original source"""

    def __init__(self, author, title, description, url, date_posted, query):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.date_posted = date_posted
        self.query = query

    def __str__(self):
        return f'Author: {self.author}\nTitle: {self.title}\nDate posted: {self.date_posted}\nURL: {self.url}'
