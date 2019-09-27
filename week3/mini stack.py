class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val = val
        self.size = 0
        self.next = None

    def push(self, x: int) -> None:
        self.size += 1
        while self.size == 1:
            top = current = self.val
        while self.size != 0 or 1:
            current.next = self.val
            top = self.val
            current = current.next

    def pop(self) -> None:
        

    def top(self) -> int:
        

    def getMin(self) -> int:
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
