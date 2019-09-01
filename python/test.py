class MyClass():
    def __init__(self  ):
        self.x = 10
        self.y = 20
        self.z = self.x  + self.y

my = MyClass()
print(my.z)

l = list( range(3))
print(l)
l[1:2] = [100,200,300]
print( l)

z = list(range(30))
print(z)
z[2:5]=z[9:12]
print(z)

buffer = list( range(30))
print( buffer )
newGapOffset = 5
gapSize = 3

del buffer[gapSize:newGapOffset]
print(buffer)