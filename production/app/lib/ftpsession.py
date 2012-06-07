"""
Simplified ftp module 

Author: Shane Satterfield
Author: David Nuon
"""
import os
class FTPSession:
	def __init__(self, host, user, passwd):
		from ftplib import FTP
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

	# Finally working. Allows the user to download a file through ftp.
	def download(self, file, local_file):
		with open(local_file, 'wb') as f:
			def callback(data):
				f.write(data)
			self.ftp.retrbinary('RETR '+ file, callback)
	
	# Deletes file
	def rm(self, file):
		self.ftp.delete(file)

	# Quits out of the ftp session. Call this function when you are done using the object.
	def quit(self):
		self.ftp.quit()
		
	# Shows the files in the directory.
	def ls(self, path=''):
		list = []
		if path:
			list = self.ftp.nlst(path)
		else:
			list = self.ftp.nlst()

		b = 0
		for x in list:
			if "." in x:
				print x
				b+=1
		if b==0:
			print 'None.'
	
	# Shows the directories in the directories.
	def dir(self):
		pass
		
	# Creates a file in the current directory.
	def create_file(self, file):
		with open(file, 'w+') as f:
			pass
		self.ftp.storbinary('STOR '+file, open(file, 'rb'))
		os.remove(file)
	
	# Remvoes a directory located at path.
	def rmdir(self, path):
		self.ftp.rmd(path)
	

	# Creates a directory.
	def mkdir(self, pathname):
		self.ftp.mkd(pathname)
		

	# Returns if there is a file in path.
	def file_exists(self, filename):
		pass
		
	# Returns if there is given directory in path.
	def dir_exists(self, dirName):
		pass
		
	# Forced close from the ftp session.
	def close(self):
		self.ftp.close()
		