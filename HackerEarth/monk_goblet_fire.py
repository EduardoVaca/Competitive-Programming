"""
PROBLEM: Little Monk and Goblet of Fire
from: hackerearth.com
"""

class Node(object):
	
	def __init__(self, data=None, prev=None, next=None):
		self.data=data
		self.prev=prev
		self.next=next

	def is_same_type(self, node):
		return node.data[0] == self.data[0]

class Queue(object):

	def __init__(self):
		self.first=None
		self.last=None
		self.last_types = {1: None, 2: None, 3: None, 4: None}

	def enqueue(self, type, n):
		new_node = Node((type, n))
		if not self.first:
			self.first = new_node
			self.last = new_node
			self.last_types[type] = new_node
		else:
			# Look for other node with same type
			if self.last_types[type]:
				if self.last_types[type].next:
					new_node.next = self.last_types[type].next
					self.last_types[type].next.prev = new_node
				elif self.last_types[type] == self.last:
					self.last = new_node
				new_node.prev = self.last_types[type]
				self.last_types[type].next = new_node
				self.last_types[type] = new_node
			else:				
				self.last.next = new_node
				new_node.prev = self.last
				self.last = new_node
				self.last_types[type] = new_node

	def dequeue(self):
		selected_data = self.first.data
		if self.last_types[self.first.data[0]] == self.first:
			self.last_types[self.first.data[0]] = None
		self.first = self.first.next
		if self.first:
			self.first.prev = None
		return selected_data


q = int(input().strip())
queue = Queue()

for _ in range(q):
	values = [x for x in input().strip().split(' ')]
	if len(values) == 3:
		queue.enqueue(int(values[1]), int(values[2]))
	else:
		chosen = queue.dequeue()
		print('{} {}'.format(chosen[0], chosen[1]))

