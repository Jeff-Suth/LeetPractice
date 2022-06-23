input = [1,2,3,4]
def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    pull number from position 1 then remove and then add number to new array
    return runningSum
    while runningSum.length <= nums.length:
    """
    runningSum = []
    num = 0
    while nums != []:
        # Keep a temporary variable so we can keep adding together the previous number that was popped off the array
        temp = num
        # Add those together and that gives our current running value from the number popped off the array plus the previous sum
        num = nums.pop(0) + temp
        # Append the number to our new array of runningSum
        runningSum.append(num)
    return runningSum

print(runningSum(input))