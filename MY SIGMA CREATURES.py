from abc import ABC, abstractmethod
class mycreatures(ABC):
    def move(self):
        pass


class me(mycreatures):
    def move(self):
        print("i can walk because i am a human being")


class snake(mycreatures):
    def move(self):
        print("i can slither and crawl")

class ishowspeed(mycreatures):
    def move(self):
        print("i can bark arrggghhh arrghhhh suiiiiiiiiiiii")

class lion(mycreatures):
    def move(self):
        print("i can roar")

R = me()
R.move()

K = snake()
K.move()

R = ishowspeed()
R.move()

K = lion()
K.move()