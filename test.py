def server_config():
    HOST = "192.168.1.36"
    PORT = 3000
    return HOST,PORT
def split(a,b):
    sep = ' '
    if b==1 :
      uname = a.split(sep, 1)[0]
      return uname
    elif b==2 :
        sep = ' '
        addr1 = format(a)
        e = ""
        addr2 = addr1.split(sep, 1)[0]
        addr2 = addr2.replace('(', '')
        addr2 = addr2.replace(',', '')
        return addr2
