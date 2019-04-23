#Block_Cipher Module

# This program will input plaintext and a key. It will convert these to ascii values converted to binary.
#It will then divide the binary values into blocks of binary digits for both the message and key
#Following a scrambling algorythm the encrypted text is writen to file. The decryption proceedure reverses
#the above functions


import random

block_size = 56
key_size = 1.5*block_size


def enterKey():       #user input: string key   --->  output string key
    print('Enter a Key: ')
    keyText  = input(':')
    keyNum = ''
    for c in keyText:
        keyNum = keyNum + str(ord(c))
    random.seed(int(keyNum))
    a = 2**(key_size - 1)
    b = (2**key_size - 1)
    keyInt = random.randint(a,b)
    key = str(keyInt)
    return key

def binary(num):      #input: integer  --->  output: 7 bit binary number string
    if (num == 0): 
        result = "0000000" 
    else: 
        quotient = num 
        result = "" 
        while quotient > 0: 
            remainder = quotient % 2 
            result = str(remainder) + result 
            quotient = quotient / 2       
    L = len(result)
    if L < 7:
        for c in range(7-L):
            result = '0' + result
    return result   

def readText(typetext):      #read:text file ---> output:message string
    if typetext == 'plain':        
        tfile =input('enter file name containg plain text: ')
    if typetext == 'cipher':
        tfile =input('enter file name containg cipher text: ')
    #tfileLoc = 'C:/Python27/my_programs/' + tfile + '.txt'
    textFile = open (tfile + '.txt',"r")
    tText = textFile.read()
    textFile.close()
    return tText

def writeText(text,typetext):
    if typetext == 'plain':        
        tfile = input('enter file name to contain plain text: ')
    if typetext == 'cipher':
        tfile = input('enter file name to contain cipher text: ')
    if typetext == 'decrypt':
        tfile = input('enter file name to contain decrypted text: ')
    #tfileLoc = 'C:/Python27/my_programs/' + tfile + '.txt'
    tText = open (tfile + '.txt',"w")
    tText.write(text)
    tText.close()


def cleanText(text):  #input: message string ---> output:clean message string
    cleantext = ''
    for c in text:
        if (ord(c) > 31) and (ord(c) < 127):
            cleantext = cleantext + c
    return cleantext

def binaryConvert(string):   #input: integer string  --->  output: large string made with many 7 bit binary strings
    binaryString = ''
    for c in string:
        num = ord(c) - 32
        binum = binary(num)
        binaryString = binaryString + str(binum)
    return binaryString

def xor(a,b):
    axorb = ''
    for c in range(len(a)):
        val = int(a[c])+int(b[c])-2*int(a[c])*int(b[c])
        axorb = axorb + str(val)
    return axorb
  
def addPads(TextbinaryString):
    bintextsize = len(TextbinaryString)
    pads = block_size - bintextsize%block_size
    for c in range(pads):
        padval_rear = random.randint(0,1)
        TextbinaryString = TextbinaryString + str(padval_rear)
    for d in range(block_size - 7):
        padval_front = random.randint(0,1)
        TextbinaryString =  str(padval_front) + TextbinaryString
    pads_bin = binary(pads)
    TextbinaryString = pads_bin + TextbinaryString
    return TextbinaryString
      
def blockText(paddedBinaryText):
    blockList = []
    for c in range(len(paddedBinaryText)/block_size):
        block = ''
        for d in range(block_size):
            block = block + paddedBinaryText[c*block_size + d]
        blockList.append(block)
    return(blockList)

def divideKey(key):
    K1 = ''
    K2 = ''
    K3 = ''
    subKeySize = int(key_size/3)
    for c in range(subKeySize):
        K1 = K1 + key[c]
        K2 = K2 + key[subKeySize + c]
        K3 = K3 + key[2*subKeySize + c]
    return K1,K2,K3

def splitBlock(block):
    blockL = ''
    blockR = ''
    subBlockSize = (block_size/2)
    for c in range(subBlockSize):
        blockL = blockL + block[c]
        blockR = blockR + block[subBlockSize + c]
    return blockL,blockR
    
def encrypt(blockList,KeybinaryString):
    encryptedBlock = ''
    K1,K2,K3 = divideKey(KeybinaryString)
    n = len(blockList)
    for c in range(n):
        block = blockList[c]
        L1,R1 = splitBlock(block)
        L2 = R1
        R2 = xor(L1,xor(K1,R1))
        L3 = R2
        R3 = xor(L2,xor(K2,R2))
        L4 = R3
        R4 = xor(L3,xor(K3,R3))
        L5 = R4
        R5 = L4
        encryptedBlock = encryptedBlock + L5 + R5
    return encryptedBlock

def decrypt(ctext,KeybinaryString):
    numCipherBlocks = len(ctext)/block_size
    cipherBlockList = []
    for c in range(numCipherBlocks):
        block = ''
        for d in range(block_size):
            block = block + ctext[c*block_size + d]
        cipherBlockList.append(block)
    K1,K2,K3 = divideKey(KeybinaryString)
    decryptedBlock = ''
    for c in range(numCipherBlocks):
        block = cipherBlockList[c]
        L1,R1 = splitBlock(block)
        L2 = R1
        R2 = xor(L1,xor(K3,R1))
        L3 = R2
        R3 = xor(L2,xor(K2,R2))
        L4 = R3
        R4 = xor(L3,xor(K1,R3))
        L5 = R4
        R5 = L4
        decryptedBlock = decryptedBlock + L5 + R5
    return decryptedBlock

def decConvert(binaryValtext):
    decVal = 0
    numDigits = len(binaryValtext)
    for c in range(numDigits):
        decVal = decVal + int(binaryValtext[c])*2**(numDigits - c - 1)
    return decVal
    
def stripPad(tText):
    textLength = len(tText)
    numPads = ''
    stripText = ''
    restoText = []
    for c in range(7):
        numPads = numPads + tText[c]
    numPadsDec = decConvert(numPads)
    for d in range(block_size,textLength - numPadsDec):
        stripText = stripText + tText[d]
    binNums = [stripText[k:k+7] for k in xrange(0, len(stripText), 7)]
    for c in binNums:
        num = decConvert(c) + 32
        restoText.append(chr(num))
        decryptedText = ''.join(restoText)
    return decryptedText
    

def main():
    decide = input('enter "e" for encrytion or "d" for decryttion: ')
    if decide =='e':        
        ptext = readText('plain')
        cleantext = cleanText(ptext)
        TextbinaryString = binaryConvert(cleantext)
        padded_text = addPads(TextbinaryString)
        blockList = blockText(padded_text)
        keyDec = enterKey()
        KeybinaryString = binary(int(keyDec))
        EBString = encrypt(blockList,KeybinaryString)
        writeText(EBString,'cipher')
    if decide == 'd':
        ctext = readText('cipher')
        keyDec = enterKey()
        KeybinaryString = binary(int(keyDec))
        DBString = decrypt(ctext,KeybinaryString)
        decryptedText = stripPad(DBString)
        writeText(decryptedText,'plain')
           
main()


        
        
