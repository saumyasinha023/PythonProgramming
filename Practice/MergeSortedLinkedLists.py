class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


first = ListNode(2)
first.next = ListNode(3)
first.next.next = ListNode(5)
first.next.next.next = ListNode(6)

second = ListNode(4)
second.next = ListNode(9)
second.next.next = ListNode(10)
second.next.next.next = ListNode(11)


class Solution():
    def mergeList(self, first, second):
        # current1 = first
        # current2 = second

        if first is None:
            return second
        if second is None:
            return first

        head = current = ListNode(0)

        while first is not None and second is not None:
            if first.val < second.val:
                head.next = first
                first = first.next
            else:
                head.next = second
                second = second.next
            head = head.next
        head.next=first or second
        return current.next


S = Solution()
head=S.mergeList(first, second)
print(head.val,head.next.val,head.next.next.val,head.next.next.next.val,head.next.next.next.next.val,head.next.next.next.next.next.val,head.next.next.next.next.next.next.val)