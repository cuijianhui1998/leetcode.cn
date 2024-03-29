#给定一个非空的整数数组，返回其中出现频率前 k 高的元素。 
#
# 示例 1: 
#
# 输入: nums = [1,1,1,2,2,3], k = 2
#输出: [1,2]
# 
#
# 示例 2: 
#
# 输入: nums = [1], k = 1
#输出: [1] 
#
# 说明： 
#
# 
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。 
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。 
# 
# Related Topics 堆 哈希表



#leetcode submit region begin(Prohibit modification and deletion)
import heapq
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = defaultdict(int)
        res = []
        for i in nums:
            count[i] += 1
        for key,c in count.items():
            if len(res)<k:
                heapq.heappush(res,(c, key))
            else:
                if c>res[0][0]:
                    heapq.heapreplace(res,(c, key))
        return [i[1] for i in res]


        
#leetcode submit region end(Prohibit modification and deletion)
