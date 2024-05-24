import ftplib

FTP_HOST = "10.1.142.5"
FTP_USER = "odstrob@outlook.com"
FTP_PASS = "Fresnillo"

def listCallback(line):
    print(line)


try:
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    ftp.encoding = "utf-8"
    welcomeMessage = ftp.getwelcome()
    print(welcomeMessage)

    fichero_enServidor = "subido.txt"
    fichero_local = "bajado.txt"
    with open(fichero_local, "wb") as file:
        ftp.retrbinary(f"RETRR {fichero_enServidor}", file.write)

    ftp.quit()
except ftplib.all_errors as e:
    errorcode_string = str(e).split(None, 1)[0]












