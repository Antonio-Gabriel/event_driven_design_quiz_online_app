from dataclasses import dataclass

from src.application.service.Mailer import Mailer

@dataclass
class Message:
    recipient: str
    message: str


class MailerMemory(Mailer):

    def __init__(self) -> None:
        self.messages: list[Message] = []

    async def send(self, recipient: str, message: str):
        self.messages.append(Message(
            recipient=recipient,
            message=message
        ))

        print(message)