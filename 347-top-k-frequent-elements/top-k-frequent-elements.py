class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        for num in nums:
            if num in f:
                f[num] +=1
            else:
                f[num] =1

        f = sorted(f.items(), key=lambda x: x[1], reverse=True)
        ans = []
        for i in range(0,k):
            ans.append(f[i][0])
        
        return ans