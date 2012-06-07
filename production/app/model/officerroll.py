import sys
import csv

sys.path.insert(0, '../lib')

from markdownfile import MarkdownList

class Officer:
	name     = ""
	position = ""
	email    = ""

	def __init__(self, name, position, email):
		self.name     = name
		self.position = position
		self.email    = email

class OfficerRoll(MarkdownList):
	execs = []
	appos = []

	def __init__(self, csv, ordered = True):
		MarkdownList.__init__(self, ordered)

	def _checkMember(self, officer):
		if isinstance(officer, Officer):
			return Officer
		else:
			return None

	def _addExec(self, officer):
		if self._checkMember(officer) == None:
			raise TypeError("Must add an officer")
		else:
			self.execs.append(officer)

	def _addAppointed(self, officer):
		if self._checkMember(officer) == None:
			raise TypeError("Must add an officer")
		else:
			self.appos.append(officer)

	def _csvParse(self, csv_text):
		try:
			member_data = csv.reader(csv_text)

			execs = []
			appos = []
			
			index = 0
			for row in member_data:
				officer = Officer(row[0], row[1], row[2])

				if index > 1:
					admin =  row[-1] == '1' if True else False
					if admin:
						self._addExec(officer)
					else:
						self._addAppointed(officer)
				index += 1
		except:
			raise TypeError

	def render(self):
		pass # TODO : Write function that will spit out markdown for this