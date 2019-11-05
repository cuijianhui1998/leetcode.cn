#给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。 
#
# 
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。 
#
# 进阶: 
#
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。 
#
# 示例: 
#
# 
#输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
#输出: 7 -> 8 -> 0 -> 7
# 
# Related Topics 链表



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        res_stack = []
        j = 0
        while stack1 and stack2:
            r = stack1.pop() + stack2.pop()
            res_stack.append((r+j)%10)
            j = (r+j)//10
        z = stack1 if stack1 else stack2
        while z:
            r = z.pop()
            res_stack.append((r + j) % 10)
            j = (r + j) // 10
        if j:
            res_stack.append(1)
        d = ListNode(-1)
        p = d
        while res_stack:
            p.next = ListNode(res_stack.pop())
            p = p.next
        return d.next
        
#leetcode submit region end(Prohibit modification and deletion)
