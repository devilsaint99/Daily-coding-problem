def add_to_k(addition,k):
    for item in range(0,len(addition)-1):
        for jtem in range(item+1,len(addition)):
            if addition[item]+addition[jtem]==k:
                return True
    return False
print(add_to_k([13,10,3,4],))