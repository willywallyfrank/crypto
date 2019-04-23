#stream cipher using the ASCII symbols 32 - 126

import random
 
def readPtext():
    Pfile =input('enter file name containing plain text: ')
    PfileLoc = 'Pfile + '.txt'
    plainText = open (PfileLoc,"r")
    pText = plainText.read()
    plainText.close()
    return pText
 
def enterKey(n):
    print('Enter a key. You must retain this Key to decrypt your message. ')
    userkey = input(': ')
    keyList = []
    for c in userkey:
        keyList.append(ord(c))
    keyStrList = map(str, keyList)
    keyStr = ''.join(keyStrList)
    keyseed = int(keyStr)
    random.seed(keyseed)
    a = 10**(n-1)
    b = 10**n-1
    key = random.randint(a,b)
    return str(key)
 
def cleanText(text):
    cleanText = []
    for c in text:
        if (ord(c) > 31) and (ord(c) < 127):
            cleanText.append(c)
    return cleanText
            
def encryptPtext(pText,key):
    pTextVals = []    
    trans_pvals = []    
    for c in pText:
        pnum = ord(c)
        pTextVals.append(pnum - 32)
    lenText = len(pTextVals)
    for c in range(lenText):
        keynum = int(key[c])
        random.seed(keynum)
        keyval = random.randint(0,94)
        enum = (keyval+pTextVals[c])%95
        trans_pvals.append(enum) 
    ctextList =  [chr(c + 32) for c in trans_pvals]
    cText =  ''.join(ctextList)
    return cText

def writeCtext(cText):
    Cfile =input('enter file name to contain cipher text: ')
    CfileLoc = 'Cfile + '.txt'
    cipherText = open (CfileLoc,"w")
    cipherText.write(cText)
    cipherText.close()

def encryption():
    pText = readPtext()
    cleantext = cleanText(pText)
    key_len = len(cleantext)
    key = enterKey(key_len)
    cText = encryptPtext(cleantext,key)
    writeCtext(cText)

def readCtext():
    Cfile =input('enter file name containing cipher text: ')
    CfileLoc = 'Cfile + '.txt'
    cipherText = open (CfileLoc,"r")
    cText = cipherText.read()
    cipherText.close()
    return cText

def decryptCtext(cText,key):
    trans_dvals = []
    cTextVals = [ord(c)-32 for c in cText]    
    lencText = len(cText)   
    for c in range(lencText):
        keynum = int(key[c])
        random.seed(keynum)
        keyval = random.randint(0,94)
        dnum = (cTextVals[c]-keyval)%95
        trans_dvals.append(dnum) 
    dtextList =  [chr(c + 32) for c in trans_dvals]
    dText =  ''.join(dtextList)
    return dText

def writedtext(dText):
    dfile =input('enter file name to contain decrypted text: ')
    dfileLoc = 'dfile + '.txt'
    decryptedText = open (dfileLoc,"w")
    decryptedText.write(dText)
    decryptedText.close()
    
def decryption():
    cText = readCtext()
    cleantext = cleanText(cText)
    key = enterKey(len(cleantext))
    dText = decryptCtext(cleantext,key)
    writedtext(dText)    

def main():
    print('enter e: for encrytion or d: for decrytion')
    choice = input('? ')
    if choice == 'e':
        encryption()
    if choice == 'd':
        decryption()
    if (choice != 'e') and (choice != 'd'):
        print('invalid choice')
        

    
main()

