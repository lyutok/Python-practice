"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.

Return k.

"""
nums = [3,2,2,3]
val = 3

k = 0
n = 0


total = len(nums)
j = 0

for i in range(total):
    for j in range(total-1, 0, -1):
        if nums[i] == val:
            c = nums[i]
            nums[i] = nums[j]
            nums[i] = c
            n += 1

                
k = total - n
print(k)
print(nums)