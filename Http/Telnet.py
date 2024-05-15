import telnetlib

if __name__ == '__main__':
    tnet = telnetlib.Telnet('telehack.com')
    info = tnet.read_until(b'\r\n.').decode()
    print(info)

    tnet.write(b'cal\r\n')


    info = tnet.read_until(b'\r\n.').decode()
    print(info)

    info = tnet.read_until(b'\r\n.').decode()
    print(info)
