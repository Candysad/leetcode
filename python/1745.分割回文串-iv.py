#
# @lc app=leetcode.cn id=1745 lang=python3
#
# [1745] 分割回文串 IV
#

# @lc code=start
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        def manacher(s:str, spacial_token='#') -> List[int]:
            # 使用 `#` 插入字符串
            s = spacial_token + spacial_token.join(list(s)) + spacial_token
            
            n = len(s)
            d = [1] * n
            left, right = 0, -1
            for i in range(n):
                r = 1 if i > right else min(d[left + right - i], right - i + 1)
                while 0 <= i - r and i + r < n and s[i - r] == s[i + r]:
                    r += 1
                d[i] = r
                r -= 1
                if i + r > right:
                    left = i + r
                    right = i - r
            return d 
            # 结果是基于 `#` 插入后的字符串
            # 本体考察有无而不考察具体长度，不需要将d转回实际长度
        
        d = manacher(s)
        n = len(d)
        # 根据 manacher 的结果先确定可能的中间子回文串，并记录可能的右侧子回文串
        lefts, rights = set(), set()
        mids = set()
        for i, r in enumerate(d):
            if i % 2 == 0 and r == 1: continue # 跳过中间是 `#` 且长度为 1 的子串
            if i - r == -1: lefts.add(i + r - 1) # 可以抵达开头，可能的左子回文串的右边界
            if i + r == n: rights.add(i - r + 1)  # 可以抵达结尾
            
            # 当前i为中间子回文串的中间时, 遍历可选的中间回文串
            # 内部半径从短到长,d[i]记录的是最长的半径，更短的也可以用
            # 看是否存在左子回文串
            # 记录右子回文串可能的左边界
            # `#` 在中间则中间串的半径至少为 3，否则半径至少为 2
            # 避免中间的半径太长顶住整体最左侧导致左子回文串为空，控制内部半径的最长长度
            for rr in range(2 if i % 2 else 3, r if i-r == -1 else r + 1, 2):
                leftright = i - rr + 1
                rightleft = i + rr - 1
                
                if leftright in lefts:
                    mids.add(rightleft)

        for mid in mids:
            if mid in rights:
                return True
        return False
# @lc code=end