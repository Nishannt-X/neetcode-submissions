from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1=Counter(nums)
        dict1=sorted(dict1,key=dict1.get,reverse=True)
        result=[]

        for i in range(k):
            result.append(dict1[i])
        return result


        