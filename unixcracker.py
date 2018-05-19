import hashlib

def testPass(passwd):
    semi_c = ':'
    d_sign = '$'
    pwdlist = passwd.split("$")
    salt = '$'+pwdlist[1]+'$'+pwdlist[2]+'$'
    print 'Salt is : ' + salt
    #cryptPas = passwd.split(d_sign, 3)[3]
    #cryptPass = cryptPas.split(semi_c)[0] 
    dictFile = open('dictionary.txt', 'r')

    for word in dictFile.readlines():

        word = word.strip('\n')
        word2 = salt + word 
        print word2
        print 'Comparing to pass in list : ' + word + ' to ' + passwd + ' ---- '
        cryptWord = hashlib.sha512(salt + word2).hexdigest()
        print 'Reproduced Hash : ' + cryptWord
        if (cryptWord == passwd):
            print '[+] Found Password : ' + word + '\n'
            return cryptWord
        print '[-] Password not found.\n'
        return
 
def main():
    passfile = open('password.txt')
    passwd = passfile.readline()
    semi_c = ':'
    #print passwd
    if semi_c in passwd:
            user = passwd.split(semi_c)[0]
            print '[*] Cracking Password for : ' + user
            testPass(passwd)

if __name__ == '__main__':
        main() 
        
