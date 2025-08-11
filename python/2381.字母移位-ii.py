#
# @lc app=leetcode.cn id=2381 lang=python3
#
# [2381] 字母移位 II
#

# @lc code=start
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        '''
        变化量的前缀和
        从 start 开始 加上变化的部分，在 end 后一个位置把变化的部分减去
        从前往后遍历的时候加上每个位置的变化，就是当前位置的实际变化
        '''
        delta = [0] * (len(s)+1)
        result = [ord(c)-ord('a') for c in s]
        for left, right, d in shifts:
            d = 2*d-1 # 2*0-1 = -1, 2*1-1 = 1
            delta[left] += d 
            delta[right+1] += -d
        
        d = 0
        for i, c in enumerate(result):
            d += delta[i]
            result[i] = chr( ((c+26+d) % 26) + ord('a')) 
            
        return ''.join(result)

        '''
        线段树...最后会全部单点查询一遍
        '''
# @lc code=end