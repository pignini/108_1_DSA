class Node: #創建一個節點分類
    def __init__(self, val=None):
        self.val = val #節點分類屬性val，是節點的值
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        current_index = 0
        curr_node = self.head
        while current_index != index :
            current_index += 1
            curr_node = curr_node.next
            print(curr_node.val)
            return

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val) #建立一個新節點
        cur_node = self.head
        if cur_node.next == None:
            head = new_node 
            cur_node.next = new_node
        else:
            cur_node = cur_node.next
            original_head = cur_node
            head = new_node
            new_nod.next = original_head
            
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val) #建立一個新的節點
        current_node = self.head
        while current_node.next != None: 
            current_node = current_node.next
        current_node.next = new_node
        
            
        
        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        new_node = Node(val)
        curr_index = 1
        curr_node = self.head
        cur_node = self.head
        
        count_index = 1
        while cur_node.next != None:
            count_index += 1
            return
        
        if index == count_index:
            addAtTail(index)
        elif index > count_index:
            pass
        else:
            while curr_index != index:
                curr_index += 1
                curr_node = curr_node.next
            pre_node = curr_node
            old_node = curr_node.next
            pre_node.next = new_node
            new_node.next = old_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        cur_node = self.head
        
        count_index = 1
        while cur_node.next != None:
            count_index += 1
            return
        
        if index >= count_index:
            pass
        else:
            cur_index = 1
            cur_index2 = -1
            cur_node = self.head
            cur_node2 = self.head
            while index != cur_index:
                cur_index += 1
                cur_node = cur_node.next
            while index != cur_index2:
                cur_index2 += 1
                cur_node2 = cur_node2.next
            
            pre_node = cur_node
            back_node = cur_node2
            pre_node.next = back_node
            

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
