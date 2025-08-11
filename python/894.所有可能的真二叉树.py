#
# @lc app=leetcode.cn id=894 lang=python3
#
# [894] 所有可能的真二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
判断标注是从给进去的根节点开始往下遍历
所以树可以从矮往上变高，每次返回需要的高度的子树的节点作为根

每次构建更高的树就创建新的头然后把之前更矮的树放在左右两边
每次构建n个节点的树，除了新的头之外还有 n-1 个节点

可以按树的总个数来分组，但是要控制跳过遍历中的偶数个数节点的情况
也可以按叶子节点（非虚空的）的个数
因为 叶子节点数 = 非叶子节点数 + 1，所以 总节点数 = 叶子节点数 + 非叶子节点树 = 2 * 叶子节点数 - 1
每次新构建一个n个节点的树需要 1 个头 + 左子树节点数 + 右子树节点数
即有 左边节点数 + 右边节点数 = n - 1
进而 2*左边左边叶子节点 - 1 + 2*右边叶子节点 - 1 = n-1
     2*(左叶子数+右叶子数) = n+1
     左叶子 + 右叶子 = (n+1)/2
     右叶子树 = (n+1)/2 - 左叶子数
     只要确定左边有多少叶子就能确定右边有多少叶子

聪明的你也看出来了，真二叉树总结点数一定是奇数，所以这里除2不会出现浮点
又因为 n <= 20，(n+1)/2 实际范围是 [1,10]

按照叶子数分组，对每个总数n，会有 (n+1)/2 个叶子数
遍历叶子数 i 为[1...(n+1)/2 - 1]的组中的所有树，放在新树的左侧
相应地遍历(n+1)/2 - i 即 [(n+1)/2 - 1 .... 1]中的树作为对应左侧叶子节点数的右侧

当然如果你不算上面这一坨直接按左右子树的总节点数写也可以
就是要跳过偶数个数的情况，n=2的时候要记一个[]
相当于存答案的空间不紧凑，遍历过程也不紧凑，有不需要的偶数情况需要跳过
'''
N = 11 # n最大20，奇数最大19，这里下标从1开始，把0空出来所以是11
dp = [[] for _ in range(N)]
dp[1] = [TreeNode(0)]
for total_leaves in range(N):
    for left_leaves in range(1, total_leaves):
        for left in dp[left_leaves]:
            for right in dp[total_leaves - left_leaves]:
                dp[total_leaves].append(TreeNode(0, left, right))

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        return dp[(n+1)//2] if n % 2 else []
        # 奇数就按叶子数找答案，偶数就没答案
# @lc code=end

