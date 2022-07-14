from typing import Type

from src.infra.mediator.Mediator import Mediator

from src.application.handler.Handler import Handler

from src.domain.event.QuizCorrected import QuizCorrected
from src.domain.event.QuizSubmitted import QuizSubmitted
from src.domain.repository.QuizRepository import QuizRepository


class QuizCorrectorHandler(Handler):
    eventName: str = "QuizSubmitted"

    def __init__(self, quiz_repository: Type[QuizRepository], mediator: Type[Mediator]) -> None:                
        self.__mediator = mediator
        self.__quiz_repository = quiz_repository      


    async def handle(self, event: QuizSubmitted):
        
        quiz = await self.__quiz_repository.get(event.quiz_props.idQuiz)        

        correct_answer = 0

        for data in quiz:
            for question in data.questions:
                if(event.quiz_props.answers[question.id] == question.correct_answer):
                    correct_answer+=1
                
        grade = round((correct_answer/len(*[data.questions for data in quiz])) * 100)  

        quiz_corrected = QuizCorrected(event.quiz_props.name, event.quiz_props.email, grade)
        await self.__mediator.publish(quiz_corrected)