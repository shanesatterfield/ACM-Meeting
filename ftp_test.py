import ftplib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--upload", "-up", help="ftp's the file")
args = parser.parse_args()

ftp = ftplib.FTP('')            #Enter the host name
ftp.login(user='',passwd='')    #Enter the Credentials

ftp.cwd('')   #cd to the directory that you want to place the file
fname = args.upload

ftp.storbinary('STOR '+fname, open(fname, 'rb'))
ftp.quit()
