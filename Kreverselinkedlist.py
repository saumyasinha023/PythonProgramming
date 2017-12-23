class Node():
    def __init__(self, head):
        self.val = head
        self.next = None


first = Node(1)
first.next = Node(2)
first.next.next = Node(3)
first.next.next.next = Node(4)
first.next.next.next.next = Node(5)


class Solution(object):
    def reverseList(self, A, B):
        head = A
        C=Node(0)
        count = 1
        while count < B:

            count += 1
            if count==B-1:
                A = A.next.next
                C.next=A.next
                count-=1

            else:
                A=A.next

S = Solution()
S.reverseList(first, 3)
