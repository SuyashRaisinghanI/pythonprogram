from collections import OrderedDict

def remove_duplicate(s): 
    return "".join(OrderedDict.fromkeys(s))

# test
s="abcfgbsca"
print(s)
print("After removing duplicates: ",remove_duplicate(s))
