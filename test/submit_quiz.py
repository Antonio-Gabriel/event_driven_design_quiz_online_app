import asyncio

from unittest import TestCase

from src.application.usecase.SubmitQuiz import SubmitQuiz, Input
from src.application.handler.QuizCorrectorHandler import QuizCorrectorHandler
from src.application.handler.QuizCommunicatorHandler import QuizCommunicatorHandler

from src.infra.mediator.Mediator import Mediator
from src.infra.service.MailerMemory import MailerMemory
from src.infra.repository.QuizRepositoryMemory import QuizRepositoryMemory


class SubmitTest(TestCase):

    # def test_submit(self):
    #     """A user subscribe a quiz response"""
        
    #     quiz_repository = QuizRepositoryMemory()
    #     submit_quiz = SubmitQuiz(quiz_repository)
        
    #     input = Input(
    #         idQuiz=1,
    #         name="John Doe",
    #         email="john.doe@gmail.com",
    #         answers={
    #             1: "a",
    #             2: "b"
    #         }
    #     )
    
    #     output = asyncio.run(submit_quiz.execute(input))
                
    #     self.assertEqual(output.grade, 50) 
    
    def test_notify_by_email_after_submit_quiz(self):
        """Notify to user after submit the quiz"""

        mediator = Mediator()
        quiz_repository = QuizRepositoryMemory()
        quiz_corrector_handler = QuizCorrectorHandler(quiz_repository, mediator)
        mediator.regieter(quiz_corrector_handler)
        
        mailer = MailerMemory()
        quiz_communicator_handler = QuizCommunicatorHandler(mailer)
        mediator.regieter(quiz_communicator_handler)

        submit_quiz = SubmitQuiz(mediator)
        
        input = Input(
            idQuiz=1,
            name="John Doe",
            email="john.doe@gmail.com",
            answers={
                1: "a",
                2: "b"
            }
        )
    
        asyncio.run(submit_quiz.execute(input))
        
        self.assertEqual(mailer.messages[0].message, "Hello John Doe, your quiz note is 50") 