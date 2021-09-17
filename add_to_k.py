"""Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

This code works faster than alternate

"""

def add_to_k(addition,k):
    for item in range(0,len(addition)-1):
        for jtem in range(item+1,len(addition)):
            if addition[item]+addition[jtem]==k:
                return True
    return False
print(add_to_k([13,10,3,4],7))