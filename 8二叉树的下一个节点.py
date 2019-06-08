# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        if not pNode: return None
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        else:
            while pNode.next:
                if pNode == pNode.next.left:
                    return pNode.next
                pNode = pNode.next
        return None

if __name__=='__main__':
    s = Solution()
    listNode = TreeLinkNode(1)
    listNode.left = TreeLinkNode(2)
    listNode.right = TreeLinkNode(3)
    print(s.GetNext(listNode).val)