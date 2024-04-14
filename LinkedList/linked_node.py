class LinkedNode:
    """
    Linked Node Implementation

    Attributes:
        data (float): Value of LinkedNode
        next (LinkedNode): Pointer to next LinkedNode
    
    """
    def __init__(self, data):
        self.data: float = data
        self.next: LinkedNode = None
        
    
    def __eq__(self, other):
        if isinstance(other, LinkedNode) is False:
            print("Object is not a LinkedNode, but is: " + str(type(other)))
            return False
        elif self.data != other.data:
            print("LinkedNode " + str(other.data) + " is not equal to LinkedNode " + str(self.data))
            return False
        else:
                print("LinkedNodes " + str(self.data) + " are equal.")
                return True
        
            
        