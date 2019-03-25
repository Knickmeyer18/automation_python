# c5automation
'''
====================================================================================================
Dictionary Data Type
- a collection of many values
- indexes for dictionaries can use many different data types, NOT just integers
- indexes for dictionaries are called 'keys', each key has an associated value  --> key-value pair
- dictionary is typed with braces, {}
- Dictionaries can still use integer values as keys, but they do not have to start at 0.. can be any #

====================================================================================================


'''
my_car = {'brand': 'VW', 'color':'black', 'model': 'Jetta'}
print(my_car['color'])
print()

fib_nums = {1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13}
print(fib_nums[7])

print()
#------------------------------------------------------------------------
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam==bacon)

print()
#------------------------------------------------------------------------


eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)

'''
Order doesn't matter for determining whether two dictionaries are the same` 
Dictionaries are UNORDERED -->  CANNOT be sliced like lists


Though Dictionaries aren't ordered, the fact that you can have arbitrary values for the KEYS
allows you to organize your data in powerful ways.
HOWEVER, all the stored data in this program is forgotten when the program terminates -- You'll
have to save data to files on the hard drive
'''

print()
#------------------------------------------------------------------------
'''
Dictionary Methods: keys(), values(), and items() 

values returned by these methods are not true lists:
- cannot be modified 
- do not have an append() method
- these values (dict_keys, dict_values, dict_items, respectively) CAN be used in FOR LOOPS

'''
fib_nums2 = {1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13}
for i in fib_nums2.values():
    print(i)
for j in fib_nums2.keys():
    print(j)
for k in fib_nums2.items():
    print(k)

print()
'''
If you want a TRUE LIST from one of these methods, pass its like-like return value to the 'list()' function
'''
not_true_list_type=fib_nums2.keys()
print(not_true_list_type)           # prints as dict_keys([1, 2, 3, 4, 5, 6, 7])
print(type(not_true_list_type))     # prints as <class 'dict_keys'>
print('-----------------------------')

true_list_type=list(fib_nums2.keys())
print(true_list_type)
print(type(true_list_type))


print()
#------------------------------------------------------------------------
'''
CHECKING Whether a Key or Value Exists  in a Dictionary
- use of the 'in' and 'not' operators and dict_methods
EX:
'''
dict_practice = {'name':'Eric', 'age':23, 'eye color': 'blue','left-handed':True}

print('name' in dict_practice.keys())
print('Eric' not in dict_practice.values())
print('hair color' in dict_practice.keys())
print(True in dict_practice.values())

print()
#------------------------------------------------------------------------
'''
The get() Method
- takes two arguments (1) the key of the value to retrieve and (2) a fallback value to return if that key doesn't exist

'''
picnicItems = {'apples': 5, 'cups': 2}
print("I am bringing "+ str(picnicItems.get('cups', 0)) + ' cups')
print("I am bringing "+ str(picnicItems.get('eggs', 0)) + ' eggs')


print()
#------------------------------------------------------------------------

'''
The setdefault() Method
- when you need to set a value in a dictionary for a certain key only if that key does not already have a value
- takes 2 arguments (1) is the key to check for, (2) the value to set at that key IF THAT KEY does not exist
'''

print()
#------------------------------------------------------------------------
'''
Pretty Printing - importing pprint module--> allows for printing out an 'easy to read' format printed out 

'''
print()
#------------------------------------------------------------------------

"""
USING DATA STRUCTURES TO MODEL REAL-WORLD THINGS
"""

print()
#------------------------------------------------------------------------
'''


'''