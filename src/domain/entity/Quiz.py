from dataclasses import dataclass
from typing import Type

@dataclass
class Answeres:
    id: str
    description: str

@dataclass
class Questions:
    id: str
    description: str
    answeres: list[Answeres]
    correct_answer: str    


class Quiz:
    def __init__(self, id_quiz: int, questions: Type[list[Questions]]) -> None:
        self._id_quiz = id_quiz
        self._questions = questions

    @property
    def questions(self):
        return self._questions

    @property
    def id_quiz(self):
        return self._id_quiz

    def __repr__(self) -> str:
        return f"Quiz({self.id_quiz!r}, {self.questions!r})"

