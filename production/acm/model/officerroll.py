import csv

from ..util.markdownfile import MarkdownList

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
	__execs    = None
	__appos    = None
	__projects = None

	__csv_string = ""

	def __init__(self, csv):
		MarkdownList.__init__(self, True)
		self.__execs    = []
		self.__appos    = []
		self.__projects = []

		self.__csv_string = csv
		self.__csvParse()
		self.__render()

	def __checkMember(self, officer):
		if isinstance(officer, Officer):
			officer.name = officer.name.replace("\t", "")
			return officer
		else:
			return None

	def __addProject(self, officer):
		if self.__checkMember(officer) == None:
			raise TypeError("Must add an officer")
		else:
			self.__projects.append(self.__checkMember(officer))

	def __addExec(self, officer):
		if self.__checkMember(officer) == None:
			raise TypeError("Must add an officer")
		else:
			self.__execs.append(self.__checkMember(officer))

	def __addAppointed(self, officer):
		if self.__checkMember(officer) == None:
			raise TypeError("Must add an officer")
		else:
			self.__appos.append(self.__checkMember(officer))

	def __csvParse(self):
		member_data  = map(lambda x: x.split(","), self.__csv_string.split("\n"))
	
		index = 0
		for row in member_data:
			officer = Officer(row[0], row[1], row[2])

			if index > 0:
				admin   =  row[-1] == '1' if True else False
				project =  row[-1] == '2' if True else False

				if admin:
					self.__addExec(officer)
				elif project:
					self.__addProject(officer)
				else:
					self.__addAppointed(officer)

			index += 1

	def __render(self):
		# The Lists
		exec_list = MarkdownList(True)
		exec_list.append("Administrative Cabinet")

		appo_list = MarkdownList(True)
		appo_list.append("Appointed Officers")

		proj_list = MarkdownList(True)
		proj_list.append("Project Managers")

		# The Officer Type: Executive and Appointed
		exec_list_members = MarkdownList(True)
		appo_list_members = MarkdownList(True)
		proj_list_members = MarkdownList(True)

		for officer in self.__execs:
			exec_list_members.append(officer.position + " - " + officer.name + ": ")

		for officer in self.__appos:
			appo_list_members.append(officer.position + " - " + officer.name + ": ")


		for officer in self.__projects:
			proj_list_members.append(officer.position + " - " + officer.name + ": ")

		exec_list.append(exec_list_members)
		appo_list.append(appo_list_members)
		proj_list.append(proj_list_members)

		self.append(exec_list)
		self.append(appo_list)
		self.append(proj_list)

		self.add_list_heading("Approval of the Agenda:")
		self.add_list_heading("Approval of the Minutes:")

class OfficerBusiness(OfficerRoll):
	def __init__(self, csv):
		OfficerRoll.__init__(self, csv)
		self._ordered = True
		self._clear()
		self.__render()

	def __render(self):
		self.append("Officer Reports:")

		officers = MarkdownList(True)

		officers.append("Faculty Advisor:")

		for member in self._OfficerRoll__execs:
			officers.append(member.position + ":")

		for member in self._OfficerRoll__appos:
			officers.append(member.position + ":")

		self.append(officers)

