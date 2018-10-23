# Description of the topic
# Enter a complex linked list (each node has a node value, and two pointers, one pointing to the next node and another special pointer to any node).
#
#
#
# Problem solving
# Idea one:
#
# In two steps: the first step, traversing the linked list, copying one copy; O(n)
#
# The second step is to traverse the linked list and find random pointers. Because the random pointers are located from the beginning, the random pointers of each node must be looked up from the beginning; the time complexity is: O(n^2)
#
# Total time complexity: O(n^2)
#
#
#
# Idea 2:
#
# In three steps:
#
# The first step: copy one, the link is behind the original node, for example: 1->2->3->4, after copying: 1->1->2->2->3->3->4->4 . Time complexity O(n)
#
# Step 2: Copy the random pointer and set the pointer of the random pointer. Time complexity O(n)
#
# The third step: split into two linked lists, pay attention to the coding details. Time complexity O(n)
#
# Total time complexity: O(n)+O(n)+O(n) == O(n)
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return head

        # Establish an association structure
        cur = head
        while cur:
            temp = cur
            cur = cur.next
            copy_node = RandomListNode(temp.label)
            copy_node.next = temp.next
            temp.next = copy_node

        # Copy random pointer
        cur = head
        while cur:
            temp = cur.random
            cur.next.random = cur.random.next if temp else None
            cur = cur.next.next

        # Copy next pointer
        copy_cur, copy_head = head.next, head.next
        while copy_cur and copy_cur.next:
            copy_cur.next = copy_cur.next.next
            copy_cur = copy_cur.next
        copy_cur.next = None
        return copy_head
