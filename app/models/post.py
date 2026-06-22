from sqlmodel import SQLModel, Field

class Post(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    competitor: str
    likes: int
    comments: int