#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def str2int(v:str):
            v = v.lstrip('0')
            return int(v) if v else 0
        vs1 = [str2int(v) for v in version1.split('.')]
        vs2 = [str2int(v) for v in version2.split('.')]
        n1 = len(vs1)
        n2 = len(vs2)
        
        i = 0
        while i < n1 or i < len(vs2):
            v1 = vs1[i] if i < n1 else 0
            v2 = vs2[i] if i < n2 else 0
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
            i += 1
        return 0
# @lc code=end

