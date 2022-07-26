
"""
Linked List is a linear data structure. Unlike arrays, linked list elements
are not stored at a contiguous location the elements are linked using
pointers. Singly linked list is represented by a pointer to the first node
called head, if linked list is empty then the value of head is NULL (None).
Each node of a singly linked list contains 2 parts:
  - Stored data
  - Pointer to the next node (or reference)
      HEAD
    [data1|-]->[data2|-]->[data3|-]->[data4|-]->[data5|-]->NULL
"""
from __future__ import annotations

import unittest
from typing import TypeVar, Generic, Generator, Any

T = TypeVar('T')

class SinglyLinkedList(Generic[T]):
    class Node:
        def __init__(self, data: T, nxt: Node = None):
            self._data = data
            self._nxt = nxt

        def __repr__(self) -> str:
            return f'[{self._data}]->[]' if self._nxt is None else f'[{self._data}]->'

        @property
        def data(self) -> T:
            return self._data

        @data.setter
        def data(self, data: T):
            self._data = data

        @property
        def nxt(self) -> Node:
            return self._nxt
        
        @nxt.setter
        def nxt(self, nxt: Node):
            self._nxt = nxt

    def __init__(self, head: Node = None, size: int=0):
        self._head = head
        self._size = size

    def __iter__(self) -> Generator[Node, Any, None]:
        tmp = self._head
        while tmp:
            yield tmp
            tmp = tmp.nxt

    @property
    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._head is None
    
    def search(self, data: T) -> bool:
        tmp = self._head
        while tmp:
            if tmp._data==data:
                return True
            return False

    def insert(self, data: T):
        node = SinglyLinkedList.Node(data)
        if self.is_empty():
            self._head = node
        else:
            tmp = self._head
            while tmp.nxt:
                tmp = tmp.nxt
            tmp.nxt = node
        self._size += 1

    def remove(self, data: T) -> T:
        if self.is_empty():
            raise RuntimeError("List is empty, can not remove")
        old, prev = self._head, None
        while old and old.data != data:
            prev = old
            old = old.nxt
        
        if not old:
            raise RuntimeError("Node does not exist in this list")

        removed = old.data
        if old is self._head:
            self._head = self._head.nxt
        else:
            prev.nxt = old.nxt

        self._size -= 1
        return removed

class TestSinglyLinkedList(unittest.TestCase):

    def test_integer_linked_list(self):
        linked_list: SinglyLinkedList[int] = SinglyLinkedList()

        self.assertTrue(linked_list.is_empty())
        self.assertEqual(linked_list.size, 0)

        linked_list.insert(0)
        linked_list.insert(1)
        linked_list.insert(2)
        linked_list.insert(3)

        self.assertFalse(linked_list.is_empty())
        self.assertListEqual([node.data for node in linked_list], [0, 1, 2, 3])

        linked_list.remove(3)
        self.assertEqual([node.data for node in linked_list],[0, 1, 2])
        linked_list.remove(2)
        self.assertEqual([node.data for node in linked_list],[0, 1])

        with self.assertRaises(RuntimeError):
            linked_list.remove(6)
    
        linked_list.remove(0)
        self.assertEqual([node.data for node in linked_list],[1])
        linked_list.remove(1)
        self.assertEqual([node.data for node in linked_list],[])

        with self.assertRaises(RuntimeError):
            linked_list.remove(6)

if __name__ == '__main__':
    unittest.main()