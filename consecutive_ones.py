"""You are given a list of integers nums which contains at least one 1. Return whether all the 1s appear consecutively.

Constraints
1 ≤ n ≤ 100,000 where n is the length of nums

Example 1
Input
nums = [0, 1, 1, 1, 2, 3]
Output
True
Explanation
All the 1s appear consecutively here in the middle.

Example 2
Input
nums = [1, 1, 0, 1, 1]
Output
False
Explanation
There's two groups of consecutive 1s.



"""


def solve(nums):
    start,end=0,0
    for i in range(len(nums)):
        if nums[i]==1:
            start=i
            break;
    for j in reversed(range(len(nums))):
        if nums[j]==1:
            end=j
            break;
    newList=nums[i:j+1]
    for item in newList:
        if item!=1:
            return False
    return True

print(solve([0, 1, 1, 1, 2, 3]))