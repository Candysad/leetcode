#
# @lc app=leetcode.cn id=1616 lang=python3
#
# [1616] 分割两个字符串得到回文串
#

# @lc code=start
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        halfl, halfr = (n - 1) >> 1, n >> 1
        inner = [[0] * (halfl + 1) for _ in range(2)]
        outer = [[0] * (halfl + 1) for _ in range(2)]
        
        left, right = 0, n-1
        while left <= right:
            if a[left] == b[right]:
                if left == 0:
                    outer[0][left] = 1
                elif outer[0][left-1]:
                    outer[0][left] = 1
            if b[left] == a[right]:
                if left == 0:
                    outer[1][left] = 1
                elif outer[1][left-1]:
                    outer[1][left] = 1
            
            if a[halfl] == a[halfr]:
                if halfl == (n-1) >> 1:
                    inner[0][halfl] = 1
                elif inner[0][halfl + 1]:
                    inner[0][halfl] = 1
                
                    
            if b[halfl] == b[halfr]:
                if halfl == (n-1) >> 1:
                    inner[1][halfl] = 1
                elif inner[1][halfl + 1]:
                    inner[1][halfl] = 1
            
            left += 1
            right -= 1
            halfl -= 1
            halfr += 1
        print(left, right)
        print(inner)
        print(outer)
        if inner[0][0] or inner[0][0]: return True
        
        for i in range((n-1)//2 - 1):
            if outer[0][i] or outer[1][i] and inner[0][i+1] or inner[1][i+1]:
                return True

        return False
            
        
        
# @lc code=end