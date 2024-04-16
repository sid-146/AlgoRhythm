import numpy as np 

class Utils:
    def __init__(self) -> None:
        self.listSize = 10
        self.startRange = 1
        self.endRange = 15

    def getRandomArray(self, size:int=None, start:int=None, end:int =None):
        if not size:
            size = self.listSize
        if not start:
            start = self.startRange
        if not end:
            end = self.endRange
        arr = np.random.randint(start,end,size).tolist()
        return arr