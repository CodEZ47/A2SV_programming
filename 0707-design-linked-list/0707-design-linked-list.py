class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.count = 0
    #######################################    
    def printList(self):
        curr = self.head
        arr = []
        
        while curr:
            arr.append("[" + str(curr.value) + "]")
            arr.append("->")
            curr = curr.next
        arr.append("[None]")
        print(arr)
        print(self.count)
    
    def getNodeAtInd(self, ind):
        ind = ind + 1
        # print("getNodeAtInd", ind)
        if ind > self.count:
            return -1
        curr = self.head
        
        for i in range(1,ind):
            curr = curr.next
        return curr
    ####################################################
    
    def get(self, index: int) -> int:
        # print("get")
        curr = self.getNodeAtInd(index)
        
        if curr != -1:
            # print(curr.value)
            return curr.value
        else:
            return curr

    def addAtHead(self, val: int) -> None:
        # print("addAtHead")
        if self.count == 0:
            self.head = Node(val)
            self.count += 1
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
            self.count += 1
        return

    def addAtTail(self, val: int) -> None:
        # print("addAtTail")
        if self.count == 0:
            self.head = Node(val)
            self.count += 1
        else:
            curr = self.getNodeAtInd(self.count-1)   
            curr.next = Node(val)
            self.count += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        # print("addAtIndex")
        if index == 0:
            self.addAtHead(val)
        elif index > self.count:
            return
        elif index == self.count:
            self.addAtTail(val)
        else:
            curr = self.getNodeAtInd(index-1)
            newNode = Node(val)
            newNode.next = curr.next
            curr.next = newNode
            self.count += 1
        
        return

    def deleteAtIndex(self, index: int) -> None:
        if self.count == 0:
            return
        if index == 0:
            self.head = self.head.next
            self.count -= 1
        elif index + 1 == self.count:
            curr = self.getNodeAtInd(index-1)
            curr.next = None
            self.count -= 1
        elif index >= self.count:
            return
        else:
            curr = self.getNodeAtInd(index-1)
            curr.next = curr.next.next
            self.count -= 1
        
        return


# newLL = MyLinkedList()
# newLL.deleteAtIndex(0)
# newLL.addAtHead(1)
# newLL.addAtTail(1)
# newLL.addAtIndex(1,2)
# newLL.addAtIndex(3,4)
# newLL.addAtIndex(0,0)
# newLL.deleteAtIndex(2)
# newLL.deleteAtIndex(2)
# newLL.deleteAtIndex(2)
# newLL.deleteAtIndex(2)
# newLL.printList()


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)