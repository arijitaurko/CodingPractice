# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 10:39:53 2022

@author: Aurko
"""


# Python Iterative program to add
# two linked lists
class Node:
	def __init__(self,val):
		self.data = val
		self.next = None
	
l1, l2, result = None,None,0

# To push a new node to linked list
def push(new_data):

	global l1

	# Allocate node
	new_node = Node(0)

	# Put in the data
	new_node.data = new_data

	# Link the old list off the new node
	new_node.next = l1

	# Move the head to point to the new node
	l1 = new_node


def push1(new_data):

	global l2

	# Allocate node
	new_node = Node(0)

	# Put in the data
	new_node.data = new_data

	# Link the old list off the new node
	new_node.next = l2

	# Move the head to point to
	# the new node
	l2 = new_node

# To add two new numbers
def addTwoNumbers():

	global l1,l2,result

	stack1 = []
	stack2 = []

	while (l1 != None):
		stack1.append(l1.data)
		l1 = l1.next

	while (l2 != None):
		stack2.append(l2.data)
		l2 = l2.next

	carry = 0
	result = None

	while (len(stack1) != 0 or len(stack2) != 0):
		a,b = 0,0

		if (len(stack1) != 0):
			a = stack1.pop()

		if (len(stack2) != 0):
			b = stack2.pop()

		total = a + b + carry

		temp = Node(total % 10)
		carry = total // 10

		if (result == None):
			result = temp
		else:
			temp.next = result
			result = temp


	if (carry != 0):
		temp = Node(carry)
		temp.next = result
		result = temp
		
	return result


# To print a linked list
def printList():

	global result

	while (result != None):
		print(result.data ,end = " ")
		result = result.next

# Driver code
	
arr1 = [ 5, 6, 7 ]
arr2 = [ 1, 8 ]

size1 = 3
size2 = 2

# Create first list as 5->6->7

for i in range(size1-1,-1,-1):
	push(arr1[i])

# Create second list as 1->8
for i in range(size2-1,-1,-1):
	push1(arr2[i])

result = addTwoNumbers()

printList()

# This code is contributed by shinjanpatra
