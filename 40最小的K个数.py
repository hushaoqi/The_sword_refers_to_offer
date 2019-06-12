# -*- coding:utf-8 -*-
import random
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        n = len(tinput)
        if n == 0 or k > n or k <= 0:
            return []
        start, end = 0, n - 1
        index = self.partition(tinput, start, end)
        while index != k - 1:
            if index > k - 1:
                end = index - 1
                index = self.partition(tinput, start, end)
            else:
                start = index + 1
                index = self.partition(tinput, start, end)

        return tinput[:k]
        # 牛客上面顺序不对还通不过，最后还来个排序
        # output = sorted(tinput[:k])  # 顺序不对还通不过
        # return output

    def partition(self, tinput, start, end):
        index = random.randint(start, end)
        # index = (start + end) // 2
        tinput[index], tinput[end] = tinput[end], tinput[index]
        small = start - 1
        for index in range(start, end):
            if tinput[index] < tinput[end]:
                small += 1
                if small != index:
                    tinput[index], tinput[small] = tinput[small], tinput[index]
        small += 1
        tinput[end], tinput[small] = tinput[small], tinput[end]
        return small
    # 内置函数操作有点sao哈
    def GetLeastNumbers_Solution2(self, tinput, k):
        n = len(tinput)
        if n == 0 or k > n or k <= 0:
            return []
        return heapq.nsmallest(k, tinput)

if __name__=='__main__':
    s = Solution()
    input = [4,5,1,6,2,7,3,8]
    k = 4
    print(s.GetLeastNumbers_Solution2(input, k))

