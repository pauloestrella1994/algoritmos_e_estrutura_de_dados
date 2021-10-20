class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        queue = []
        if root is None:
            return
        queue.append(root)
        while len(queue) != 0:
            node = queue.pop(0)
            print(node.data, end =' ')
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

T=int(input("Number of elements in tree: "))
myTree=Solution()
root=None
for i in range(T):
    data=int(input("Element to be inserted in tree: "))
    root=myTree.insert(root,data)
myTree.levelOrder(root)