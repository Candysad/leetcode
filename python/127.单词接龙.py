#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
from collections import defaultdict
from math import inf
# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        广度优先搜索
        字符串单个差异优化建图，以 a*c 为键连接 abc 和 adc
        '''
        wn = len(beginWord)
        queue = []
        
        g = defaultdict(list)
        t = [c for c in beginWord]
        for j in range(wn):
            tt = t.copy()
            tt[j] = "*"
            tt = "".join(tt)
            g[tt].append(-1)
        
        
        for i, s in enumerate(wordList):
            if s == endWord:
                queue.append(i)
            
            t = [c for c in s]
            for j in range(wn):
                tt = t.copy()
                tt[j] = "*"
                tt = "".join(tt)
                g[tt].append(i)
        
        if not queue:
            return 0
        vis = set(queue)
        result = 1
        while queue:
            tq = queue
            queue = []
            for i in tq:
                if i == -1:
                    return result
                
                t = [c for c in wordList[i]]
                for j in range(wn):
                    tt = t.copy()
                    tt[j] = "*"
                    tt = "".join(tt)
                    for k in g[tt]:
                        if k not in vis:
                            queue.append(k)
                            vis.add(k)
                
            result += 1

        return 0
    
        '''
        进一步有双向深度优先
        因为给出了begin 和 end，可以同时向对方出发
        '''
        # wn = len(beginWord)
        # queue1 = []
        # g = defaultdict(list)
        
        # for i, s in enumerate(wordList):
        #     if s == endWord:
        #         queue1.append(i)
            
        #     t = [c for c in s]
        #     for j in range(wn):
        #         tt = t.copy()
        #         tt[j] = "*"
        #         tt = "".join(tt)
        #         g[tt].append(i)
        
        # if not queue1:
        #     return 0
        # # queue1, vis1 从 end 开始
        # vis1 = {queue1[0]:1}
        # # queue2, vis2 从 begin 开始
        # queue2 = []
        # vis2 = {}
        # count = 1
        # t = [c for c in beginWord]
        # for j in range(wn):
        #     tt = t.copy()
        #     tt[j] = "*"
        #     tt = "".join(tt)
        #     for k in g[tt]:
        #         if k not in vis2:
        #             queue2.append(k)
        #             vis2[k] = count + 1 
        
        
        
        # while queue1 and queue2:
        #     tq = queue1
        #     queue1 = []
        #     result = inf
        #     for i in tq:
        #         if i in vis2:
        #             result = min(result, count - 1 + vis2[i])
        #         else:
        #             t = [c for c in wordList[i]]
        #             for j in range(wn):
        #                 tt = t.copy()
        #                 tt[j] = "*"
        #                 tt = "".join(tt)
        #                 for k in g[tt]:
        #                     if k not in vis1:
        #                         queue1.append(k)
        #                         vis1[k] = count + 1
        #     if result != inf: return result
            
        #     count += 1
            
        #     tq = queue2
        #     queue2 = []
        #     for i in tq:
        #         t = [c for c in wordList[i]]
        #         for j in range(wn):
        #             tt = t.copy()
        #             tt[j] = "*"
        #             tt = "".join(tt)
        #             for k in g[tt]:
        #                 if k not in vis2:
        #                     queue2.append(k)
        #                     vis2[k] = count + 1
        # return 0
# @lc code=end

