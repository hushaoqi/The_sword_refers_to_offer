'''
解题思路：
  （1）把字符串旋转形成另外一个字符串，称为旋转字符串；
  （2）求原字符串s1与旋转字符串s2中，最长公共子串的长度；
  （3）删除的字符数目 = 原字符串的长度 - 最长公共子串的长度。
需要解决的子问题：
   求两个字符串s1和s2中最长公共子串的长度。
   子问题的求解方式：动态规划
     设 MaxLen(i,j)表示s1左边i个字符与s2左边j个字符的最长公共子串长度，则子问题的解为MaxLen(strlen(s1),strlen(s2));
     MaxLen(i,j)的求解方式为：
       若s1第i个字符与s2第j个字符相匹配，则 return 1+MaxLen(i-1,j-1);
       否则：return max(MaxLen(i-1,j),MaxLen(i,j-1))
    边界条件：
    MaxLen(i,n)=0; for n in 0 to strlen(s2)
    MaxLen(n,j)=0; for n in 0 to strlen(s1)
'''
import sys
def maxlcp(strs):
    if strs == None or len(strs) == 0:
        return 0
    lens = len(strs)
    dp =[0] *lens
    dp[0] = 1 if strs[0] == strs[lens-1] else 0
    for i in range(lens):
        pre = dp[0]
        dp[0] = max(dp[0],1 if strs[i] == strs[lens-1] else 0)
        for j in range(1, lens):
            cur = dp[j]
            dp[j] = max(dp[j], dp[j-1])
            if strs[i] == strs[lens-1-j]:
                dp[j] = max(dp[j], pre+1)
            pre = cur
    return dp[lens-1]

def longestPalindromeSubseq(s: str) -> int:
    n = len(s)
    dp = [[0]*10 for _ in range(10)]
    i = n - 1
    while i >= 0:
        dp[i][i] = 1
        j = i + 1
        while j < n:
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

            j += 1
        i -= 1
    return n - dp[0][n-1]

if __name__ == '__main__':
    while True:
        line = sys.stdin.readline().strip()
        lens = len(line)
        if not line:
            break
        maxLcp = maxlcp(line)
        # print lens
        # print maxLcp
        print(lens - maxLcp)
        print(longestPalindromeSubseq(line))