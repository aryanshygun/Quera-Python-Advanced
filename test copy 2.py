class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            # return [i, nums[i+1::].index(target-nums[i]) + i + 1] if (target-nums[i]) in nums[i+1::] else None
            x = target - nums[i]
            if x in nums[i+1::]:
                return [i, nums[i + 1::].index(x) + i + 1]
        
qq = Solution()
print(qq.twoSum([3, 2, 4], 6))
# print(qq.twoSum([3,6,9,13,25], 19))