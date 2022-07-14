from abc import ABC, abstractproperty

class DomainEvent(ABC):

    name: str = abstractproperty()
