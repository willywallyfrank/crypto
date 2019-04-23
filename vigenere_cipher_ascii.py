#vignere cipher using the ASCII symbols 32 - 126
 
def readPtext():
    Pfile =input('enter file name containing plain text: ')
    PfileLoc = 'Pfile + '.txt'
    plainText = open (PfileLoc,"r")
    pText = plainText.read()
    plainText.close()
    return pText
 
def enterKey():
    print('Enter a key. You must retain this Key to decrypt your message. ')
    key = input(': ')
    return key
 
def encryptPtext(pText,key):   
    pTextVals = []
    keyVals = []
    trans_pvals = []
    
    
    for c in pText:
        pnum = ord(c)
        if (pnum > 31) and  (pnum < 127):
            pTextVals.append(pnum - 32)
    for c in key:
        knum = ord(c)
        if (knum > 31) and (knum < 127):
            keyVals.append(knum - 32)
    lenText = len(pTextVals)
    lenKey = len(keyVals)
    for c in range(lenText):
        enum = (keyVals[c%lenKey]+pTextVals[c])%95
        trans_pvals.append(enum) 
    ctextList =  [chr(c + 32) for c in trans_pvals]
    cvals = [ord(c) for c in ctextList]
    cText =  ''.join(ctextList)
    pvals = [ord(c) for c in pText]
    return cText

def writeCtext(cText):
    Cfile =input('enter file name to contain cipher text: ')
    CfileLoc = 'Cfile + '.txt'
    cipherText = open (CfileLoc,"w")
    cipherText.write(cText)
    cipherText.close()

def encryption():
    pText = readPtext()
    key = enterKey()
    cText = encryptPtext(pText,key)
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
    ckeyVals = [ord(c)-32 for c in key]
    lenText = len(cText)
    lenKey = len(key)
    for c in range(lenText):
        dnum = (cTextVals[c]-ckeyVals[c%lenKey])%95
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
    key = enterKey()
    dText = decryptCtext(cText,key)
    writedtext(dText)    

def main():
    print('enter e: for encrytion or d: for decrytion')
    choice = raw_input('? ')
    if choice == 'e':
        encryption()
    if choice == 'd':
        decryption()
    if (choice != 'e') and (choice != 'd'):
        print('invalid choice')
        

    
main()

