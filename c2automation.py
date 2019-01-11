# Automate the Boring Stuff with Python

# https://automatetheboringstuff.com/#toc

#skipping chapters pertaining to material I have a good grasp on

import random, sys, os, math
'''
====================================================================================================
Chapter 2: Flow Control
====================================================================================================
Discussion: 
- Boolean Values
- Comparison Operators
- Boolean Operators
- Conditions
- Blocks of Code
- if Statements
- else Statements
- elif Statements
- while Loop Statements
- break Statements
- continue Statements
- for Loops and range() Function
- import Modules
- Ending a Program Early with sys.exit()
 
 '''


t = True
f = False

a1 = t and t
a2 = t and f
a3 = f and t
a4 = f and f
# -----------
a5 = t or t
a6 = t or f
a7 = f or t
a8 = f or f

# print(a1, a2, a3, a4, a5, a6, a7, a8) # Correct

a9 = not t
a10 = not f

#print(a9, a10)


s1 = (4<5) and (5<6)
s2 = (4<5) and (9<6)

#print(s1, s2)

d1 = (1==2) or (2==2)

f1 = True and (5<6)

# print()
# ------------------------------------------------
# name = 'bob'
# age = 30
# if name == 'alice':
# 	print('Hi, alice')
# else:
# 	print('hi, stanger')


# #print()
# # ------------------------------------------------
# name = 'bob'
# age = 30
# if name == 'alice':
# 	print('hi, alice')
# elif age < 12:
# 	print('you are not alice, kid')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal vampire.')
# elif age > 100:
#     print('You are not Alice, grannie.')	

# print()
# # ------------------------------------------------

# name = 'bob'
# age = 30
# if name == 'alice':
# 	print('hi, alice')
# elif age < 12:
# 	print('you are not alice, kid')
# else:
# 	print('You are neither alice nor a little kid.')


# print()
# # ------------------------------------------------
# spam = 0
# while spam < 5:
# 	print ("Hello World!")
# 	spam = spam + 1


# print()
# ------------------- while loop -----------------------------
# name =''
# while name != 'xxx':
# 	print('type something:')
# 	name = input()
# print('thanks')

#print()
# -------------------- break STATEMENT ----------------------------
# while True:                         # <---- creates an INFINITE LOOP
# 	print('please type your name:')
# 	name = input()
# 	if name == 'your name':
# 		break						 # <----- prgm will only exit when the break statement is executed.				
# print('Thank you!')


# print()
# --------------------- continue statement ---------------------------
# while True:
# 	print('who are you?')
# 	name = input()
# 	if name != 'Joe':
# 		continue
# 	print("hello Joe. what is the password?")
# 	password = input()
# 	if password == 'swordfish':
# 		print('Access granted.')
# 		break


# print()
# --------------------for LOOPS and range() FUNCION---------------------------

# for i in range(5):
# 	print('will stop on the fifth iteration' +'('+ str(i) +')' )

# print('------------')

# j=0 # Counter
# while j < 5:
# 	print('will stop on the fifth iteration ('+str(j)+')')
# 	j+=1	


# print('------------')


# total = 0
# for num in range(101):
# 	total=total + num
# print(total)


# print('------------')


# total_1 = 0
# for num in range(100):
# 	total_1=total_1+num
# print(total_1)


# print('------------')


# print()
# # -----------------------------------------------
# for k in range(12,16):
# 	print(k)


# print()
# # -----------------------------------------------
# for l in range (0,10,2):
# 	print(l)


# print()
# # -----------------------------------------------
# for e in range(5,-1,-1):
# 	print(e)

# print()
# # -----------------------------------------------
# while True:
# 	print('Type exit to exit.')
# 	response = input()
# 	if response == 'exit':
# 		sys.exit()
# 	print('You typed '+ response +'.')

# print()
# -----------------------------------------------


# print()
# -----------------------------------------------
test_variable = print('testing variable')

class test_class:
	
	def test_function(x=None,y=None):
		test='this is a test.'
		print(test)

# test_function()