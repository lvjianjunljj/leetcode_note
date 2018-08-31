# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.
#
# Example 1:
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
# Example 2:
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
# Note:
#
# 0 < s1.length, s2.length <= 1000.
# All elements of each string will have an ASCII value in [97, 122].
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        def aux_dp(s1, s2, start1, start2, dp):
            if dp[start1][start2] > -1:
                return dp[start1][start2]
            dp[start1][start2] = 0
            if start1 == len(s1):
                for i in range(start2, len(s2)):
                    dp[start1][start2] += ord(s2[i])
            elif start2 == len(s2):
                for i in range(start1, len(s1)):
                    dp[start1][start2] += ord(s1[i])
            else:
                if s1[start1] == s2[start2]:
                    dp[start1][start2] = aux_dp(s1, s2, start1 + 1, start2 + 1, dp)
                else:
                    dp[start1][start2] = min(aux_dp(s1, s2, start1 + 1, start2, dp) + ord(s1[start1]),
                                             aux_dp(s1, s2, start1, start2 + 1, dp) + ord(s2[start2]))
            return dp[start1][start2]

        dp = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        return aux_dp(s1, s2, 0, 0, dp)


class Solution2(object):
    def minimumDeleteSum(self, s1, s2):
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for i in range(len(s1) - 1, -1, -1):
            dp[i][len(s2)] = dp[i + 1][len(s2)] + ord(s1[i])
        for j in range(len(s2) - 1, -1, -1):
            dp[len(s1)][j] = dp[len(s1)][j + 1] + ord(s2[j])

        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i + 1][j] + ord(s1[i]),
                                   dp[i][j + 1] + ord(s2[j]))

        return dp[0][0]
# Thought of two answer is same but the cost time of Solution2 is shorter, fuck.........
