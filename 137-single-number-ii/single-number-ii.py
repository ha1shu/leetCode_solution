class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] +=1
            else:
                frequency[num] = 1
            
        for key,value in frequency.items():
            if value == 1:
                return key
            
        return -1