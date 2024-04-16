from utils.utils import Node
from pydantic import BaseModel


class LinkedList(BaseModel):
    # def __init__(self) -> None:
    try:
        head: Node | None = None
        size: int = 0
        indexHash: dict | None = {"None": False}
        maxIndex: int = 0
    except Exception as e:
        print(f"Error while initializing class variable : {e}")

    def __isEmpty(self) -> bool:
        return self.head is None

    def __isPresent(self) -> bool: ...

    @staticmethod
    def genIndex(data, size):
        return f"{data}_{size}"

    def addNode(self, data) -> bool:
        try:
            new = Node(**data)
            new.setNext(self.head)
            self.head = new
            self.size += 1
            self.maxIndex = 0
        except Exception as e:
            print(f"Error while adding node : {e}")
            return False
        # self.indexHash.update({self.genIndex(data, self.size) :  'None'})
        return True

    def updateNode(self, index: int, update: str): ...

    def show(self):
        current = self.head
        try:
            while current is not None:
                data = current.getData()
                print(f"|| {data} ||")
                print(f"\t||\t\t")
                current = current.getNext()
        except Exception as e:
            print(f"Failed to show linked list : {e}")

    # def getSize(self) -> int:
    #     current = self.head
    #     size = 0
    #     while current is not None:
    #         size += 1
    #         current = current.getNext()

    #     self.size = size
    #     return self.size

    def deleteNode(self): ...


if __name__ == "__main__":
    obj = LinkedList()
    while True:
        print("1: Add || 2:Print ||0 to exit")
        a = int(input("Enter option"))
        if a == 1:
            res = obj.addNode(data={"data": "Data data for node one"})

            if res:
                print("Node added")
            else:
                print("Failed to add node")
        elif a == 2:
            obj.show()
        elif a == 0:
            break
        else:
            print("Wrong Choice")
