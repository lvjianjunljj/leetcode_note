# You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.
#
# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.
#
# Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.
#
# Example 1:
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]
# Note:
# The number of given pairs will be in the range [1, 1000].
import operator


class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort()
        ans = 0
        dp = [1] * len(pairs)
        for i in range(len(pairs) - 2, -1, -1):
            for j in range(i + 1, len(pairs)):
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
        return ans


class Solution2(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        last_index, ans = -float('inf'), 0
        pairs.sort(key=operator.itemgetter(1))
        for x, y in pairs:
            if x > last_index:
                last_index = y
                ans += 1
        return ans
# Solution is TLE, dynamic programming is not a good thought(Solution), greedy is better(Solution2).