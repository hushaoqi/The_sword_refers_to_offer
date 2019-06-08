# -*- coding:utf-8 -*-
# 这道题对于Python来说似乎没有意义
# 在Python中字符串类型是不可变类型，即不可以在原处修改
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        s = s.replace(' ', '%20')
        return s
if __name__=='__main__':
    s = Solution()
    string = "we are happy"
    print(s.replaceSpace(string))