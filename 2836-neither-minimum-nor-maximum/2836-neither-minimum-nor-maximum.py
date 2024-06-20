class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        maxN = max(nums)
        minN = min(nums)
        if maxN:
            nums.remove(maxN)
            if len(nums)>1 and minN:
                nums.remove(minN)

                if len(nums) > 0:
                    return nums[0]
                else:
                    return -1
            else:
                return -1
        else:
            return -1
        