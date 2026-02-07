class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        d=defaultdict(list)
        
        for i,v in enumerate(nums):
            
            d[v].append(i)

        ans=float('inf')
        for pos in d.values():
            if len(pos)>=3:
                for i in range(len(pos)-2):
                    a,b,c=pos[i],pos[i+1],pos[i+2]
                    dist=abs(a-b)+abs(b-c)+abs(c-a)
                    ans=min(ans,dist)
        return  ans if ans !=float('inf') else -1
        