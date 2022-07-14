from src.application.handler.Handler import Handler
from src.domain.event.DomainEvent import DomainEvent


class Mediator:
    def __init__(self) -> None:
        self.__hendlers: list[Handler] = []

    def regieter(self, handler: Handler):
        self.__hendlers.append(handler)

    async def publish(self, event: DomainEvent):
        for handler in self.__hendlers:                        
            if(handler.eventName == event.name):
                await handler.handle(event)
            
        