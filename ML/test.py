def example(nums, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
    for num in nums:
        helper(num)
        return found
    
found = example([8,3,2,1,5,4,9,6], {2,3,5,9})
print(found)