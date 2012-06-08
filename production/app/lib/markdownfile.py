"""
	Class to provide a convenient way to create indented files

	Author: David Nuon
"""

import markdown
from indentedfile import IndentedFile

class MarkdownList(IndentedFile):
	_ordered = False
	_list_contents = []

	def __init__(self, ordered = False):
		IndentedFile.__init__(self)
		self._list_contents = []
		self._ordered = ordered

	def _clear(self):
		self._list_contents = []

	def append(self, item):
		if type(item) != str and not isinstance(item, MarkdownList):
			raise Exception("ValueError")
		else:
			self._list_contents.append(item)

	def add_list_heading(self, string):
		sublist = MarkdownList(True)
		sublist.append(string)
		self.append(sublist)

	def markdown(self, level=0):
		self._level = level
		init_level  = level

		for list_item in self._list_contents:
			if type(list_item) == str:
				self._level = init_level
				if self._ordered:
					self.write("0. " + list_item)
				else:
					self.write("- " + list_item)
			else:
				if isinstance(list_item, MarkdownList):
					self._level = 0 
					self.write(list_item.markdown(init_level + 1))

		return self._contents[:-1] # We want to take off the extra linebreak at the end

	# Handy things

	def __str__(self):
		print_list = []

		for item in self._list_contents:
			if type(item) == str:
				print_list.append(item)
			else:
				if isinstance(item, MarkdownList):
					print_list.append(item.__str__())

		return str(print_list)

	def __len__(self):
		return len(self._list_contents)

	def __getitem__(self, key):
		return self._list_contents[key]

	def __setitem__(self, key, item):
		if type(item) != str and not isinstance(item, MarkdownList):
			raise Exception("ValueError")
		else:
			self._list_contents[key] = item

	def __delitem__(self, key):
			self._list_contents.remove(self._list_contents[key])

	def __iter__(self):
		return (n for n in self._list_contents)

	def __contains__(self, item):
		return item in self._list_contents

class MarkdownFile(IndentedFile):
	def __str__(self):
		return markdown.markdown(self._contents)