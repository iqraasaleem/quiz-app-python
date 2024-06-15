from sqlmodel import SQLModel,Field
from typing import Optional


class Category(SQLModel, table=True):
    category_id: Optional[int] = Field(None, primary_key=True)
    category_name: str
    category_discription: str

class QuizLevel(SQLModel, table=True):
    quiz_level_id: Optional[int] = Field(None, primary_key=True)
    quiz_level: str
    category_id: int = Field(int, foreign_key="category.category_id")
    

class Quiz(SQLModel, table=True):
    quesion_id: Optional[int] = Field(None, primary_key=True)
    quesion: str
    quizlevel_id: int = Field(int, foreign_key="quizlevel.quiz_level_id")

class Choices(SQLModel,table=True):
    choice_id: Optional[int] = Field(None, primary_key=True)
    choice: str
    quesion_id: int = Field(int, foreign_key="quiz.quesion_id")
    staus:bool = False

