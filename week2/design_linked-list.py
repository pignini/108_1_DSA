# [Design Linked list](https://leetcode.com/problems/design-linked-list/)

class Node: #創建一個節點分類
    def __init__(self, val=None):
        self.val = val #節點分類屬性val，是節點的值
        self.next = None　#節點分類屬性nexr，是節點下一個指向的值


class MyLinkedList:
    index = 0
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()
    
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        current_node = 0
        while self.next != 0:
            current_node  += 1
            if current_node == index:
                print self.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = node(val) #建立一個新節點
        new_node.next = self.head #把原本的頭節點設定成新節點的下一個
        self.head = new_node #把新節點設立成頭節點
         
    #count node
        current_node = 0
        while self.next != 0:
            current_node  += 1
            return current_node
        
        
            

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = node(val)
        if self.next is None:
            self.next = new_node
            return

        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        self.val = val
        
       
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
