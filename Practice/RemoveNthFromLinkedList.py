class Node():
    def __init__(self, head):
        self.val = head
        self.next = None


first = Node(1)
first.next = Node(2)
first.next.next = Node(3)
first.next.next.next = Node(4)
first.next.next.next.next = Node(5)
first.next.next.next.next.next = Node(6)
first.next.next.next.next.next.next = Node(7)


# print(first.val)
# print(first.next.val)
# print(first.next.next.val)


class Solution():
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


S = Solution()
node = S.removeNthFromEnd(first, 2)
print(node.val)
print(node.next.val)
print(node.next.next.val)
print(node.next.next.next.val)
