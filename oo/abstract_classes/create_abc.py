from abc import ABCMeta, abstractmethod

# Force implementation of str method in subclasses 
class Program(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self) -> str:
        pass