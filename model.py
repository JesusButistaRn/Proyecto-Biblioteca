from dataclasses import dataclass, field

@dataclass
class Book:
    book_id: int
    title: str
    author: str
    year: int
    available: bool = field(default=True)

    def mark_borrowed(self):
        if not self.available:
            raise ValueError("Book is already borrowed")
        self.available = False

    def mark_returned(self):
        self.available = True

@dataclass
class Member:
    member__id: int
    name: str