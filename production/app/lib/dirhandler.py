"""
	Class to provide a convenient way to handle directories and files
	with a given path.

	Author: David Nuon
"""
import os
import shutil
import sys

class DirHandler:
	__dir_path  = ''
	__file_list = []

	def __init__(self, path):
		self.__dir_path = path
		self.generate_list()

	def generate_list(self):
		# Get the output of os.walk as a list
		# then get only files of the root, [0]
		# then get only directories, [1]

		self.__file_list = [n for n in os.walk(self.__dir_path)][0][1]

	def get_list(self):
		return self.__file_list

	def mkdir(self, dirname):
		dir_path = os.path.join(self.__dir_path, dirname)
		if not os.path.exists(dir_path):
			os.mkdir(dir_path)
			self.generate_list()
		else:
			raise IOError("Directory already exists")

	def rm(self, filename, dirname = '.'):
		path = os.path.join(self.__dir_path, filename)
		try:
			if not dirname == '.':
				path = os.path.join(self.__dir_path, dirname, filename)

			os.remove(path)
		except:
			raise IOError("Unable to delete file")

	def rmdir(self, dirname):
		dir_path = os.path.join(self.__dir_path, dirname)

		# We want to delete a directory and all of its contents
		shutil.rmtree(dir_path)
		self.generate_list()

	def create_file(self, filename, content, dirname = '.'):
		path = os.path.join(self.__dir_path, filename)
		if dirname != '.':
			path = os.path.join(self.__dir_path, dirname, filename)

		with open(path, 'w+') as f:
			f.write(content)