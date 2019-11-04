#给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。 
#
# 示例 1: 
#
# 输入: [[1,1],[2,2],[3,3]]
#输出: 3
#解释:
#^
#|
#|        o
#|     o
#|  o  
#+------------->
#0  1  2  3  4
# 
#
# 示例 2: 
#
# 输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
#输出: 4
#解释:
#^
#|
#|  o
#|     o        o
#|        o
#|  o        o
#+------------------->
#0  1  2  3  4  5  6 
# Related Topics 哈希表 数学



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)<=1:
            return 0
        funcPoints = []

        def helper(arr, points):
            if len(arr) == 2:
                funcPoints.append(arr)
                return
            for index, point in enumerate(points):
                
                helper(arr+[point], points[index + 1:])

        helper([], points)
        funcs = [self._func(point_tuple) for point_tuple in funcPoints]
        max_point = 2
        for index, func in enumerate(funcs):
            m = 2
            for point in points:
                if point in funcPoints[index]:
                    continue
                if isinstance(func, int):
                    if point[0]==func:
                        m += 1
                    continue
                if func[0] * point[0] + func[1] == point[1]:
                    m += 1
            max_point = max_point if max_point >= m else m
        return max_point

    def _func(self, point_tuple):
        if point_tuple[1][0] - point_tuple[0][0]!=0:
            a = (point_tuple[1][1] - point_tuple[0][1]) / (point_tuple[1][0] - point_tuple[0][0])
            b = point_tuple[1][1] - a * point_tuple[1][0]
            return (a, b)
        else:
            return point_tuple[1][0]


s = Solution()
a = s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]] )
print(a)
    #leetcode submit region end(Prohibit modification and deletion)
