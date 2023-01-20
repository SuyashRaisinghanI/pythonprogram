# Python code to remove whitespace
#importing module
from functools import reduce
 
#Function to remove white space
def remove(string):
    return reduce(lambda x, y: (x+y) if (y != " ") else x, string, "");
     
# Driver Program
string = ' g e e k '
print(remove(string))
