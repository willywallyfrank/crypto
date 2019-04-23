#AFFINE CIPHER using the ASCII symbols 32 - 126
 
def readPtext():
    Pfile =input('enter file name containing plain text: ')
    PfileLoc = 'Pfile + '.txt'
    plainText = open (PfileLoc,"r")
    pText = plainText.read()
    plainText.close()
    return pText
 
def enterKey():
    print('Given C = a + bP Mod95 where (b,95) = 1 ')
    a = input('enter a: ')
    b = input('enter b: ')
    if b%5 == 0 or b%19 ==0:        
        bad_b_val = True
    else:       
        bad_b_val = False 
    while bad_b_val:
        print('b must be relatively prime to 95')
        b = input('enter b: ')
        if b%5 == 0 or b%19 ==0:
            bad_b_val = True
        else:
            bad_b_val = False
    return a,b
 
def encryptPtext(pText,a,b):   
    pTextVal = []
    for c in pText:
        num = ord(c)
        if (num > 31) and  (num < 127):
            pTextVal.append(num - 32)
    trans_pvals = [(a + b*x)%95 for x in pTextVal]
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
    a,b = enterKey()
    cText = encryptPtext(pText,a,b)
    writeCtext(cText)

def readCtext():
    Cfile =input('enter file name containing cipher text: ')
    CfileLoc = 'Cfile + '.txt'
    cipherText = open (CfileLoc,"r")
    cText = cipherText.read()
    cipherText.close()
    return cText

def decryptCtext(cText,a,b):
    cTextVal = [ord(c)-32 for c in cText]
    b_inv = b**17%95
    trans_cvals = [b_inv*(x - a)%95 for x in cTextVal]
    ptextList =  [chr(c + 32) for c in trans_cvals]
    pText =  ''.join(ptextList)
    return pText

def writedtext(dText):
    dfile =input('enter file name to contain decrypted text: ')
    dfileLoc = 'dfile + '.txt'
    decryptedText = open (dfileLoc,"w")
    decryptedText.write(dText)
    decryptedText.close()
    
def decryption():
    cText = readCtext()
    a,b = enterKey()
    dText = decryptCtext(cText,a,b)
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

