# def find_duplicate(nums):
#     for num in nums:
#         if not isinstance(num, int) or num < 0:
#             return False
#     if len(nums) == 0:
#         return False
#     if nums[0] in nums[1:]:
#         return nums[0]
#     else:
#         return find_duplicate(nums[1:])


def find_duplicate(nums):
    if len(nums) == 0:
        return False
    nums.sort()
    for i in range(len(nums) - 1):
        if not isinstance(nums[i], int) or nums[i] < 0:
            return False
        if nums[i] == nums[i + 1]:
            return nums[i]
    return False
