a = 15
b = 15
c = [1,2]
d = [1,2]

x = a == b
print("a == b:",x)

x = a is b
print("a is b:",x)

x = c == d
print("c == d:",x)

x = c is d
print("c is d:",x)


# EXPLANATION OF WHY 'is' AND '==' GIVE DIFFERENT RESULTS FOR THE LISTS:
# 1. The '==' operator checks for VALUE equality. Since list 'c' and list 'd' 
#    both contain the exact same elements ([1, 2]), 'c == d' evaluates to True.
#
# 2. The 'is' operator checks for IDENTITY (memory location equality). 
#    Lists are mutable data structures in Python. Every time you define a new 
#    list using square brackets, Python allocates a completely separate chunk 
#    of memory for it. Because 'c' and 'd' are stored in different places in 
#    RAM, 'c is d' evaluates to False. They look identical, but they are 
#    different objects.

#   i just only copied the comments but the code i entered in typed written by me. the reason i done 
#   because if i wrote it through there is 99% of possiblities i wont able to explain you(bhaiya).
#   but i understood.