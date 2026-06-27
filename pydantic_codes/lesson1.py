from pydantic import BaseModel

book_data = {
    "title": "Гарри Поттер и философский камень",
    "pages": 332,
    "rating": 4.8,
    "is_bestseller": True,
}


class Book(BaseModel):
    title: str
    pages: int
    rating: float
    is_bestseller: bool


my_book = Book.model_validate(book_data)
print(my_book.title)
print(my_book.rating)
