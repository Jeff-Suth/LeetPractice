def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    Find the sum of nums that will be rightSum...when popping off a number from nums then minus it from the sum and add it to leftSum. When rightSum == leftSum then stop
    While rightSum != leftSum
    """
    index = 0
    leftSum = 0
    rightSum = 0
    temp = 0
    equal = False
    # Let's calculate the sum of the numbers on the right before starting so to avoid having to keep checking throughout
    for i in range(0,len(nums)):
        rightSum = rightSum + nums[i]
    # I was not sure to do a while loop until the list of numbers was empty or while leftSum != rightSum but after testing I think this approach works better
    # I still think this is very ugly and not the best way to handle this probelm but it is a solution
    while nums != []:
        # Before checking if they're equal, the problem states that we are not including the current index in either of the sums
        # So we will pop it off the list and minus it before comparing the sums. If it is not equal we will add it to leftSum and increase index
        # If they are equal we will break out of this while loop and return the index
        # If we iterate through everything in nums and the sums are still not equal we will return an index of -1 per the prompt's specifications
        temp = nums.pop(0)
        rightSum = rightSum - temp
        print(f"leftSum is {leftSum}. rightSum is {rightSum}.")
        if rightSum != leftSum:
            leftSum = temp + leftSum
            index += 1
        elif rightSum == leftSum:
            # We decide to add a boolean here to doubly confirm if the sums are equal since we ran into an issue with negatives at the end of the list
            equal = True
            break
    if rightSum != leftSum or not(equal):
        index = -1
    return index


# input = [1,7,3,6,5,6]
input = [-1,-1,-1,1,1,1]
print(pivotIndex(input))