#给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
#
# 示例 1: 
#
# 输入: "abcabcbb"
#输出: 3 
#解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
#
# 示例 2: 
#
# 输入: "bbbbb"
#输出: 1
#解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
#
# 示例 3: 
#
# 输入: "pwwkew"
#输出: 3
#解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# Related Topics 哈希表 双指针 字符串 Sliding Window



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        q = []
        d = {}
        max_len = 0
        p = 0
        for index, i in enumerate(s):
            if i in d:
                max_len = max_len if p <= max_len else p
                for index1, j in enumerate(q):
                    if j == i:
                        q = q[index1 + 1:]
                        break
                    del d[j]
                q.append(i)
                p = len(q)
            else:
                d[i] = index
                q.append(i)
                p += 1
        return max_len if p <= max_len else p
        
#leetcode submit region end(Prohibit modification and deletion)
