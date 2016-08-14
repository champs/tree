class Node(object):
	def __init__(self, data):
		self.data = data
		self.childs = {}

	def __repr__(self):
		return 'Node {}: {}'.format(self.data, self.childs)

	def get_child(self, data):
		return self.childs.get(data)

	def set_child(self, data):
		if not self.childs.get(data):
			self.childs[data] = Node(data)
		return self.childs[data]

	def add_word(self, word):
		node = self
		for i in xrange(len(word)):
			node = node.set_child(word[i])

	def walk_node(self, word):
		node = self
		for i in xrange(len(word)):
			node = node.get_child(word[i])
			if not node:
				return
		return node

	def predict(self):
		""" find path from node to all leafs
		"""
		pass




if __name__ == '__main__':

	root = Node('root')
	for word in ['care', 'cars', 'carp', 'carb', 'craw', 'crab']:
		root.add_word(word)
	print root

	# suggestion
