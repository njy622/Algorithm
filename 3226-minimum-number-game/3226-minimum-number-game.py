class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums_List = []
        for _ in range(int(len(nums)/2)):
            a = min(nums)
            nums.remove(a)
            b = min(nums)
            nums.remove(b)
            nums_List.append(b)
            nums_List.append(a)
        return nums_List