#
# @lc app=leetcode.cn id=2311 lang=python3
#
# [2311] 小于等于 K 的最长二进制子序列
#

# @lc code=start
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        target = bin(k)[2:] # 将目标值转为二进制字符串
        table = [] # 记录所有 1 和它前面的0的个数
        prez = 0 # 记录前面的 0 的个数
        for i, c in enumerate(s):
            if c == '0':
                prez += 1
            else:
                table.append([i, prez])
        if not table: # 没有 1，全是 0
            return len(s)
        
        # 从指定位置起 找一个最长的小于等于target的长度
        # 只在右侧至少有 len(target) 长度时使用
        def find(i):
            pt = 1
            pn = i+1
            while pt < len(target) and pn < n:
                if s[pn] < target[pt]:
                    # 一旦出现target是1但s里有0的情况，则s产生的二进制一定比target小
                    # 可以直接贪心把后面的遍历跳过，直接把剩下的字符都加进去
                    # 当然，不能超过长度
                    return min(pt + n-pn, len(target))
                elif s[pn] == target[pt]: # 都是 1
                    pn += 1
                    pt += 1
                else: # target 是 0，s里的是 1，s 的指针向后走
                    pn += 1
            return pt
        
        result = prez # 最起码全部的0可以组成一组
        for ti in range(len(table) - 1, -1, -1): # 枚举每个1作为一段的起始
            if n - table[ti][0] < len(target): # 长度不够就直接产生
                tl = n - table[ti][0] 
            else:
                tl = find(table[ti][0]) # 长度够了就进去找
            result = max(result, tl + table[ti][1])
            if tl == len(target): 
                # 右侧长度刚好等于 target
                # 再往左边找1做开头也只会减少左侧前导 0 的个数，直接离开
                return result
        return result
# @lc code=end