class Node:
    def __init__(self, val):
        self.val = val
        self.next=  None
    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next

if __name__=="__main__":
    node1 = Node(12)
    node2 = Node(99)
    node3 = Node(37)
    node1.next = node2
    node2.next = node3
    node2.traverse()

class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None