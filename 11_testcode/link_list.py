# -*- coding: utf-8 -*-

class Node():
	"""Node class"""

	def __init__(self, data):
		"""Function to initialize the node object"""
		self.data = data
		self.next = None

class LinkedList():
	"""Link list"""

	def __init__(self):
		self.head = None



if __name__ == '__main__':

	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second
	second.next = third


print(llist.head.data)
print(llist.head.next)















