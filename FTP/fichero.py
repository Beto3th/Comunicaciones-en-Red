import ftplib

FTP_HOST = "10.1.142.5"
FTP_USER = "odstrob@outlook.com"
FTP_PASS = "Fresnillo"

def listCallback(line):
    print(line)

ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
ftp.encoding = "utf-8"
welcomeMessage = ftp.getwelcome()
print(welcomeMessage)

respMessage = ftp.retrlines("LIST", listCallback)
print("----------------------------")
print(respMessage)

ftp.quit()

