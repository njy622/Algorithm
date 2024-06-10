class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
                break
            else: 
                nums.append(target)
                nums.sort()
                for j in range(len(nums)):
                    if target == nums[j]:
                        return j
                
        