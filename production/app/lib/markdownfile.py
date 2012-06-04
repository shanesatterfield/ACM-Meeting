"""
	Class to provide a convenient way to create indented files

	Author: David Nuon
"""

import markdown
from indentedfile import IndentedFile

class List(IndentedFile):
	_ordered = 0
	_list_contents = []

	def add_item(item):
		if type(item) != "str" or type(item) != List:
			raise Exception("ValueError")
		else:
			_list_comments.append(item)

class MarkdownFile(IndentedFile):
	def __str__(self):
		return markdown.markdown(self._contents)
