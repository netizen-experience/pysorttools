def bubble_sort(nums):
    """
    Sorts a list of numbers using the bubble sort algorithm.
    """
    n = len(nums)
    for i in range(n):
        # Last i elements are already in place
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums