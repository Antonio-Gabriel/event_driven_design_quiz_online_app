from src.domain.entity.Quiz import Quiz, Questions, Answeres
from src.domain.repository.QuizRepository import QuizRepository


class QuizRepositoryMemory(QuizRepository):
    
    def __init__(self) -> None:
        self.quizzes: list[Quiz] = [
            Quiz(
                id_quiz=1,
                questions=[
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
            )
        ]

    async def get(self, id_quiz: int):
        quiz = list(filter(lambda qz: qz.id_quiz == id_quiz, self.quizzes))
        
        return quiz