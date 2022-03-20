# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if not l1:
        return l2
    if not l2:
        return l1

    carry = 0
    last = first = None
    node1 = l1
    node2 = l2

    while node1 or node2 or carry:
        # do the math
        current_val = carry
        if node1:
            current_val += node1.val
        if node2:
            current_val += node2.val

        carry = current_val // 10
        current_val %= 10

        new_digit = ListNode(val=current_val)
        if not first:
            first = new_digit

        if last:
            last.next = new_digit

        last = new_digit

        if node1:
            node1 = node1.next
        if node2:
            node2 = node2.next

    return first
