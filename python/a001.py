class AbstractGreeting(metaclass=ABCMeta):
    @abstractmethod
    def greeting(self, name):
        pass

class EnglishGreeting(AbstractGreeting):
    def greeting(self, name):
        return 'Hello, %s' % name

class JapaneseGreeting(AbstractGreeting):
    def greeting(self):
        return 'こんにちは、%sさん' % 'John'

print(EnglishGreeting().greeting('John'))
print(JapaneseGreeting().greeting())
