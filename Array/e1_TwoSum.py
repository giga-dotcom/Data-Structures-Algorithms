def two_sum(nums, target):
    nums_to_index = {}
    for i in range(len(nums)):
        if (target - nums[i]) in nums_to_index:
            return[nums_to_index[target - nums[i]], i]
        else:
            nums_to_index[nums[i]] = i

print(two_sum([2,7,11,15],9))




