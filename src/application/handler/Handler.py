from abc import ABC, abstractclassmethod, abstractproperty

from src.domain.event.DomainEvent import DomainEvent

class Handler(ABC):
    
    eventName: str = abstractproperty()

    @abstractclassmethod
    async def handle(event: DomainEvent):
        """handle event by domain name"""
        
        raise NotImplementedError("Method not implemented")