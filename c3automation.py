
# '''
# ====================================================================================================
# Chapter 3: Functions
# ====================================================================================================


# '''
import random 
# import c2automation

# c2automation.test_variable

# c2_module=c2automation.test_class()
# c2_module.test_function()


# # ------------------------------

# def hello(name, it):
# 	for i in range(it):
# 		print("Hello " + name)

# hello('eric', 2)

# print()
# # ------------- magic eight-ball -----------------

# def magic_8_Ball(ansNum):
# 	if ansNum==1:
# 		return 'It is certain'
# 	elif ansNum==2:
# 		return 'It is decidedly so'
# 	elif ansNum==3:
# 		return 'Yes'
# 	elif ansNum==4:
# 		return 'Ask again later'
# 	elif ansNum==5:
# 		return 'Concentrate and ask again'
# 	elif ansNum==6:
# 		return 'My reply is no'
# 	elif ansNum==7:
# 		return 'Outlook not so good'
# 	elif ansNum==8:
# 		return 'Very doubtful'

# r = random.randint(1,8)
# fortune=magic_8_Ball(r)
# print(fortune)

# # ^ this can work OORR this...(below)

# print(magic_8_Ball(random.randint(0,8))) # <-- random.randint() evaluates a random int btwn 0-8, including 0 and 8**

# '''
# ** 
# REMEMBER: expressions are composed of values and operators. A FUNCTION CALL can be used in an expression because
# 	it evaluates to its return value.
# '''

# print()
# # ------------ The None Value / Keyword Arguments and print() ------------------

# '''
# None value (must be capital 'N') >> represents the absence of a value. Its the only value of the NoneType data type. (Other programming
#  languages might call this value 'null', nil', or 'undefined')
# ====================
# Keyword arguments and print() >>  are identified by the keyword put before them in the function call. Often used for 
# 	optional parameters
# 	-- keyword arguments:
# 			- end=
# 			- sep=
# EX:
# '''
# print('hello')
# print('world')
# print('-----------')
# print('Hello', end='')  # <<output is printed on a single line b/c there is no longer a new-line printed after 'Hello'
# print('world')
# print('-----------')
# print('Hello', end='zzz') # << 'zzz' will be between 'Hello' & 'World'
# print('world')
# print('-----------')
# print('Hello', 'goodbye','greetings')  # <<output is printed with separation between the three strings
# print('------------')
# print('Hello', 'goodbye','greetings', sep=',') # << output dependant on the sep=
# print('------------')
# print('Hello', 'goodbye','greetings', sep=', ') # << output dependant on the sep=

# print()
# # ------------- Local and Global Scope -----------------
# '''
# local scope: 
# 	- parameters and variables assigned in a called function exist in the function's 'local scope'
# 	-- i.e. local variable
# global scope:
# 	- variables assigned outside all functions exist in the 'global scope'
# 	-- global variable
# ** - A VARIABLE MUST BE EITHER LOCAL OR GLOBAL, it cannot be of both scopes
# '''
# # def spam():
# # 	eggs = 1000
# # spam()
# # print(eggs)
# # this call causes an ERROR

# def spam():
# 	eggs=99
	
# 	print(eggs, 'This is from the spam function', sep=' | --> ')
# 	bacon()

# def bacon():
# 	ham = 101
# 	eggs = 50
# 	print(eggs, 'This is from the bacon function', sep=' | --> ')

# spam()


# print()
# ------------ Local and Global Variables with the SAME NAME ------------------
# def foo():
# 	bar = 'foo ++ local'
# 	print(bar)

# def too():
# 	bar = 'too -- local'
# 	print(bar)
# 	foo()
# 	print(bar )

# bar = 'global'
# too()
# print(bar)

# there are three different bar variables.


# print()
# # ------------ Global Statement ------------------

# '''
# If you need to modify a global variable from within a function, use the 'global' statement.
# Using the statement in a function (typically identifying the variable at the top of the function)
# tells Python that the specified variable is a global variable as to prevent a local variable of the same 
# name from being created.

# EX:
# '''
# def foo():
# 	global bar
# 	bar = '-- global variable inside the function --'
# 	print(bar)

# bar = '++ global variable outside the function ++'
# foo()
# print(bar, '#2')

# '''
# 			******* NEED TO BE VERY CAREFUL WHEN DEALING WITH GLOBAL VARIABLES ********
# '''


# print()
# ------------ Exception Handling ------------------
'''
Getting errors or 'exceptions' will cause a program to crash. Don't want this to happen in real-world
programs. Instead, we want the program to detect errors, handle them, and continue running.
'''

def practice_exception_handling_function(divided_by): # a function to divide numbers by ZERO and other #s can cause an error
	return 42 / divided_by

try:
	print(practice_exception_handling_function(2))
	print(practice_exception_handling_function(7))
	print(practice_exception_handling_function(12))
	print(practice_exception_handling_function(0)) # this initially caused an error
except ZeroDivisionError:
	print('Error HERE: Invalid argument')
 

 