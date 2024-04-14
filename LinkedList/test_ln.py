import unittest
from linked_node import LinkedNode


class TestLinkedNode(unittest.TestCase):
    """
    Test Cases for LinkedNode

    """
    def setUp(self) -> None:
        self.test_LN: LinkedNode = LinkedNode(1)

    def tearDown(self) -> None:
        self.test_LN = None

    def test_NodesEqual(self):
        """
        Equal LinkedNode comparison.

        """
        try:
            assert self.test_LN == self.test_LN
            self.test_LN.data = 2
            assert self.test_LN == LinkedNode(2)
            print("NodesEqual Passed.\n")
        except:
            self.fail("NodesEqual Failed.\n")
    
    def test_NodesNotEqual(self):
        """
        Not equal LinkedNode comparison.

        """
        try:
            assert self.test_LN != LinkedNode(2)
            self.test_LN.data = 2
            assert self.test_LN != LinkedNode(1)
            print("NodesNotEqual Passed.\n")
        except:
            self.fail("NodesNotEqual Failed.\n")
    
    def test_NodeType(self):
        """
        LinkedNode Type test.

        """
        try:
            self.test_LN = LinkedNode(1)
            assert isinstance(self.test_LN, LinkedNode)
            assert self.test_LN != 1
            print("NodeType Passed.\n")
        except:
            self.fail("NodeType Failed.\n")
        

if __name__ == '__main__':
    unittest.main()
