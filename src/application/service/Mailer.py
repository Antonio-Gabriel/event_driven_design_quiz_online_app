from abc import ABC, abstractclassmethod


class Mailer(ABC):

    @abstractclassmethod
    async def send(recipient: str, message: str):
        """Send email to recipient with message"""
        
        raise NotImplementedError("Method not implemented")