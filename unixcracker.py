import hashlib
 
def testPass(passwd):
    dictFile = open('dictionary.txt', 'r')
    semi_c = ':'
    d_sign = '$'
    pwdlist = passwd.split("$")
    salt ='$'+pwdlist[1]+'$'+pwdlist[2]
    cryptPas = passwd.split(d_sign, 3)[3]
    cryptPass = cryptPas.split(semi_c)[0]
    for word in dictFile:
        cryptWord = hashlib.sha512(salt.encode() + word.encode()).hexdigest() + ':' + salt
        print cryptWord
        if (cryptWord == cryptPass):
            print '[+] Found Password : ' + word + '\n'
            return
    print '[-] Password not found.\n'
    return
 
def main():
    passfile = open('password.txt')
    passwd = passfile.readline()
    semi_c = ':'
    print passwd
    if semi_c in passwd:
            user = passwd.split(semi_c)[0]
            print '[*] Cracking Password for : ' + user
            testPass(passwd)

if __name__ == '__main__':
        main() 
        
