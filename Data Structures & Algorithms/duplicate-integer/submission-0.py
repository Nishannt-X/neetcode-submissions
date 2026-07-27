class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicti={}

        for i in range(len(nums)):
            dicti[nums[i]]=dicti.get(nums[i],0)+1
        
        for i in dicti.values():
            if i>1:
                return True
        return False

        