class Node:

    def __init__(self):
        self.word = None  # only assigned if this node is last letter of word
        self.childs = {}

    def __add__(self, word, str_pos=0):

        cur = word[str_pos]
        node = self.childs.get(cur)
        if not node:
            node = Node()
            self.childs[cur] = node
        if str_pos + 1 == len(word):
            node.word = word
        else:
            node.__add__(word, str_pos + 1)

    def __repr__(self):
        return self.word

    def __get_all__(self):
        out = []
        if self.word:
        	out.append(self.word)
        for c, node in self.childs.iteritems():
        	out += node.__get_all__()
        return out

    def __get_all_with_prefix__(self, prefix):
        """ walk until the node prefix
        	- get_all
        """
        node = self
        for c in prefix:
        	node = node.childs.get(c)
        	if not node:
        		return
        return node.__get_all__()

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        self.root.__add__(word)

    def get_all(self):
    	return self.root.__get_all__()
    def get_all_with_prefix(self, prefix):
    	return self.root.__get_all_with_prefix__(prefix)

possible_words = ['cars', 'care', 'workers', 'cattles', 'emergency', 'carb', 'working', 'worship', 'worry', 'woraya']

trie = Trie()
trie.insert("go")
trie.insert("gone")
trie.insert("gi")
trie.insert("cool")
trie.insert("comb")
trie.insert("grasshopper")
trie.insert("home")
trie.insert("hope")
trie.insert("hose")
for word in possible_words:
	trie.insert(word)
print trie.get_all()
