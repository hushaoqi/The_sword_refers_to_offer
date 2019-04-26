'''
题目描述
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
'''
class Solution:
    def __init__(self):
        self.duplication = None
    # 排序法 time: O(nlogn)

    def duplicate(self, numbers: 'List[int]', length: 'int')->'bool':
        if numbers is None or length <= 0: return False
        for i in range(length):
            if numbers[i] < 0 or numbers[i] > length - 1: return False

        numbers.sort()
        for i in range(length-1):
            if numbers[i] == numbers[i+1]:
                self.duplication = numbers[i]
                return True
        return False
    # hashTable time: O(n) space: O(n)

    def duplicate2(self, numbers: 'List[int]', length: 'int')->'bool':
        if numbers is None or length <= 0: return False
        for i in range(length):
            if numbers[i] < 0 or numbers[i] > length - 1: return False

        diction = {}
        for num in numbers:
            if num not in diction:
                diction[num] = 1
            else:
                self.duplication = num
                return True
        return False

    # 序号与num对应若冲突则相等， time:O(n) space:O(1)

    # 1、判断输入数组有无元素非法
    # 2、从头扫到尾，只要当前元素值与下标不同，就做一次判断, numbers[i]
    # 与numbers[numbers[i]]，相等就认为找到了
    # 重复元素，返回true, 否则就交换两者，继续循环。直到最后还没找到认为没找到重复元素，返回false
    def duplicate3(self, numbers: 'List[int]', length: 'int')->'bool':
        if numbers is None or length <= 0: return False
        for i in range(length):
            if numbers[i] < 0 or numbers[i] > length - 1: return False

        for i in range(length):
            # while 循环的次数≤2，每个数字最多只要交换两次就能找到属于它自己的位置
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    self.duplication = numbers[i]
                    return True

                temp = numbers[i]
                numbers[i] = numbers[temp]
                numbers[temp] = temp
        return False

    # 若要求不能改变原数组，通过计数，类似于二分查找的方法实现， time：O(nlogn) space: O(1)
    # 题目：长度为 n+1 的数组里所有的数字都在 1 ~ n 的范围内
    def duplicate4(self, numbers: 'List[int]', length: 'int')->'bool':
        if numbers is None or length <= 0: return False
        for i in range(length):
            if numbers[i] < 0 or numbers[i] > length - 1: return False

            start = 1
            end = length - 1
            while end >= start:
                middle = ((end - start) >> 1) + start
                count = self.countRange(numbers, length, start, middle)
                if end == start:
                    if count > 1:
                        # self.duplication = numbers[start]
                        self.duplication = start
                        return True
                    else:
                        break
                if count > (middle - start + 1):
                    end = middle
                else:
                    start = middle + 1
        return False

    def countRange(self, numbers: 'List[int]', length: 'int', start: 'int', end: 'int')->'int':
        if numbers is None:
            return 0
        count = 0
        for i in range(length):
            if numbers[i] >= start and numbers[i] <= end:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    numbers = [2, 3, 1, 0, 2, 5, 3]
    length = len(numbers)
    if s.duplicate3(numbers, length):
        print(s.duplication)


    numbers2 = [2, 3, 5, 4, 3, 2, 6, 7]
    length2 = len(numbers2)
    if s.duplicate4(numbers2, length2):
        print(s.duplication)