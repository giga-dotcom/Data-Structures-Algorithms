from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums: List[int]
        #if array is empty
        if not nums:
            return 0

    #initialize slow pointer to 0

        slow = 0

        #Iterate over the array with the fast pointer
        for fast in range(1, len(nums)):
         #if the current element is different from the last unique element
            if nums[fast] != nums[slow]:
            #move slow pointer forward
                slow += 1
        #now update the element at the slow pointer to be the current element
                nums[slow] = nums[fast]

        #The number of unique elements is slow + 1
        return slow + 1

    #Example usuage:
sol = Solution()
nums = [1,1,2]
k = sol.removeDuplicates(nums)
print(k)
print(nums[:k])

nums2 = [0,0,1,1,1,2,2,3,3,4]
k2 = sol.removeDuplicates(nums2)
print(k2)
print(nums2[:k2])
