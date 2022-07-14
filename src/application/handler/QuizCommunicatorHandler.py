from typing import Type

from src.domain.event.QuizCorrected import QuizCorrected

from src.application.service.Mailer import Mailer
from src.application.handler.Handler import Handler


class QuizCommunicatorHandler(Handler):
    eventName: str = "QuizCorrected"

    def __init__(self, mailer: Type[Mailer]) -> None:
        self.__mailer = mailer


    async def handle(self, event: QuizCorrected):
        await self.__mailer.send(event.email, f"Hello {event.username}, your quiz note is {event.grade}")