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
print()

g_list = []

for i in range(10):
	g_list.append(i)

print(g_list)
for j in range(len(g_list)):
	print("index " + str(j) + ' in g_list is: ' + str(g_list[j]))

'''
######################################################################################
- Using range(len(g_list)) in the previously shown for loop is handy because the code
in the lopcan access the index (as the variable j) and the value at that index as 
(g_list[j]). Best of all, range(len(g_list)) will iterate through all the indexes of
g_list, no matter how many items it contains.
######################################################################################
'''
print()

var = 2
var2 = 11

print(var in g_list)
print(var2 in g_list)
print('--------------------')
print(var not in g_list)
print(var2 not in g_list)

print()
# -----------------------------------------------
h_list = [1,2,3]
first, second, third = h_list

print(first, second, third)
print()
uno, dos = 1,2
uno, dos = dos, uno
print(uno, dos)
print()

'''
######################################################################################
List Methods:
 - index() -- provides the index of the specified value in the parenthesis
 - append(Val) -- adds its argument to the end of the list
 - insert( indexNum, Val) -- NEEDS two arguments... inserts the given value at that index
 - remove()-- removes given argument from list
 - sort() -- can take an unordered list and give it order
######################################################################################
'''
i_list = []
for j in range (10):
	i_list.append(j)

i_list.sort(reverse=True)
print(i_list)
'''
 ABOUT SORT() METHOD:
 1)  this method sorts the list in place, don't try to capture the return value by writing
 code like i_list=i_list.sort()

 2)  cannot sort lists that have both number values AND string values in them.
 
 3)  sort() uses "ASCIIbetical order" rather than alphabetical order for sorting strings. 
	This means  uppercase letters come before lowercase letters. Therefore lowercase 'a'
	comes after Uppercase 'Z'
	SOLUTION:
	pass str.lower for key keyword argument in the sort() method call
	vvvvvvvvvvvvvvvvv
'''
letter_list =['a','z','A','Z']
# without solution
letter_list.sort()
print(letter_list)
print()
# WITH SOLUTION
letter_list.sort(key=str.lower)
print(letter_list)


# print()
# -----------------------------------------------

'''
######################################################################################

List-Like Types: Strings and Tuples
- strings and lists are similar -- consider a string a list of text characters
-- many of the things you can do with lists, you can do with strings (indexing, slicing, 
using for loops, with len(), and with the 'in' and 'not in' operators. )
--------------------------------------------------------------------------------------
Mutable and Immutable Data Types
- lists and Strings are different in an IMPORTANT WAY ==> 
A list:
	- is a mutable data type: It can have values added, removed, or changed
a String:
	- is immutable data type: It cannot be changed. Trying to reassign a single character
	in a string results in a TypeError error

The proper way to "mutate" a string is to use slicing and concatenation to build a new string
by copying from parts of the old string
 

######################################################################################
'''



print()
# -----------------------------------------------

'''
######################################################################################
The Tuple Data Type
- almost identical to the list data type EXCEPT...
	1. tuples are typed with parentheses instead of square brackets
######################################################################################
'''
a_tuple = ('abc',1,2.0)
print(a_tuple[0])

print()

'''
######################################################################################
Main difference between tuples and lists
	2. Tuples cannot have their values modified, appended, or removed. Trying to do so
	will cause a TypeError error
######################################################################################
'''
# print()
# -----------------------------------------------

# print()
# -----------------------------------------------

# print()
# -----------------------------------------------



'''
######################################################################################

######################################################################################
'''
'''
######################################################################################

######################################################################################
'''