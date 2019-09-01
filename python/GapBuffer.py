class GapBuffer():
    INITIAL_GAP_SIZE = 4
    gapOffset = 0
    gapSize = INITIAL_GAP_SIZE

    def __init__( self,  text):
        self.buffer = list( text)
        self.buffer[0:0]= [ '' for i in range( self.gapSize)]
#        print( self.buffer)
    def confirmGap( self, newGapOffset  ):
#        print( "newGapOffset:" , newGapOffset)
        if self.gapSize == 0 :
            print( self.gapSize , "==", 0)
            self.tmp = ['' for k in range(self.INITIAL_GAP_SIZE)]
            print( "self.tmp   :", self.tmp)
            print( "self.buffer:", self.buffer)
            self.tmp = self.tmp + self.buffer
            print( "self.tmp   :", self.tmp)
            self.gapOffset = len(self.buffer)
            self.gapSize = self.INITIAL_GAP_SIZE
            self.buffer = self.tmp
        if newGapOffset < self.gapOffset :
            print ( "newGapOffset < self.gapOffset ")
            moveLen = self.gapOffset - newGapOffset+1
            self.buffer[newGapOffset:moveLen] = self.buffer[newGapOffset+self.gapSize:moveLen]
        else:
            print ( "newGapOffset >= self.gapOffset ")
            moveLen = newGapOffset - self.gapOffset+1
            movePos = self.gapOffset+self.gapSize
            print( "moveLen:", moveLen)
            print( "movePos:", movePos)
            del self.buffer[movePos:moveLen]
            print(  self.buffer)
            print( "self.buffer[self.gapOffset:moveLen] = ", self.buffer[self.gapOffset:moveLen])
            self.buffer[movePos:moveLen]  = self.buffer[self.gapOffset:moveLen]
            print( "line 29 ", self.buffer )
    def insert( self, offset, ch):
        print( "insert() start...")
        self.printParameter()
        self.confirmGap(  offset)
        self.printParameter()
        self.buffer[self.gapOffset]=ch
        self.gapOffset += 1
        self.gapSize -= 1
        print( self.buffer) 
        self.printParameter()
    
# here is for debug.
    def printParameter(self):
        print( "====")
        print("self.buffer:", self.buffer )
        print("self.gapOffset:", self.gapOffset)
        print("self.gapSize:",self.gapSize)
        print( "----")

#
mem = GapBuffer( "hello")
mem.insert( 2,"a")

