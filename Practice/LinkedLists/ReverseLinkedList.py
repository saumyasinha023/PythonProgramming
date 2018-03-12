# 1->2->3->4
# 4->3->2->2->1
# None<-1<-2<-3<-4

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


first = ListNode(1)
first.next = ListNode(2)
first.next.next = ListNode(3)
first.next.next.next = ListNode(4)
first.next.next.next.next = ListNode(5)


class Solution:
    def reverseList(self, head):
        prev = None

        while head != None:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        return prev

S=Solution()
print(S.reverseList(first).next.val)


def t2Sum(self, A, B):
    return self.helper(A, B, 0)


def helper(self, root, tsum, bal):
    if root is None:
        return 0

    if bal > tsum:
        return 0
    if bal == tsum:
        return 1

    bal = self.helper(root.left, tsum, bal)
    if bal<sum:
        bal += tsum
        return bal
    bal = self.helper(root.right, tsum, bal)
    if bal<sum:
        bal += tsum
        return bal