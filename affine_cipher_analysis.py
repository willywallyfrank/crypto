#a plain text file is expected in 'C:/Users/William/Desktop/Encrypt' folder. It will output cipher text and decrytp text to the same folder.

symSet = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
          'r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
           'S','T','U','V','W','X','Y','Z',' ',',','<','.','>','/','?','"','!','@','#','$','$','%','^','*','(',')',
           '-','_','+','=','[',']','{','}','|','\',',':',';','`','~','&','\\',"'"]

def inputKeyParameters():
    print('affine key: C = (a + bP)mod97')
    a = int(input('enter a: '))
    b = int(input('enter b: '))
    return a,b

def readPtext():
    Pfile = input('enter file name containing plain text: ')
    PfileLoc = 'C:/Users/William/Desktop/Encrypt/' + Pfile + '.txt'
    plainText = open (PfileLoc,"r")
    pText = plainText.read()
    plainText.close()
    return pText


def encryptPtext(a,b,pText):   
    pTextVal = []
    for c in pText:
        if c in symSet:
            pTextVal.append(symSet.index(c))
    trans_pvals = [(a + b*x)%97 for x in pTextVal]
    ctextList =  [symSet[c] for c in trans_pvals]
    cText =  ''.join(ctextList)
    return cText

def writeCtext(cText):
    Cfile = input('enter file name to contain cipher text: ')
    CfileLoc = 'C:/Users/William/Desktop/Encrypt/' + Cfile + '.txt'
    cipherText = open (CfileLoc,"w")
    cipherText.write(cText)
    cipherText.close()

def readCtext():
    Cfile = input('enter file name containing cipher text: ')
    CfileLoc = 'C:/Users/William/Desktop/Encrypt/' + Cfile + '.txt'
    cipherText = open (CfileLoc,"r")
    cText = cipherText.read()
    cipherText.close()
    return cText

def decryptCtext(a,b,cText):
    cTextVal = [symSet.index(c) for c in cText]
    bInv = b**95%97
    trans_cvals = [((x - a)*bInv)%97 for x in cTextVal]
    ptextList =  [symSet[c] for c in trans_cvals]
    pText =  ''.join(ptextList)
    return pText

def writedtext(dText):
    dfile = input('enter file name to contain decrypted text: ')
    dfileLoc = 'C:/Users/William/Desktop/Encrypt/' + dfile + '.txt'
    decryptedText = open (dfileLoc,"w")
    decryptedText.write(dText)
    decryptedText.close()
    
def ctextanalyze(cText):
    sym = []
    symfreq = []
    for c in cText:
        if (c in symSet) and (c not in sym):
            sym.append(c)
            symfreq.append(cText.count(c))     
    return sym,symfreq
                
def encryption():
    a,b = inputKeyParameters()
    pText = readPtext()
    cText = encryptPtext(a,b,pText)
    writeCtext(cText)  

def decryption():
    a,b = inputKeyParameters()
    cText = readCtext()
    dText = decryptCtext(a,b,cText)
    writedtext(dText) 

def ctextanalysis():
    cText = readCtext()
    s,f = ctextanalyze(cText)
    for i in range(len(s)):
        print(s[i]),
        print(f[i])
                    
    
def main():
    print(len(symSet))
    print('enter e for encrytion or d for decrytion or a for analyze')
    choice = input('? ')
    if choice == 'e':
        encryption()
    if choice == 'd':
        decryption()
    if choice == 'a':
        ctextanalysis()                                          
    if (choice != 'e') and (choice != 'd') and (choice != 'a'):
        print('invalid choice')
    
main()


    

        
    
    

    
