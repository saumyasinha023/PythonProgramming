# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


first = ListNode(1)
first.next = ListNode(1)
first.next.next = ListNode(3)

class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return head
        fakehead= ListNode(0)
        fakehead.next=head
        cur=head
        prev=fakehead

        while cur is not None:
            while cur.next is not None and cur.val==cur.next.val:
                cur=cur.next
            if prev.next==cur:
                prev=prev.next
            else:
                prev.next=cur.next
            cur=cur.next
        return fakehead.next



S=Solution()
node=S.deleteDuplicates(first)
print(node.val)




