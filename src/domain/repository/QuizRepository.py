from abc import ABC, abstractclassmethod

class QuizRepository(ABC):

    @abstractclassmethod
    async def get(id_quiz: int):
        """Get all quizs"""

        raise NotImplementedError("Method not implemented")
        