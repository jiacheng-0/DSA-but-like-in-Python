

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l = ListNode(1)
print(l)
print(l.val)
print(l.next)

l2 = ListNode(2)
l.next = l2
# print(l.next.val)


print('---')
while l.next:
    print(l.val)
    l = l.next
    
print(l.val)