from typing import Type
from dataclasses import dataclass

from src.domain.event.DomainEvent import DomainEvent

@dataclass
class Input:
    idQuiz: int
    name: str
    email: str
    answers: dict

class QuizSubmitted(DomainEvent):
    name: str = "QuizSubmitted"

    def __init__(self, quiz_props: Type[Input]) -> None:
        self.__quiz_props = quiz_props


    @property
    def quiz_props(self):
        return self.__quiz_props


    def __repr__(self) -> str:
        return f"""
            QuizSubmitted(
                {self.__quiz_props.idQuiz!r}, {self.__quiz_props.name!r}, 
                {self.__quiz_props.email!r}, {self.__quiz_props.answers!r}
            )
        """


