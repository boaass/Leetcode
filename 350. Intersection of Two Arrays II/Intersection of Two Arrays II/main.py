# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:
#
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
#
# What if the given array is already sorted? How would you optimize your algorithm? What if nums1's size is small
# compared to nums2's size? Which algorithm is better? What if elements of nums2 are stored on disk, and the memory
# is limited such that you cannot load all elements into the memory at once?


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num_dict = {}
        r = []
        for n in nums1:
            if n not in num_dict.keys():
                num_dict[n] = 1
            else:
                num_dict[n] += 1

        for n in nums2:
            if n in num_dict.keys():
                if num_dict[n] == 1:
                    num_dict.pop(n)
                else:
                    num_dict[n] -= 1

                r.append(n)

        return r


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    s = Solution()
    r = s.intersect(nums1, nums2)
    print r