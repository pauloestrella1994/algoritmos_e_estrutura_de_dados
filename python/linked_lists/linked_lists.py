class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end ='')
            current = current.next
    
    def insert(self, head, data):
        temp = Node(data)
        if head is None:
            return temp
        current = head
        while current.next is not None:
            current = current.next
        current.next = temp
        return head


mylist = Solution()
T = int(input("Number of elements to insert in linked list: "))
head = None
for i in range(T):
    data = int(input("Insert your number: "))
    head = mylist.insert(head, data)
mylist.display(head)