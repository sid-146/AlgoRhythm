from pydantic import BaseModel


class Node(BaseModel):
    # def __init__(self, data) -> None:
    data: str
    next: "Node" = None
    index: int | None = None

    def getData(self):
        return self.data

    def setData(self, value):
        self.data = value

    def getNext(self):
        return self.next

    def getIndex(self):
        return self.index

    def setNext(self, value):
        self.next = value


class Vertex(BaseModel): ...
