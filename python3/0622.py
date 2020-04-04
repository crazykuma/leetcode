class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size=k
        self.queue=["" for i in range(k)]
        self.pos=[0 for i in range(k)]
        # self.head = -1
        # self.tail = -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head=0
            self.tail=0
            self.queue[self.tail]=value
            self.pos[self.tail]=1
            return True
        else:
            self.tail=(self.tail+1)%self.size
            self.queue[self.tail]=value
            self.pos[self.tail]=1
            return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.queue[self.head]=""
            self.pos[self.head]=0
            self.head=(self.head+1)%self.size
            return True
        
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.tail]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if sum(self.pos)==0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if sum(self.pos)==self.size:
            return True
        else:
            return False


if __name__ == "__main__":
    s=MyCircularQueue(3)
    print(s.enQueue(1))
    print(s.enQueue(2))
    print(s.enQueue(3))
    print(s.enQueue(4))
    print(s.Rear())
    print(s.isFull())
    print(s.deQueue())
    print(s.enQueue(4))
    print(s.Rear())
