class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        set(nums)
        nums.sort()
        counter = 0
        for num in reversed(nums):
            counter +=1 
            if counter == k:
                return num