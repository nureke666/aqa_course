from pydantic import BaseModel

author_data = {
    "name": "Джордж Оруэлл",
    "genres": ["Антиутопия", "Сатира", "Политика"],
    "website": None
}

class Author(BaseModel):
    name: str
    genres: list[str]
    website: str | None
    is_alive: bool = False

author = Author.model_validate(author_data)
print(author.genres)
print(author.is_alive)    