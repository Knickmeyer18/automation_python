# Automate the Boring Stuff with Python

# https://automatetheboringstuff.com/#toc

#skipping chapters pertaining to material I have a good grasp on


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

print(a1, a2, a3, a4, a5, a6, a7, a8) # Correct

a9 = not t
a10 = not f

print(a9, a10)


s1 = (4<5) and (5<6)
s2 = (4<5) and (9<6)

print(s1, s2)

d1 = (1==2) or (2==2)

f1 = True and (5<6)

print()
# ------------------------------------------------
name = 'bob'
if name == 'alice':
	print('Hi, alice')
else:
	print('hi, stanger')


print()
# ------------------------------------------------
name = 'bob'
if name == 'alice':
	print('hi, alice')
elif age < 12:
	print('you are not alice, kid')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')	


'''
====================================================================================================
Chapter 3: 
====================================================================================================


'''








'''
====================================================================================================
Chapter 4:
====================================================================================================


'''


























