"""
Simplified ftp module 

Author: Shane Satterfield
Author: David Nuon
"""
class FTPSession:
	def __init__(self, host, user, passwd):
		from ftplib import FTP
		import os
		if user:
			self.ftp = FTP(host, user, passwd)
		else:
			self.ftp = FTP(host)

	# Shows what is in the current directory.
	def list(self):
		self.ftp.dir()

	# Changes the directory to the give path.
	def cd(self, path):
		self.ftp.cwd(path)

	# file is the filepath
	# path is the path to the directory you want to upload to
	def upload(self, file):
		self.ftp.storbinary('STOR '+file, open(file, 'rb'))

	# Inprogress
	def download(self, file, local_file):
		pass
		"""with open('local_file', 'wb') as f:
			self.ftp.retrbinary('RETR '+ file, lambda data: f.write(data))"""
	
	# Deletes file
	def rm(self, file):
		self.ftp.delete(file)

	# Quits out of the ftp session. Call this function when you are done using the object.
	def quit(self):
		self.ftp.quit()

	def ls(self):
		pass
		# Shows the files in the directory.

	def dir(self):
		pass
		# Shows the directories in the directories.

	def create_file(self, filename):
		with open(filename, 'w+') as f:
			pass
		upload(filename)
		os.remove(filename)
		# Creates a file in the current directory.

	def rmdir(self, path):
		self.ftp.rmd(path)
		# Remvoes a directory located at path.

	def mkdir(self, pathname):
		self.ftp.mkd(pathname)
		# Creates a directory.

	def file_exists(self, filename):
		pass
		# Returns if there is a file in path.

	def dir_exists(self, dirName):
		pass
		# Returns if there is given directory in path.

	def close(self):
		self.ftp.close()
		# Forced close from the ftp session.