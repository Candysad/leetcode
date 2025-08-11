#
# @lc app=leetcode.cn id=2129 lang=python3
#
# [2129] 将标题首字母大写
#

# @lc code=start

class Solution:
    '''
    简单题
    字符串结构
    python能一行
    '''
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join([word.lower() if len(word) < 3 else word[0].capitalize() + word[1:].lower() for word in title.split()])
        # @lc code=end

