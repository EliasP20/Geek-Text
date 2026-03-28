from sqlalchemy.orm import Session
from app.models import Author

from sqlalchemy import func

from app.schemas.author import AuthorCreate

def create_author(db: Session, author: AuthorCreate):
    author = Author(
        first_name=author.first_name,
        last_name=author.last_name,
        biography=author.biography,
        publisher=author.publisher
    )
    db.add(author)
    db.commit()
    db.refresh(author)
    return author
 