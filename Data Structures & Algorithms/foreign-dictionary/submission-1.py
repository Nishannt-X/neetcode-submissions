from collections import deque,defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        graph=defaultdict(set)
        indeg={}
        for i in words:
            for j in i:
                indeg[j]=0
        
        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]

            if len(w1)>len(w2) and w1.startswith(w2):
                return ""
            for a1,a2 in zip(w1,w2):
                if a1!=a2:
                    if a2 not in graph[a1]:
                        graph[a1].add(a2)
                        indeg[a2]+=1
                    break
        que=deque()

        for i in indeg:
            if indeg[i]==0:
                que.append(i)
        ans=[]

        while que:
            alph=que.popleft()
            ans.append(alph)

            for i in graph[alph]:
                indeg[i]-=1
                if indeg[i]==0:
                    que.append(i)
        if len(ans)!=len(indeg):
            return ""
        
        return "".join(ans)

            





        


        