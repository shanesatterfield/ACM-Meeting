"""
Simplified ftp module 

Author: Shane Satterfield
Author: David Nuon
"""
class ftp_session:
	def __init__(self, host, user, passwd):
		from ftplib import FTP
		if user:
			self.ftp = FTP(host, user, passwd)
		else:
			self.ftp = FTP(host)

	# Shows what is in the current directory.
	def ls(self):
		self.ftp.dir()

	# Changes the directory to the give path.
	def cd(self, path):
		self.ftp.cwd(path)

	# file is the filepath
	# path is the path to the directory you want to upload to
	def upload(self, file):
		self.ftp.storbinary('STOR '+file, open(file, 'rb'))

	# Inprogress
	"""
	def download(self, file, local_file):
		with open('local_file', 'wb') as f:
			self.ftp.retrbinary('RETR '+file, lambda data: f.write(data))
	"""
	# Deletes file
	def delete(self, file):
		self.ftp.delete(file)

	# Quits out of the ftp session. Call this function when you are done using the object.
	def quit(self):
		self.ftp.quit()