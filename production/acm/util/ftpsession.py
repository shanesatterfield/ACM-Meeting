"""
Simplified ftp module 

Author: Shane Satterfield
Author: David Nuon
"""
import os
import ftplib
class FTPSession:

    _dir_path = ''

    _dirList = []
    _fileList = []
    _bothList = []
    _layer    =  0

    def __init__(self, host, user, passwd):
        try:
            if user:
                self.ftp = ftplib.FTP(host, user, passwd)
            else:
                self.ftp = ftplib.FTP(host)
            self._generate_list()
            self._dir_path = '/'
        except ftplib.error_perm:
            raise ftplib.error_perm('Cannot connect. Incorrect information.')

    def _generate_list(self):
        list = self.ftp.nlst()

        self._fileList = []
        self._dirList = []
        self._bothList = []

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

            self._bothList.append(var)

            #Checks to see if var is a file or directory, then appends var into the respective list.
            if "." in x:
                self._fileList.append(var)

            else:                
                self._dirList.append(var)


    # Shows the files in the current directory.
    def ls(self, full_tree = False):
        _list = self._fileList
        self._generate_list()

        if full_tree:
            _list = self.__recursive_list(recur = False, list_files = True, list_dir = False)

        return _list

    # Shows the directories in the directories.
    def dir(self, full_tree = False):
        _list = self._dirList
        self._generate_list()

        if full_tree:
            _list = self.__recursive_list(recur = False, list_files = False, list_dir = True)

        return _list

    # Shows what is in the current directory (both files and directories).
    # Pass full_tree as True to get the entire directory tree
    def list(self, full_tree = False):
        _list = []
        self._generate_list()

        if not full_tree:
            _list = self._bothList
        else:
            _list[:] += self.__recursive_list(recur = False, list_files = True, list_dir = True)

        return _list

    def __recursive_list(self, recur = False, list_files = False, list_dir = False):
        if recur:
            self._layer += 1

        _list = []
        
        if len(self._fileList) > 0:
            if list_files:
                for _file in self._fileList:
                    if _file != "." and _file != "..":
                        _list[:] += [self._dir_path + '/' + _file]

        if len(self._dirList) > 0:
            path = "/".join(self._dir_path.split("/"))
            _full_path_dirList = map(lambda x: path + '/' + x, self._dirList)
            for _dir in _full_path_dirList:
                if list_dir:
                    _list[:] += [_dir + '/']

                self.cd(_dir)
                _list[:] += self.__recursive_list(True, list_files, list_dir)

        else:
            if len(self._dirList) == 0:
                if recur == True and self._layer > 1:
                    for n in xrange(0, self._layer):
                        self._layer -= 1
                        self.cd('..')
                else:
                    self.cd('..')

        self._layer = 0
        return _list

    # Changes the directory to the give path.
    def cd(self, path):
        try:
            self.ftp.cwd(path)

            if path[0] == '/':
                self._dir_path = path

            elif '/' in path and not '..' in path:
                self._dir_path = self._dir_path + '/' + path


            elif '..' in path and len(self._dir_path) > 1:
                temp = self._dir_path.split('/')
                temp.pop()

                self._dir_path = '/'.join(temp)

                if len(self._dir_path) == 0:
                    self._dir_path = '/'

                if self._dir_path.index('/') != 0:
                    self._dir_path.insert(0, '/')

                if len(path[2:]) > 0:
                    if len(self._dir_path) > 0 and self._dir_path[len(self._dir_path) -1] != '/':
                        self._dir_path = self._dir_path + '/' + path[3:]
                    else:
                        self._dir_path += path[3:]
    
            elif self._dir_path == '/':
                self._dir_path += path
            else:
                self._dir_path = self._dir_path + '/' + path

            self._generate_list()
        except ftplib.error_perm:
            raise ftplib.error_perm('The path does not exist.')

    def current_dir(self, full=False):
        if full:
            return self._dir_path
        else:
            list = self._dir_path.split('/')
            if self._dir_path == '/':
                return self._dir_path
            elif len(list) > 1:
                return list[-1]

    # file is the filepath
    # path is the path to the directory you want to upload to
    def upload(self, file):
        try:
            self.ftp.storbinary('STOR '+file, open(file, 'rb'))
            self._generate_list()
        except IOError:
            raise IOError('File does not exist.')

    # Finally working. Allows the user to download a file through ftp.
    def download(self, file, local_file):
        with open(local_file, 'wb') as f:
            def callback(data):
                f.write(data)
            try:
                self.ftp.retrbinary('RETR '+ file, callback)
            except IOError:
                raise IOError('File does not exist.')

    # Retrives the contents of the remote file and returns its contents.
    def retrieve(self, file):
        class Capsule:
            __data = None
            
            def set(self, data):
                self.__data = data

            def get(self):
                return self.__data

        data_file = Capsule()
        try:
            self.ftp.retrbinary('RETR '+ file, data_file.set)
            return data_file.get()

        except IOError:
            raise IOError('File does not exist.')
    
    # Deletes file
    def rm(self, file):
        try:
            self.ftp.delete(file)
            self._generate_list()
        except ftplib.error_perm:
            raise ftplib.error_perm('File does not exist.')

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
            raise ftplib.error_perm('Directory does not exist.')
    
    #Call this function if you want to delete a directory that has other things inside it.
    def rmdir_all(self, dirname):
        if dirname in self._dirList:
            try:
                #Do this just in case there isn't anything in the directory.
                self.rmdir(dirname)
            except ftplib.error_perm:
                self.cd(dirname)
                self.__rmdir_recursion()
                self.rmdir(dirname)

    #Use this to recursively go through the child directories and delete the files/empty directories.
    def __rmdir_recursion(self):
        if len(self._fileList) > 0:
            for f in self._fileList:
                self.rm(f)
        if len(self._dirList) > 0:
            for x in self._dirList:
                self.cd(x)
                self.__rmdir_recursion()
                self.rmdir(x)
        if len(self._bothList) == 0:
            self.cd('..')
            
    # Creates a directory.
    def mkdir(self, dirname):
        self.ftp.mkd(dirname)
        self._generate_list()

    # Returns if there is a file in path.
    def file_exists(self, filename):

        for x in self._fileList:
            if x == filename:
                return True
        return False
        
    # Returns if there is a directory dirName in the current directory.
    def dir_exists(self, dirName):

        for x in self._dirList:
            if x == dirName:
                return True

        return False
        
    # Quits out of the ftp session. Call this function when you are done using the object.
    def quit(self):
        self.ftp.quit()
        
    # Forced close from the ftp session.
    def close(self):
        self.ftp.close()