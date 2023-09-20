from abc import ABC, abstractmethod

class CRUDInterface(ABC):
    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def read(self, criteria):
        pass

    @abstractmethod
    def update(self, criteria, updates):
        pass

    @abstractmethod
    def delete(self, criteria):
        pass
