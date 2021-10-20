#insert elements and return the height of a binary search tree

class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data

class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        if not root:
            return -1
        if not root.left and not root.right:
            return 0
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        return max(left_height, right_height) + 1


T=int(input("Number of elements in tree: "))
myTree=Solution()
root=None
for i in range(T):
    data=int(input("Element to be inserted in tree: "))
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(f"The maximun height is {height}")       