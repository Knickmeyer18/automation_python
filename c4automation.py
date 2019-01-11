# ====================================================================================================
# import c3automation
# c3automation.hello(9, 'eric')
# print(c3automation.practice_exception_handling_function(2))
# ====================================================================================================

'''
# ====================================================================================================
# Chapter 4: Lists
# ====================================================================================================
'''
'''
- A 'list' is a value that contains multiple values in an ordered sequence
- 'list value' >> refers to the list itself - a value that can be stored in a 
	variable or passed to a function like any other value, NOT the values inside the list value
		-- a list value looks like:
				['a','b','c']
- list begins and ends with []
- items within are called 'items'
- 'items' are separated by commas (they are 'comma-delimited')
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
'''
print()
alist = ['aaa', 1, 2.0, True]

print(alist)
print('----------------------')

print(type(alist), '--> type of the list')

print('----------------------')

for i in range(len(alist)):
	print(type(alist[i]))
	print('----------------------')