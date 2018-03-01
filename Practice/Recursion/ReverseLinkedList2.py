class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


first = ListNode(2)
first.next = ListNode(3)
first.next.next = ListNode(5)
first.next.next.next = ListNode(6)
first.next.next.next.next = ListNode(8)


class Solution():
    def __init__(self):
        self.count = 1
        self.t = ListNode(0)

    def reverseBetween(self, head, m, n):
        runner = head
        current = runner
        if head.next == None or head == None:
            return head
        if m >= n:
            return head
        while self.count != m:
            self.count += 1
            runner = runner.next

        tmp = self.runnerHelper(current, runner, n, m)
        return tmp

    def runnerHelper(self, current, runner, n, m):
        if self.count == n or runner.next == None:
            current.next = runner
            self.t = runner.next
            return
        self.count += 1
        self.runnerHelper(current, runner.next, n, m)
        q = runner.next
        q.next = runner
        runner.next = None
        self.count -= 1
        if self.count == m:
            runner.next = self.t
        return current


S = Solution()
root = S.reverseBetween(first, 2, 5)
print(root.val)
print(root.val, root.next.val, root.next.next.val, root.next.next.next.val, root.next.next.next.next.val)
