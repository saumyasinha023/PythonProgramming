class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Tree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Tree(3)
root.left=Tree(9)
root.right=Tree(20)
root.right.left=Tree(15)
root.right.right=Tree(7)

class Solution():
    def __init__(self):
        self.head=ListNode(0)
        self.current=self.head
    def flatten(self,root):
        # current=self.head
        self.flatHelper(root,self.current)
        return self.head.next

    def flatHelper(self, root, current):
        if root is None:
            return
        else:
            tmp=ListNode(root.val)
            self.current.next=tmp
            self.current=self.current.next
            self.flatHelper(root.left,self.current)
            self.flatHelper(root.right,self.current)

S=Solution()
first=S.flatten(root)
print(first.next.next.next.val)