import crypt
 
def testPass(cryptpass):
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile:
        cryptWord = hashlib.sha512(salt.encode() + word.encode()).hexdigest() + ': ' + salt
        if (cryptWord == cryptPass):
            print '[+] Found Password : ' + word + '\n'
            return
    print '[-] Password not found.\n'
    return
 
def main():
    passfile = open('password.txt')
    passwd = passfile.readline()
    semi_c = ':'
    d_sign = '$'
    print passwd
    if semi_c in passwd:
            user = passwd.split(semi_c)[0]
            salt = 
            cryptPass = 
            print '[*] Cracking Password for : ' + user
            testPass(cryptPass)

if __name__ == '__main__':
        main() 
        
