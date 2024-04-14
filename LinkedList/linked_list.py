# from LinkedList.linked_node import LinkedNode

# class LinkedList:
#     """
#     Linked List Implementation

#     Attributes:
#         head (LinkedNode): Head node of a Linked Lists

#     """
#     def __init__(self):
#         self.head: LinkedNode = None

    # def __eq__(self, other):
    #     if self.head is None and other.head is None:
    #         return False
    #     elif self.next is None and other.head.next is None:
    #         assert self.head.data == other.head.data
    #     else:
    #         current_head: LinkedNode = self.head
    #         currennt_other: LinkedNode = other.head
    #         while current_head.next != None and currennt_other.next != None:
    #             if self.head.data != other.head.data:
    #                 return False
    #             current_head = current_head.next
    #             other_head = other_head.next
    #     if current_head.next is None and currennt_other.next is None:
    #         assert current_head.data == currennt_other.data
    #     else:
    #         return False

    
    # def insertAtEnd(self, next: LinkedNode):
    #     """
    #     Insert a Node into a LinkedList.

    #     Args:
    #         next (LinkedNode): LinkedNode to be inserted at end of LinkedList.

    #     """
    #     if self.head is None:
    #         self.head = next
    #     else:
    #         self.head.next = next
    
   
    
    # def updateNode(self, val: float, index: int):
    #     """
    #     This code defines a method called updateNode in a linked list class. 
    #     It is used to update the value of a node at a given position in the linked list.

    #     Args:
    #         val (float): New value for node.
    #         index (int): Index of node to update
        
    #     Raises:
    #         ValueError: Node does not exist at index.

    #     """
    #     current: LinkedNode = self.head
    #     position: int = 0
    #     if position == index:
    #         current.data = val
    #     else:
    #         while current != None and position != index:
    #             current = current.next
    #             position += 1
    #         if position == index:
    #             current.data = val
    #         else:
    #             print("Node does not exist at index: " + str(index))
    #             raise ValueError("Node does not exist at index: " + str(index))
    
    # def deleteNode(self, index: int):
    #     """
    #     Deletes node of at Linked List.

    #     Args:
    #         index (int): Index of node to be deleted.
    #     Returns:
    #         self.head: Updated head of LinkedList
    #     Raises:
    #         ValueError: Node does not exist at index.

    #     """
    #     # Case 0: Head is None
    #     if self.head is None:
    #         pass
    #     else:
    #         current: LinkedNode = self.head
    #         position: int = 0
    #         # Case 1: Index at head of List.
    #         if position == index:
    #             self.head = current.next
    #             current = None
    #         else:
    #             while position != index and current.next != None:
    #                 # Case 2: Index at end of List.
    #                 if position + 1 == index and current.next.next == None:
    #                     current.next = None
    #                 # Case 3: Index between head and end of List.
    #                 elif position + 1 == index and current.next.next != None:
    #                     next: LinkedNode = current.next.next
    #                     current.next = next
    #             # Case 4: LinkedNode does not exist at given index.
    #             else:
    #                     print("Node does not exist at index: " + str(index))
    #                     raise ValueError("Node does not exist at index: " + str(index))