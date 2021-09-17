def add_to_k(list1, k):
    for i in list1[:len(list1)-1]:
        list1.remove(i)
        if k-i in list1:
            return 'True'
    return 'False' 


print(add_to_k([13,10,3,4],7))