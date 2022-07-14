from src.domain.event.DomainEvent import DomainEvent


class QuizCorrected(DomainEvent):
    name: str = "QuizCorrected"

    def __init__(self, username: str, email: str, grade: int) -> None:
        self.__username = username
        self.__email = email
        self.__grade = grade

    @property
    def username(self):
        return self.__username

    @property
    def email(self):
        return self.__email
    
    @property
    def grade(self):
        return self.__grade