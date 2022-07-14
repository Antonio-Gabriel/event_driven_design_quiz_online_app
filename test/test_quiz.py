from unittest import TestCase

from src.domain.entity.Quiz import Quiz, Questions, Answeres

class TestQuiz(TestCase):
    def test_quiz(self):
        """Create a quiz"""

        questions = [
            Questions(
                id=1, 
                description="Javascript is good?",
                answeres=[
                    Answeres("a", "Yes"),
                    Answeres("b", "No")
                ],
                correct_answer="a"
            ),
            Questions(
                id=2, 
                description="Typescript is better than javascript?",
                answeres=[
                    Answeres("a", "Yes"),
                    Answeres("b", "No")
                ],
                correct_answer="a"
            )
        ]
        
        quiz = Quiz(1, questions)                    

        self.assertEqual(quiz.questions[0].id, 1, "question doesn't equals")
        self.assertEqual(quiz.id_quiz, 1, "is not equal")

        self.assertEqual(len(questions), 2)        
