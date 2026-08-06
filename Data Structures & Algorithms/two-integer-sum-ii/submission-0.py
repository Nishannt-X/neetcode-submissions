class Solution:
    def twoSum(self, number: List[int], target: int) -> List[int]:

        left=0
        right=len(number)-1

        while left<=right:
            if number[left]+number[right]==target:
                return [left+1,right+1]
            elif number[left]+number[right]<target:
                left+=1
            elif number[left]+number[right]>target:
                right-=1
        return []
            


        