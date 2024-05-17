#
# @lc app=leetcode.cn id=1652 lang=python3
#
# [1652] 拆炸弹
#

# @lc code=start
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        '''
        滑动窗口
        指针取模
        负的反过来，答案再反回去
        '''
        n = len(code)
        if k == 0:
            return [0] * n
        t = k
        if k < 0:
            code[:] = code[::-1]
            t = -k
        
        left = 0
        right = 1
        window = 0
        while right <= t:
            window += code[right]
            right += 1
        right %= n

        c = 0
        result = []
        while c < n:
            result.append(window)
            c += 1
            
            left = (left + 1) % n
            window = window - code[left] + code[right]
            right = (right + 1) % n
        
        return result if k > 0 else result[::-1]
        
# @lc code=end

