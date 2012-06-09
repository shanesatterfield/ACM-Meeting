"""
	Class to provide a convenient way to create indented files
	
	Author: David Nuon
"""
class IndentedFile:
	_indent  = "\t"
	_level   = 0
	_contents = ""

	def __init__(self, indent_type = None):
		if indent_type != None:
			self._indent = indent_type

	def tab(self):
		self._level += 1

	def untab(self):
		self._level -= 1
		if self._level < 0:
			self._level = 0

	def write(self, string):
		self._contents += self._indent*self._level + string + "\n"

	def set_level(self, n):
		if type(n) == type(0):
			self._level = n

	def set_contents(self, string):
		self._contents = str(string)

	def get_contents(self):
		return self._contents