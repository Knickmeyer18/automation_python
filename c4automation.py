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
print(alist[int(3.0)])

print()
# --------------------- LISTS WITH MULTIPLE INDEXES --------------------------

b_list = [['cat', 'bat'], [10, 20, 30, 40, 50]]

print( b_list[0] )
print( b_list[0][1] )
print( b_list[1][4] )


print()
# --------------------- NEGATIVE INDEXES --------------------------

c_list = [12,23,34,45,56,67,78,89,90]
print( c_list[-1] )
print( c_list[-3] )

print()
# --------------------- GETTING SUBLISTS WITH SLICES --------------------------

d_list =[2,4,6,8,10,12,14,16,18,20]

print( d_list[2] )
print( d_list[0:2] )
print( d_list[0:-1] ) # [2,4,6,8,10,12,14,16,18]
print( d_list[1:-1] ) # [4,6,8,10,12,14,16,18]
# print( d_list[-1:1] )  -- didn't work
print( d_list[2:-1] )
print( d_list[3:-1] )
print( d_list[4:-1] )
print( d_list[5:-1] )
print( d_list[6:-2] )


z = d_list[7:10] + d_list[0:3]
print(z)


print()
# -------------------CHANGING VALUE IN A LIST WITH INDEXES----------------------------
e_list = [1,3,5,7,9,11,13,15,17,19,21]

print(e_list)
e_list[0]= 'splunk'
print(e_list)



print()
# -----------------------------------------------

z = d_list[7:10] + d_list[0:3]
print(z)

y = e_list[:4]*3

print(y)

print()
# -------------------- Removing Values from lists with  DEL Statements ---------------------------
f_list = ['a', 'b', 'c', 'd']

print(f_list)
del f_list[1]
print(f_list)


'''
######################################################################################
A bad practice:
- creating many individual variables to store a group of similar values
--> IF the number of similar values changes, your program will never be able to store more
	of those values than you have variables. Also, these types of programs have a lot of 
	duplicate or nearly identical code in them.
INSTEAD OF USING MULTIPLE, REPETITIVE VARIABLES...

Solution:
- Use a single variable tht contains a list value.
--> BENEFITS OF USING LIST(S):
	-- your data is now in a structure 
	-- your program is more flexible in processing the data than it would be with repetitive variables
######################################################################################
'''
print()
# -------------------- FOR loops with lists ---------------------------

# 1st
for i in range(4):
	print(i)
print()
print('VS')
print()
# 2nd
for i in [0,1,2,3]:
	print(i)

'''
######################################################################################
- These two return values are the same because from 'range(4)' is a list-like value that python 
considers similar to [0,1,2,3]. 

*** the 2nd for loop actually loops through its clause with the variable i set to a 
	successive value in the [0,1,2,3] list in each iteration.
######################################################################################
'''

'''
######################################################################################
A COMMON PYTHON TECHNIQUE:
- use 'range(len(someList))' with a for loop to iterate over the indexes of a list. 

######################################################################################
'''

# print()
# -----------------------------------------------





# print()
# -----------------------------------------------





# print()
# -----------------------------------------------





# print()
# -----------------------------------------------

# print()
# -----------------------------------------------

# print()
# -----------------------------------------------

