# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        r = ""
        for i in range(len(strs[0])):
            for s in strs:
                if len(s) <= i:
                    return r
                if s[i] != strs[0][i]:
                    return r
            r += strs[0][i]

        return r

if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    s = Solution()
    print s.longestCommonPrefix(strs)