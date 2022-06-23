"""
__author__ = "Prathamesh Rodi"
__copyright__ = "Copyright 2022"
__project__ = "Algorithms"
__version__ = "0.0.1"
__maintainer__ = "Prathamesh Rodi"
__email__ = "prathameshrodi3009@gmail.com"
"""
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the
# array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one
# position.
#
# Return the max sliding window.
#
#
#
# Example 1:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

from collections import deque
from typing import List


class Solution:
    def maxslidingwindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l, r = 0, 0
        q = deque()
        while r < len(nums):
            # Check if 1st value in queue is smaller than the current value and remove all the value until
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if q[0] < l:
                q.popleft()
            if r - l + 1 == k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res

# Amazon OA
# Find the minimum operations to be performed on the array to have maximum element in the sliding window of 3 to be
# greater than K. The only allowed operation would be to increase the element by 1.
# Example :
# Input : array = [1, 3, 0, 3, 1] , K=5
# Output: 4
# Explanation : Increasing the element at index (0-based Index) 1 and 3 two times.

if __name__ == '__main__':
    print(Solution().maxslidingwindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
