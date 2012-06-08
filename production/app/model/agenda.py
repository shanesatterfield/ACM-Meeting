import sys

sys.path.insert(0, '../lib')

from officerroll import OfficerRoll, OfficerBusiness
from markdownfile import MarkdownList

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

if __name__ == "__main__":
	testdata = """name,position,email,exec
	David Nuon,President,chair@csulb.acm.org,1
	Ian Goegebuer,Vice President,vicechair@csulb.acm.org,1
	Christopher Gomez,Treasurer,treasurer@csulb.acm.org,1
	Shane Satterfield,Secretary,secretary@csulb.acm.org,1
	Victoria Hatfield,AESB Representative,aesbrep@csulb.acm.org,
	Anthony Gialcalone,Librarian,librarian@csulb.acm.org,
	Leo Tronolone,Publicity and Recruitment Chair,publicity@csulb.acm.org,
	James Coolidge,Market Manager,vendor@csulb.acm.org,
	Orion Sakorn,Historian,historian@csulb.acm.org,
	Diana Ignacio,Event Coordinator,events@csulb.acm.org,
	John-Jimi Kathleen Som,Webmaster,webmaster@csulb.acm.org,
	Johnny Patterson,Office Technician,tech@csulb.acm.org,
	Graham Otte,Codename: Fattybanana,tech@csulb.acm.org,2"""

	a = Agenda(testdata)
	print a.markdown()