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
            nums[i] = 99
            n += 1
         
    
        

for i in range(n):
        # Последние i элементов уже на месте, их не проверяем
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего — меняем местами
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                
k = total - n
print(k)
print(nums)