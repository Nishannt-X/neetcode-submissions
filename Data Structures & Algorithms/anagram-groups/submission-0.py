class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti={}

        for i in strs:
            key="".join(sorted(i))

            if key not in dicti:
                dicti[key]=[]
            dicti[key].append(i)
        return list(dicti.values())
        