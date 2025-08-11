#
# @lc app=leetcode.cn id=2671 lang=python3
#
# [2671] 频率跟踪器
#

# @lc code=start
class FrequencyTracker:
    '''
    数据结构题
    
    两个字典 hash表
    一个用来存数字和它们自己的出现个数
    一个用来存出现个数的出现个数，用来回答hasFrequency
    '''
    def __init__(self):
        self.nums = {}
        self.freq = {0: 0}

    def add(self, number: int) -> None:
        freq = self.nums.get(number, 0)
        self.nums[number] = freq + 1
        
        freq_freq = self.freq.get(freq + 1, 0)
        if freq > 0:
            self.freq[freq] -= 1
        self.freq[freq + 1] = freq_freq + 1

    def deleteOne(self, number: int) -> None:
        freq = self.nums.get(number, 0)
        if freq > 0:
            self.nums[number] = freq - 1
            self.freq[freq] -= 1
            self.freq[freq-1] += 1
    
    def hasFrequency(self, frequency: int) -> bool:
        freq_freq = self.freq.get(frequency, 0)
        return freq_freq > 0 
# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
# @lc code=end

