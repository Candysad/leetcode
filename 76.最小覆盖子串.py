#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
from collections import Counter
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        字串要求保持顺序，且连续不中断
        字串要尽量短，以t为 'ab' 为例, 'c ab d' 就不如里面的'ab'
        换句话说，作为答案的子串肯定是目标中的字符做边界，否则两侧至少有一边浪费了长度'c ab' 'ab c'
        所以只需要记录目标中的字符，在s中找出所有这些字符
        然后看它们两两组合做边界（保持前后顺序），谁满足所有字符都出现且最小
        
        子序列遍历滑动窗口直接找符合要求的位置做下一个窗口，避免浪费时间
        '''
        # 1 个的情况单独判断
        if len(t) == 1 and t in s:
            return t

        char_index = [] # 记录s中目标字符的位置
        chars = []      # 记录对应字符是什么
        for i, c in enumerate(s):
            if c in t:
                chars.append(c)
                char_index.append(i) # 保持顺序并将它们记录下来
        
        nc = len(char_index)

        target = Counter(t)
        
        min_len = len(s) + 1
        result = ''

        left = 0
        right = 0
        counter = Counter()
        # 初始化第一个区间
        while not(counter >= target) and right < nc: # 注意Counter比较大小是只要有元素没有比另一个大就是False
            counter[chars[right]] += 1
            right += 1
        # right 最后会指向下一个需要添加的位置，或者末尾的 nc
        
        if right== nc and not(counter >= target): # 最大的都没找到 # 注意Counter比较大小
            return ''
        
        # 第一个可行的区间
        result = s[char_index[left]: char_index[right-1] + 1]
        min_len = len(result)
        
        while right < nc:
            # 左移一次区间
            counter[chars[left]] -= 1
            left += 1
            
            # 将新的区间补足字符
            while not (counter >= target)  and right < nc: # 注意Counter比较大小
                counter[chars[right]] += 1
                right += 1  

            if counter >= target:
                ts = s[char_index[left]: char_index[right-1] + 1]
                if len(ts) < min_len:
                    min_len = len(ts)
                    result = ts
            else: # 还没有符合的区间说明后面都不符合了
                return result
                    
        # 右边到头了，但是左边有多余的部分，尝试减少左边 
        if right == nc:
            counter[chars[left]] -= 1
            left += 1
            
            while left < nc and counter >= target:
                ts = s[char_index[left]: char_index[right-1] + 1]
                if len(ts) < min_len:
                    min_len = len(ts)
                    result = ts
                counter[chars[left]] -= 1
                left += 1

        return result
# @lc code=end

