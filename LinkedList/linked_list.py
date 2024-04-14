from linked_node import LinkedNode

class LinkedList:
    """
    Linked List Implementation

    Attributes:
        head (LinkedNode): Head node of a Linked List.

    """
    def __init__(self):
        self.head: LinkedNode = None

    def __eq__(self, other):
        if isinstance(other, LinkedList) is False:
            print("Object is not a LinkedList.")
            return False
        elif self.getSize() != other.getSize():
            print("LinkedList of size: " + str(self.getSize()) + 
                  " is not equal to other LinkedList of size: " + 
                  str(other.getSize()))
            return False
        else:
            current_head: LinkedNode = self.head
            current_other: LinkedNode = other.head
            index: int = 0
            while current_head.next != None and current_other.next != None:
                comp: bool = current_head == current_other 
                if comp is False:
                    print("LinkedLists are not equal at index: " + index)
                    return False
                current_head = current_head.next
                current_other = current_other.next
                index += 1
        return True
    
    def getSize(self):
        size = 0
        current: LinkedNode = self.head
        while self.head is not None:
            size += 1
            current = current.next
        return size
        

    
    def insertAtEnd(self, node: LinkedNode):
        """
        Insert a Node into a LinkedList.

        Args:
            next (LinkedNode): LinkedNode to be inserted at end of LinkedList.

        """
        if self.head is None:
            self.head = node
        elif self.head.next is None:
            self.head.next = node
        else:
            current: LinkedNode = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self.size += 1
    
    def printList(self):
        """
        Prints all of the elements in the Linked List.

        """
        current: LinkedNode = self.head
        index: int = 0
        if index >= self.getSize():
            print("List is empty.")
        while index < self.getSize():
            print("LinkedNode data = " + str(current.data))
            current = current.next
            index += 1

     
    def updateNode(self, val: float, index: int):
        """
        This code defines a method called updateNode in a linked list class. 
        It is used to update the value of a node at a given position in the linked list.

        Args:
            val (float): New value for node.
            index (int): Index of node to update
        
        Raises:
            ValueError: Node does not exist at index.

        """
        current: LinkedNode = self.head
        position: int = 0
        if position == index:
            current.data = val
        else:
            while current != None and position != index:
                current = current.next
                position += 1
            if position == index:
                current.data = val
            else:
                print("Node does not exist at index: " + str(index))
                raise ValueError("Node does not exist at index: " + str(index))
    
    def deleteNode(self, index: int):
        """
        Deletes node of at Linked List.

        Args:
            index (int): Index of node to be deleted.
        Returns:
            self.head: Updated head of LinkedList
        Raises:
            ValueError: Node does not exist at index.

        """
        # Case 0: Head is None
        try:
            assert self.size > 0
        except:
            print("List is empty.")
            raise ValueError("List is empty.")
        current: LinkedNode = self.head
        position: int = 0
        # Case 1: Index at head of List.
        if position == index:
            self.head = current.next
            current = None
        elif position != index and current.next is not None:
            while position + 1 != index and current.next != None:
                # Case 2: Index at end of List.
                if position + 1 == index and current.next.next == None:
                    current.next = None
                # Case 3: Index between head and end of List.
                elif position + 1 == index and current.next.next != None:
                    next: LinkedNode = current.next.next
                    current.next = next
                position += 1
                current = current.next
            # Case 4: LinkedNode does not exist at given index.
        else:
            print("Node does not exist at index: " + str(index))
            raise ValueError("Node does not exist at index: " + str(index))