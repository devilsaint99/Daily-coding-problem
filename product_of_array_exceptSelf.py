"""Given an array of integers, return a new array such that each element at index i of the new array
     is the product of all the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
     If our input was [3, 2, 1], the expected output would be [2, 3, 6]."""


import numpy as np

def product_of_Array(nums):
    product_list=[]
    prod=np.prod(nums)
    for item in nums:
        product=prod//item
        product_list.append(product)
    return product_list


num_list=[1,2,3,4,5]
num_list1=[3,2,1]
print(product_of_Array(num_list))
print(product_of_Array(num_list1))

#GG