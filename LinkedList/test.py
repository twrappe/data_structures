import unittest
# from linked_list import LinkedList
from linked_node import LinkedNode

class TestLinkedNode(unittest.TestCase):
    """
    Test Cases for LinkedLists

    """
    def setUp(self) -> None:
        self.test_LN: LinkedNode = None

    def tearDown(self) -> None:
        self.test_LN = None

    def test_nodeEq(self):
            try:
                print("Running Node Equality Tests.")
                print("Initial Test Node 1.")
                self.test_LN = LinkedNode(1)
                assert self.test_LN == LinkedNode(1)
                assert self.test_LN != LinkedNode(2)
                print("Changing Test Node to 2.")
                self.test_LN.data = 2
                assert self.test_LN == LinkedNode(2)
                assert self.test_LN != LinkedNode(1)
                assert self.test_LN != 1
                assert self.test_LN != None
                print("Node Equality Tests Passed.")
            except:
                 self.fail("Node Equality Tests Failed.")

# class TestLinkedList(unittest.TestCase):
#     def setUp(self):
#          self.test_LL: LinkedList = None

#     def tearDown(self) -> None:
#         while self.test_LL is not None:
#             self.test_LL
    # def test_checkEnd(self) -> bool:
    #     """
    #     Checks the value of the linked List at 
    #     """
    #     data= 1
    #     head_node: LinkedNode = LinkedNode(data)
    #     self.LL.insertAtEnd(head_node)
    #     assert self.LL.head.data == data
    #     data = 2
    #     next_node: LinkedNode = LinkedNode(data)
    #     self.LL.i

if __name__ == '__main__':
    unittest.main()
        
        
        

