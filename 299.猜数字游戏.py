#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        '''
        两次遍历
        遍历目标secret比较相同位置，找A
        顺便用hash表存模式guess中的位置不对的数字对应的个数
        用栈存secret没匹配上的数
        O(n)
        
        没匹配上的按序出栈在表中找有没有错位置的对应数找B
        O(n)
        '''
        # hashtable = [0 for i in range(10)]
        hashtable = {str(i):0 for i in range(10)}
        # dict 比 list 慢?
        # 差不多 python 的问题
        
        # 都换成 table 也差不多
        resttable = {str(i):0 for i in range(10)}
        
        A = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                resttable[secret[i]] += 1
                hashtable[guess[i]] += 1

        B = 0
        for rest in resttable:
            B += min(resttable[rest], hashtable[rest])
        
        return str(A) + "A" + str(B) + "B"   
# @lc code=end

