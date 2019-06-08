# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点，pre：前序，tin：中序
    def reConstructBinaryTree(self, pre: 'List[int]', tin: 'List[int]') -> 'TreeNode':
        if pre and tin:
            root = TreeNode(pre.pop(0))
            mid = tin.index(root.val)
            root.left = self.reConstructBinaryTree(pre, tin[0:mid])
            root.right = self.reConstructBinaryTree(pre, tin[mid + 1:])
            return root

        else:
            return None

    def print_tree(self, root:'TreeNode'):
        if root:
            print(root.val, end=' ')
        if root.left:
            self.print_tree(root.left)
        if root.right:
            self.print_tree(root.right)


if __name__=='__main__':
    s = Solution()
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    '''
            1
          /   \
        2       3
      /       /   \
     4       5     6
      \           /
       7         8
    '''
    root = s.reConstructBinaryTree(pre, tin)
    s.print_tree(root)

