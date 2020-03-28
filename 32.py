Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruit = fruits
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    fruit = fruits
NameError: name 'fruits' is not defined
>>> the_count = [1, 2, 3, 4, 5]
>>> fruits = ['apples', 'oranges', 'pears', 'apricots']
>>> change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
>>> fruit = fruits
>>> number = the_count
>>> i = change
>>> # this first kind of for- loop goes through a list
>>> for number in the_count:
print("This is count %d" % number)
# same as above
for fruit in fruits:
	
SyntaxError: expected an indented block
>>> for fruit in fruits:
	print("A fruit of type: %s" % fruit)
	# also we can go through mixed lists too
	# notice we have to use %r since we don't know what's in it
	for i in change:
		print("I got %r" % i)
		# we can also build lists, first start with an empty one
		elements = []

A fruit of type: apples
I got 1
I got 'pennies'
I got 2
I got 'dimes'
I got 3
I got 'quarters'
A fruit of type: oranges
I got 1
I got 'pennies'
I got 2
I got 'dimes'
I got 3
I got 'quarters'
A fruit of type: pears
I got 1
I got 'pennies'
I got 2
I got 'dimes'
I got 3
I got 'quarters'
A fruit of type: apricots
I got 1
I got 'pennies'
I got 2
I got 'dimes'
I got 3
I got 'quarters'
>>> I got 'quarters'# then use the range function to do 0 to 5 counts
SyntaxError: invalid syntax
>>> # then use the range function to do 0 to 5 counts
>>> for i in range(0, 6):
	print("Adding %d to the list." % i)
	# append is a function that lists understand
	elements.append(i)
	# now we can print them out too
	for i in elements:
		print("Element was: %d" % i)

		
Adding 0 to the list.
Element was: 0
Adding 1 to the list.
Element was: 0
Element was: 1
Adding 2 to the list.
Element was: 0
Element was: 1
Element was: 2
Adding 3 to the list.
Element was: 0
Element was: 1
Element was: 2
Element was: 3
Adding 4 to the list.
Element was: 0
Element was: 1
Element was: 2
Element was: 3
Element was: 4
Adding 5 to the list.
Element was: 0
Element was: 1
Element was: 2
Element was: 3
Element was: 4
Element was: 5
>>> 