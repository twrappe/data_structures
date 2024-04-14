import unittest
from linked_list import LinkedList
import time


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        """
        Setup LinkedList Test Environment.

        """
        self.test_LL: LinkedList = LinkedList()
        assert self.test_LL.head is None
        assert self.test_LL.getSize() == 0

    def tearDown(self) -> None:
        """
        Teardown LinkedList Test Environment.

        """
        while self.test_LL.head is not None:
            self.test_LL.deleteNode(0)
        assert self.test_LL.getSize() == 0
        assert self.test_LL.head is None
        self.test_LL = None
    
    def test_ListEq(self) -> None:
        """
        LinkedList Equality Tests.

        """
        pass

    def test_ListAccessSpeed(self) -> None:
        """
        LinkedList Access Speed Tests.

        """
        pass   

if __name__ == '__main__':
    unittest.main()