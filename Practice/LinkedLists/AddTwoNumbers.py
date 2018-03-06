class Node():
    def __init__(self, head):
        self.val = head
        self.next = None


first = Node(1)
# first.next = Node(9)
# first.next.next = Node(3)

second = Node(9)
second.next = Node(9)


# second.next.next = Node(4)


class Solution():
    def addTwoNumbers(self, l1, l2):
        ans = Node(0)
        head = ans
        p, q, r = l1, l2, ans
        carry, sum = 0, 0

        while p or q or carry:
            pval, qval = 0, 0
            if p:
                pval = p.val
                p = p.next
            if q:
                qval = q.val
                q = q.next

            tsum = pval + qval

            if carry != 0:
                sum = (tsum + carry) % 10
                tsum = tsum + carry
            else:
                sum = tsum % 10
            r = Node(sum)
            ans.next = r
            carry = int(tsum / 10)

            ans = ans.next
        head = head.next
        return head


S = Solution()
head = S.addTwoNumbers(first, second)
print(head.val, head.next.val, head.next.next.val)
