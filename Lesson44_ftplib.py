from ftplib import FTP
# in order for this code to work you will have to fill in your credentials
ftp = FTP('DomainName.com')
ftp.login(user='username', passwd='password')
ftp.cwd('/specific_domain/') # depends on the site you connect to
# downloading a file:
def grabFile():
    filename = 'filename.extention'
    localfile = open(filename, 'wb') # write binary
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024) # buffer size is 1024
    ftp.quit() # closing the connection
    localfile.close() # closing the file
# uploading files to the ftp server
def placeFile():
    filename = 'fileName.extention'
    ftp.storbinary('STOR ' + filename, open(filename, 'rb')) # read binary