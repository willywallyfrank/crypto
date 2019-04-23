#RSA Module

#   THIS PROGRAM WILL DO THE FOLLOWING:
#0: create a Public and Private Key set and write to files for each
#1: create a Public Keys File from individual public key files
#2: encrypt a password using a public key
#3: decrypt an encrypted password using private key
# all files are read and writed to the local directory with relative addresses

import math 
import random

def findPrime(digits):
    a = 10**(digits - 1)
    b = 10**digits - 1
    number = random.randint(a,b)
    if number%2 == 0:
        number = number + 1
    while not isPrime(number):        
        number = number + 2       
    return number

def isPrime(number):
    root = int(math.sqrt(number))
    c = 2
    while c <= root:
        if number%c == 0:
            return False
        c = c + 1
    return True

def inputkey():
    Dp = input('enter the number of digits for the prime number p: ')
    Dq = input('enter the number of digits for the prime number q: ')
    DE = input('enter the number of digits for the prime number E: ')
    return Dp,Dq,DE

def phi(n):
    phi_n = 1
    basevals,expList = primeFactors(n)
    length = len(basevals)
    for c in range(length):
        phi_n = phi_n * basevals[c]**(expList[c] - 1 )*(basevals[c] - 1 )
    return phi_n    
    
def keys(p,q,E):
    N = p*q
    M = (p-1)*(q-1)
    phi_p = phi(p-1)
    phi_q = phi(q-1)
    phin = phi_p * phi_q
    D = pow(E,phin-1,M)
    return D,N

def primeFactors(n):
    primeFactorList = []
    k = 2
    while k <= n/2 + 1:       
        factor = True
        while factor:
            if n%k == 0:
                primeFactorList.append(k)
                factor = True
                n = n/k
            else:
                factor = False
        k = k + 1
    primeFactorList.append(n)
    pfactors = set(primeFactorList)
    expList = []
    basevals = []
    for c in pfactors:
        exp = primeFactorList.count(c)
        basevals.append(c)
        expList.append(exp)
    return basevals,expList

def createKeys():
    userName = raw_input('enter the user name who will use the keys: ')
    Dp,Dq,DE = inputkey()
    p = findPrime(Dp)
    print('p = ' + str(p))
    q = findPrime(Dq)
    print('q = ' + str(q))
    E = findPrime(DE)
    print('E = ' + str(E))
    D,N = keys(p,q,E)
    print('privite key: D: ' + str(D))
    print('Public Keys: N: ') + str(N) + ' E: ' +str(E)
    keyfile = open('PublicKey' + userName + '.txt','w')
    text =  userName + ' ' + str(N) + ' ' + str(E)
    keyfile.write(text)
    keyfile.close()
    pkeyfile = open('PrivateKey' + userName + '.txt','w')
    ptext = str(N) + ' ' + str(D)
    pkeyfile.write(ptext)
    pkeyfile.close()
    return 
    
def blockSize(n):
    if n < 95:
        return 0
    blocksize = 0
    block = ''
    blockval = 0
    while blockval < n:
        block = block + '95'
        blocksize = blocksize + 1
        blockval = int(block)
    return blocksize - 1

def padSize(password,n):
    p = len(password)
    b = blockSize(n)
    padsize = (b - p%b)%b
    return padsize

def WriteKeys():
    f = open('PublicKeys.txt','w')
    numKeys = input('Enter the number of key files to be read: ')
    for k in range(numKeys):
        keyfile =raw_input('enter file ' + str(k+1) + ' name containing key: ')
        keyText = open (keyfile + '.txt',"r")
        kText = keyText.read()
        if not kText.endswith("\n"):
            kText = kText + "\n"
        keyText.close()        
        f.write(kText) 
    f.close()
    
def ReadKeys():
    keyfile = open('PublicKeys.txt','r')
    keydata = keyfile.readlines()
    keyfile.close()
    if '\n' in keydata:
        keydata.remove('\n')
    num = len(keydata)
    keydict = {}
    for n in range(num):
        items = keydata[n].split()
        name = items[0]
        nkey = int(items[1])
        ekey = int(items[2])
        if ekey > nkey:
            temp = nkey
            nkey = ekey
            ekey = temp
        keydict[name] = (nkey,ekey)
    return keydict

def inputPassword():
    password = raw_input('enter your passord using at least 4 charecters: ')
    return password

def getKey():
    name = raw_input('enter the name of the person whose key you wish: ')
    keyDict = ReadKeys()
    keys = keyDict[name] 
    Nkey = keys[0]
    Ekey = keys[1] 
    return int(Nkey),int(Ekey)

def encryptPassword():
    N,E = getKey()
    password = inputPassword()
    blocksize = blockSize(N)
    padsize = padSize(password,N)
    pblocks = []
    cblocks = []
    numText = ''
    for L in password:
        num = ord(L)
        if (num > 31) and  (num < 127):
            p = num - 32
            if p < 10:
                pString = '0' + str(p)
            else:
                pString = str(p)
            numText = numText + pString
    for c in range(padsize):
        numText = numText + '96'
    digits = len(numText)
    pblocks = [numText[i:i+2*blocksize] for i in range(0, digits, 2*blocksize)]
    for p in pblocks:
        c = pow(int(p),E,N)
        cblocks.append(str(c))
    cblocksvals = " ".join(cblocks)
    fileName = raw_input('enter the name of the file tha will contain the encrypted password: ')
    cfile = open(fileName + '.txt','w')
    cfile.write(cblocksvals)
    cfile.close()    
    return pblocks,cblocks       

def decryptPassword():
    pkeyfile = open('PrivateKeyWilliam.txt','r')
    pkeytext = pkeyfile.read()
    keylist = pkeytext.split()
    vals = []
    N = int(keylist[0])
    D = int(keylist[1])
    dfilename = raw_input('enter file name containing encrypted password: ')
    dfile = open(dfilename + '.txt','r')
    dtext = dfile.read()
    dlist = dtext.split()
    for c in dlist:
        vals.append(str(pow(int(c),D,N)))
    blocksize = blockSize(N)
    dStr = ''.join(vals)
    num = len(dStr)
    pblocks = [dStr[i:i+2] for i in range(0, num, 2)]
    password = ''
    for c in pblocks:
        if int(c) < 96:
            password = password + chr(int(c)+32)
    print password  

def menu():
    repeat = True
    while repeat:
        print
        print('                MENU                                ')
        print('for creating a single set of Public/Private Keys:---------c')
        print('for writing to file a complete set of Users Public Keys:--w')
        print('for displaying the complete set of public keys:-----------r')
        print('for displaying a single public key:-----------------------k')
        print('for encrypting a password:--------------------------------e')
        print('for decrypting a password:--------------------------------d')
        print('for exit:-------------------------------------------------x')
        choice = raw_input(': ')
        if choice == 'c':
            createKeys()
        if choice == 'w':
            WriteKeys()
        if choice == 'r':
            print('Name (N,E)')
            Keys = ReadKeys()
            for k in Keys:
                print(k),
                print(Keys[k])
        if choice == 'k':
            print(getKey())
        if choice == 'e':
            p,c = encryptPassword()
            print
            print('unencrypted: '),
            print(p)
            print('  encrypted: '),
            print(c)
        if choice == 'd':
            decryptPassword()
        if choice == 'x':
            break
    
menu()


    
