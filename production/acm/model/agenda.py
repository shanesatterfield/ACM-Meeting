import sys

from officerroll import OfficerRoll, OfficerBusiness
from ..util.markdownfile import MarkdownList

class Agenda(MarkdownList):
	__csv = ""

	def __init__(self, csv):
		MarkdownList.__init__(self, True)
		self.__csv = csv
		self.__agenda()

	def __agenda(self):
		officerbusiness = OfficerBusiness(self.__csv)
		officerroll     = OfficerRoll(self.__csv)

		self.append("Call To Order")

		self.add_list_heading("Roll Call")
		self.append(officerroll)
		self.add_list_heading("Announcements:")

		business = MarkdownList(True)
		business.append("Business:")
		business.append(officerbusiness)
		business.add_list_heading("Old Business:")
		business.add_list_heading("New Business:")
		self.append(business)

		self.append("Adjournment")