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

	def __str__(self):
		return self.name + " : " + self.position

	def __repr__(self):
		return self.name + " : " + self.position


class OfficerRoll(MarkdownList):
	__execs = None
	__appos = None
	__csv_string = ""

	def __init__(self, csv):
		MarkdownList.__init__(self, True)
		self.__execs = []
		self.__appos = []
		self.__csv_string = csv
		self.__csvParse()
		self.__render()

	def __checkMember(self, officer):
		if isinstance(officer, Officer):
			return Officer
		else:
			return None

	def __addExec(self, officer):
		if self.__checkMember(officer) == None:
			raise TypeError("Must add an officer")
		else:
			self.__execs.append(officer)

	def __addAppointed(self, officer):
		if self.__checkMember(officer) == None:
			raise TypeError("Must add an officer")
		else:
			self.__appos.append(officer)

	def __csvParse(self):
		member_data  = map(lambda x: x.split(","), self.__csv_string.split("\n"))

		__execs = []
		__appos = []
		
		index = 0
		for row in member_data:
			officer = Officer(row[0], row[1], row[2])

			if index > 0:
				admin =  row[-1] == '1' if True else False
				if admin:
					self.__addExec(officer)
				else:
					self.__addAppointed(officer)
			index += 1

	def __render(self):
		# The Lists
		exec_list = MarkdownList(True)
		exec_list.append("Administrative Cabinet")

		appo_list = MarkdownList(True)
		appo_list.append("Appointed Officers")

		# The Officer Type: Executive and Appointed
		exec_list_members = MarkdownList(True)
		appo_list_members = MarkdownList(True)

		for officer in self.__execs:
			exec_list_members.append(officer.position + " - " + officer.name + ": ")

		for officer in self.__appos:
			appo_list_members.append(officer.position + " - " + officer.name + ": ")

		self.append("Roll Call")
		exec_list.append(exec_list_members)
		appo_list.append(appo_list_members)

		self.append(exec_list)
		self.append(appo_list)

class OfficerBusiness(OfficerRoll):
	def __init__(self, csv):
		OfficerRoll.__init__(self, csv)
		self._ordered = True
		self._clear()
		self.__render()

	def __render(self):
		self.append("Faculty Advisor:")

		for member in self._OfficerRoll__execs:
			self.append(member.position + ":")

		for member in self._OfficerRoll__appos:
			self.append(member.position + ":")
