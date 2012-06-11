"""
Simplified ftp module 

Author: Shane Satterfield
Author: David Nuon
"""
import os
import ftplib
class FTPSession:

    _dirList = []
    _fileList = []
    _bothList = []

    def __init__(self, host, user, passwd):
        try:
            if user:
                self.ftp = ftplib.FTP(host, user, passwd)
            else:
                self.ftp = ftplib.FTP(host)
            self._generate_list()
        except ftplib.error_perm:
            pass

    def _generate_list(self):
        global _dirList
        global _fileList
        global _bothList

        list = self.ftp.nlst()

        _fileList = []
        _dirList = []
        _bothList = []

        for x in list:
            # Var is the the name of the file/directory that is x.
            var = ''

            #This pulls out the parent directories that may be attached to the path.
            if '/' in x:
                temp = x.split('/')
                var = temp.pop()

            #If no parent directories are in the path, then var is simply x.
            else:
                var = x

            _bothList.append(var)

            #Checks to see if var is a file or directory, then appends var into the respective list.
            if "." in x:
                _fileList.append(var)

            else:                
                _dirList.append(var)


    # Shows the files in the current directory.
    def ls(self):
        self._generate_list()
        global _fileList
        
        return _fileList

    # Shows the directories in the directories.
    def dir(self):
        self._generate_list()
        global _dirList
        return _dirList

    # Shows what is in the current directory (both files and directories).
    def list(self):
        self._generate_list()
        global _bothList

        return _bothList

    # Changes the directory to the give path.
    def cd(self, path):
        try:
            self.ftp.cwd(path)
            self._generate_list()
        except ftplib.error_perm:
            pass

    # file is the filepath
    # path is the path to the directory you want to upload to
    def upload(self, file):
        try:
            self.ftp.storbinary('STOR '+file, open(file, 'rb'))
            self._generate_list()
        except IOError:
            pass

    # Finally working. Allows the user to download a file through ftp.
    def download(self, file, local_file):
        with open(local_file, 'wb') as f:
            def callback(data):
                f.write(data)
            try:
                self.ftp.retrbinary('RETR '+ file, callback)
            except IOError:
                pass
    
    # Deletes file
    def rm(self, file):
        try:
            self.ftp.delete(file)
            self._generate_list()
        except ftplib.error_perm:
            pass

    # Quits out of the ftp session. Call this function when you are done using the object.
    def quit(self):
        self.ftp.quit()
        
    # Creates a file in the current directory.
    def create_file(self, file, content=""):
        with open(file, 'w+') as f:
            if content:
                f.write(content)
        self.ftp.storbinary('STOR '+file, open(file, 'rb'))
        os.remove(file)
        self._generate_list()

    # Remvoes a directory located at path.
    def rmdir(self, dirname):
        try:
            self.ftp.rmd(dirname)
            self._generate_list()
        except ftplib.error_perm:
            pass
    
    # Creates a directory.
    def mkdir(self, dirname):
        self.ftp.mkd(dirname)
        self._generate_list()

    # Returns if there is a file in path.
    def file_exists(self, filename):
        global _fileList

        for x in _fileList:
            if x == filename:
                return True
        return False
        
    # Returns if there is a directory dirName in the current directory.
    def dir_exists(self, dirName):
        #This variable hold the list of directories in the current directory.
        global _dirList

        for x in _dirList:
            if x == dirName:
                return True

        return False
        
    # Forced close from the ftp session.
    def close(self):
        self.ftp.close()