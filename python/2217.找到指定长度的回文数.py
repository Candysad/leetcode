#
# @lc app=leetcode.cn id=2217 lang=python3
#
# [2217] 找到指定长度的回文数
#

# @lc code=start
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        '''
        按前一半生成
        '''
        bits = (intLength + 1) >> 1
        limit = 10**bits - 1
        base = 10**(bits - 1)
        
        def double(num):
            if intLength % 2:
                return int(str(num) + str(num)[:-1][::-1])
            else:
                return int(str(num) + str(num)[::-1])
            
        return [double(base + q-1) if base + q-1 <= limit else -1 for q in queries]
        
        '''
        取模生成
        '''
        # def generate(target):
        #     # 需要判断的位数，前一半
        #     bits = intLength // 2
        #     if intLength % 2 == 0:
        #         bits -= 1

        #     result = [0] * intLength
        #     left, right = 0, intLength - 1
        #     # 第一位
        #     t = (target-1) // 10**bits
        #     result[left], result[right] = t+1, t+1
        #     left += 1
        #     right -= 1
            
        #     target -= t * 10**bits
        #     bits -= 1
        #     while left <= right:
        #         if bits == 0:
        #             t = target - 1
        #         else:
        #             t = (target-1) // 10**bits

        #         result[left], result[right] = t, t
        #         left += 1
        #         right -= 1
        #         target -= t * 10**bits
        #         bits -= 1
        #     return int(''.join([str(c) for c in result]))
        
        # bits = intLength // 2
        # if intLength % 2 == 0:
        #     bits -= 1
        # limit = 9 * 10 ** bits
        # return [generate(q) if q <= limit else -1 for q in queries]  
# @lc code=end