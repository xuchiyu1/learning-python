class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]


        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)

        return maxSum
"""
LeetCode 53 - Maximum Subarray
Difficulty: Easy
Type: Array / Greedy / DP

Key Idea:
- Maintain a running subarray sum.
- If current sum becomes negative, discard it.
- At each step, update the global maximum.

Core Transition:
current_sum = max(num, current_sum + num)

Time: O(n)
Space: O(1)

Reflection:
- Key insight: a negative prefix only hurts future sums.
- Learned to recognize when to reset a running state.
- This is dynamic programming simplified into greedy form.
"""
