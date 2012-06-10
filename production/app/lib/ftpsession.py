"""
Simplified ftp module 

Author: Shane Satterfield
Author: David Nuon
"""
import os
import ftplib
from ftplib import FTP
class FTPSession:
    def __init__(self, host, user, passwd):
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
        try:
            self.ftp.storbinary('STOR '+file, open(file, 'rb'))
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
        except ftplib.error_perm:
            pass

    # Quits out of the ftp session. Call this function when you are done using the object.
    def quit(self):
        self.ftp.quit()
        
    # Shows the files in the current directory.
    def ls(self):
        list = []
        list = self.ftp.nlst()

        fileList = []

        for x in list:
            if "." in x:
                if '/' in x:
                    temp = x.split('/')
                    file = temp.pop()
                    fileList.append(file)

                else:
                    fileList.append(x)

        return fileList
    
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
    def rmdir(self, dirname):
        self.ftp.rmd(dirname)
    
    # Creates a directory.
    def mkdir(self, dirname):
        self.ftp.mkd(dirname)
        

    # Returns if there is a file in path.
    def file_exists(self, filename):
        path = ''
        list = []
        if '/' in filename:
            temp = filename.split('/')
            file = temp.pop()
            path = '/'.join(temp)
            list = self.ls(path)

        else:
            file = filename
            list = self.ls()

        for x in list:
            if x == file:
                return True

        return False
        
    # Returns if there is given directory in path.
    def dir_exists(self, dName):
        path = ''

        list = []

        if '/' in dName:
            temp = dName.split('/')
            dirName = temp.pop()
            path = '/'.join(temp)
            list = self.ftp.nlst(path)

        else:
            dirName = dName
            list = self.ftp.nlst()

        for x in list:
            if x.find('.') != -1:
                list.pop(list.index(x))

        for x in list:
            if x == dirName:
                return True

        return False
        
    # Forced close from the ftp session.
    def close(self):
        self.ftp.close()