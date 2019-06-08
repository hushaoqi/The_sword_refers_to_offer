# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    # 不改变原链表，使用额外空间（列表或栈） time：O(n) space：O(n)
    def printListFromTailToHead(self, listNode: 'ListNode')->'List[int]':
        stack = []
        while listNode is not None:
            stack.append(listNode.val)
            listNode = listNode.next
        stack.reverse()
        return stack


if __name__=='__main__':
    s = Solution()
    listNode = ListNode(1)
    listNode.next = ListNode(2)
    listNode.next.next = ListNode(3)
    print(s.printListFromTailToHead(listNode))
