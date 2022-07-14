from typing import Type
from dataclasses import dataclass

from src.domain.event.QuizSubmitted import QuizSubmitted

from src.infra.mediator.Mediator import Mediator


@dataclass
class Input:
    idQuiz: int
    name: str
    email: str
    answers: dict


class SubmitQuiz:
    def __init__(self, mediator: Type[Mediator]) -> None:                
        self.__mediator = mediator        

    async def execute(self, input: Type[Input]) -> None:         

        event = QuizSubmitted(input)
        await self.__mediator.publish(event)
        
