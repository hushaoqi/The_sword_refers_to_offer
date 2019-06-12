# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for num in range(1,n+1):
            while num > 0:
                if num % 10 == 1:
                    count += 1
                num = num / 10
        return count

    def NumberOf1Between1AndN_Solution2(self, n):
        res = 0
        tmp = n
        base = 1
        while tmp:
            last = tmp % 10
            tmp = tmp // 10
            res += tmp * base
            if last == 1:
                res += n % base + 1
            elif last > 1:
                res += base
            base *= 10
        return res

    def NumberOf1Between1AndN_Solution3(self, n):
        '''
        我们从低位到高位求每位1出现的次数，累加求和即可
        例如：求0~abcde中1的个数，现在我们求c这一位中1出现的次数，其他位雷同;
        有两部分组成:
        第一部分：ab * 100，表示当ab这两位在0~ab-1范围内时，de可以从0~99取值
          第二部分：如果c>1时，当ab为ab时1的个数为0~99
                  如果c=1时，当ab为ab时1的个数为de + 1
                如果c<0时，当ab为ab是1的个数为0
        '''
        # write code here
        exp = 1
        count = 0
        while n / exp:
            # step1
            # 当前位exp=100时，对于12345保留1200，当前exp是1时，对12345保留1234
            # 一句话，保留比exp位要大的部分，再除以10。
            count += (n / (10 * exp)) * exp

            # step2
            # 判断当前位是否大于  等于  小于 1 从而决定第二部分应该加多少
            if (n / exp) % 10 > 1:
                count += exp
            elif (n / exp) % 10 == 1:
                # 只保留当前位或者比当前位大的部分
                count += n - (n / exp) * exp + 1
            exp *= 10
        return count
if __name__=='__main__':
    s = Solution()
    print(s.NumberOf1Between1AndN_Solution2(9))