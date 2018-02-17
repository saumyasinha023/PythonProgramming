class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)


class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next != None and current.next.next != None:
            first = current.next
            second = current.next.next
            first.next = second.next
            current.next = second
            second.next = first
            current = current.next.next
        return dummy.next


S = Solution()
head = S.swapPairs(head)
print(head.val, head.next.val, head.next.next.val, head.next.next.next.val)
