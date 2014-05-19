class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return '{} -> [{}, {}]'.format(self.data, self.left, self.right)

    def to_json(self):
        return {self.data: {'left': self.left.to_json() if self.left else None,
                            'right': self.right.to_json() if self.right else None}
                }

    def insert(self, data):
        """
            populate data into tree
        """

        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def search(self, data, parent=None):
        """ look up for node that data match otherwise return None
            if data < self.data look to the left
            otherwise look to the right
            @param data
            @parent parent node

            @return node, parent node or None, None
        """

        if data < self.data:
            if self.left:
                return self.left.search(data, self)
            else:
                return None, None
        elif data == self.data:
            return self, parent

        else:
            if self.right:
                return self.right.search(data, self)
            else:
                return None, None
    def tree_data(self):
        stack = [] # carry
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.data
                node = node.right

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print self.data,
        if self.right:
            self.right.print_tree()

    def count_children(self):
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        print cnt
        return cnt

    def delete(self, data):
        node, parent = self.search(data)
        print 'node', node
        if not node:
            return None
        if node.count_children() == 0:
            #delete node and update parent
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None
            del node

        elif node.count_children() == 1:
            #node have one child, connect parent with child node
            if parent.left is node:
                parent.left = node.left or node.right
            else:
                parent.right = node.left or node.right
            del node
        else:
            #node have two child, take the lowest successor to replace deleted node
            pre_successer = node
            sucesser = node.right
            while sucesser.left:
                pre_successer = sucesser
                sucesser = sucesser.left
            print 'deleting, ', data
            print pre_successer
            print sucesser
#            if pre_successer is node:
                #pre_successer.left = None
                #pre_successer.right = None
            pre_successer.left = None
            print pre_successer

            if parent.left is node:
                parent.left = sucesser
            else:
                parent.right = sucesser
            print 'parent', parent
            if node.left:
                print node.left.data
            if node.right:
                print node.right.data
            print 'yy'*10
            sucesser.left = node.left
            sucesser.right = node.right
            print 'zz' * 10
            del node


root = Node(6)

root.insert(10)
root.insert(1)
root.insert(11)
print root
#print json.dumps(root.to_json(), indent=5)

node, parent = root.search(11)
print node
print parent
print 'X'* 10

x = [3,10,1,6,14, 4,7,13]
r1 = Node(8)
for i in x:
    r1.insert(i)


print r1.print_tree()
print r1.print_tree()
for i in r1.tree_data():
    print i
