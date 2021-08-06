nums = [0, 4, 3, 0]
target = 0

# Commented out debugging process instead of deleting. Showed myself stepping through the list, which if statement
# I was in, and checking if the counter was incrementing which was the issue originally with this run. [0,3] should
# be returned.

def twosum(nums, target):
    counter = 0
    for num in nums:
        # print(f"The {num}")
        index1 = counter
        goal_1 = target - num
        goal_2 = num - target
        if goal_1 in nums:
            # print("In goal 1!")
            if nums.index(goal_1) != index1:
                index2 = nums.index(goal_1)
                if goal_1 == num:
                    return index2, index1
                else:
                    return index1, index2
            else:
                counter += 1
                # print(counter)
        elif goal_2 in nums:
            # print("In goal 2!")
            if nums.index(goal_2) != index1:
                index2 = nums.index(goal_2)
                if goal_2 == num:
                    return index2, index1
                else:
                    return index1, index2
            else:
                counter += 1
        else:
            counter += 1

print(twosum(nums, target))

# So what was wrong with the double for loop approach?
# While correct and functional for small data sets, it is not scalable and robust!
# What I mean by that is that if we scale up the data set to have 20,000 values then it will have to iterate
# through the nested for loop 400000000! That is O(N^2) time because we have to go through the array N^2 times.
# With this approach, we are able to achieve O(N) time
# Test 1 = double for loop
# Test 2
#     for num in nums:
#         print(num)
#
#     done = False
#     counter = 0
#     i = len(nums)
#     while not(done) and counter < i:
# def twosum(nums, target):
#     counter = 0
#     i = len(nums)
#     while counter < i:
#         for x in range(0,i):
#             num = nums[x]
#             print(num)
#             goal_1 = target - num
#             goal_2 = num - target
#             if goal_1 in nums:
#                 index1 = nums.index(num)
#                 index2 = nums.index(goal_1)
#                 return index1, index2
#             elif goal_2 in nums:
#                 index1 = nums.index(num)
#                 index2 = nums.index(goal_2)
#                 return index1, index2
#             else:
#                 counter += 1
# Test 3
# for num in nums:
#             goal_1 = target - num
#             goal_2 = num - target
#             if goal_1 in nums and goal_1 != num:
#                 index1 = nums.index(num)
#                 index2 = nums.index(goal_1)
#                 return index1, index2
#             elif goal_2 in nums and goal_2 != num:
#                 index1 = nums.index(num)
#                 index2 = nums.index(goal_2)
#                 return index1, index2