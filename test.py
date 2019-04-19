def server_config(a=0):
    HOST = "192.168.1.33"     #Server configurations
    PORT = 3000
    if a == 1:
     return HOST
    else:
     return HOST,PORT

def split(a,b):
    sep = ' '
    if b==1 :                        #code to split username
      uname = a.split(sep, 1)[0]
      return uname
    elif b==2 :
        sep = ' '
        addr1 = format(a)               #code to split ip address
        e = ""
        addr2 = addr1.split(sep, 1)[0]
        addr2 = addr2.replace('(', '')
        addr2 = addr2.replace(',', '')
        return addr2
