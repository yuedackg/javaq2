class AbstractHello( metaclass=ABCMeta):
    @abstractmethod
    def Hello( self):
        pass

class WrongHello ( AbstractHello):
    pass

w = WrongHello()

