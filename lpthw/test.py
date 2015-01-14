
#!/usr/bin/env python

# -*- coding: utf-8 -*-

class Parent(object):
	
	def __init__(self):
		self.name = "Parent"

	def printName(self):
		print self.name

class Child(Parent):

	def __init__(self):
		super(Child, self).__init__()
		self.childName = "Child"

	def printName(self):
		print "Parent"
		super(Child, self).printName()
		print "Child"
		print self.childName

father = Parent()
father.printName()
print "-" * 20
son = Child()
son.printName()
