from abc import ABC, abstractmethod

class Base(ABC):
    def __init__(self, comment=""):
        self.comment=comment
        
    @abstractmethod
    def __str__(self):
        pass
        
def Element(Base):
    def __init__(self, label, comment=""):
        Base.__init__(self, comment)
        self.label=label

    @abstractmethod
    def __str__(self):
        pass