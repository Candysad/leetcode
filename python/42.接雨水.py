#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        左右指针找每一段可以接水的区间
        确定区间的上限
        从左遍历到右算接多少水
        
        区间怎么确定？
        从左往右找，右边比左边更高说明中间都被框住了
        最后一个区间可能右边一直不够高，里面可能局部有沟可以放水但是没找出来？
        从末尾到最后一个 left 之间的区域，反过来从右往左找一次就找出来了
        '''
        left = 0
        right = 1
        result = 0
        n = len(height)
        
        #  从左向右，以右边更大的情况为分界
        while right < n:
            if height[right] >=  height[left]:
                span_height = height[left]
                left += 1
                while left < right:
                    result += span_height - height[left]
                    left += 1
            right += 1

        # 最后一段可能右边没有分界，要反过来找一遍
        if height[-1] < height[left]:
            right = n - 1
            t = right - 1
            while t >= left:
                if height[t] >= height[right]:
                    span_height = height[right]
                    right -= 1
                    while right > t:
                        result += span_height - height[right]
                        right -= 1
                t -= 1
        return result
        
        '''
        双指针从两边向中间
        其实就是上面的过程，只是同时从两边开始
        每个区间只有外侧的更矮的时候形成新的区间，故两侧都和各自的max计算得到水量
        换句话说，中间的比两侧的高才会在两侧形成有水的区间，所以spanheight是外侧的max
        
        不会右边比左边更矮而导致不该和leftmax算水量吗？
        不会。
        因为右边如果更矮这一次就该更新右边
        换个角度想，左侧形成区间一定是左侧区间的左边max是当前区间的短板，如果右边是短板，那这个区间就应该是右侧区间
        如何保证两侧区间不会交错呢？
        因为最高的一定出现在两个区间中间，一旦有一边到达这里，就不可能在更新了，因为另一边总是比他小，他不会再动了
        '''
        # left, right = 0, len(height) - 1
        # left_max, right_max = 0, 0
        # result = 0
        # while left < right:
        #     if height[left] < height[right]:
        #         if height[left] < left_max:
        #             result +=  left_max - height[left]
        #         else:
        #             left_max = height[left]
        #         left += 1
        #     else:
        #         if height[right] < right_max:
        #             result +=  right_max - height[right]
        #         else:
        #             right_max = height[right]
        #         right -= 1
        # return result

# @lc code=end

