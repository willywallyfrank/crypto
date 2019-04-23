'''
Ceasar Shift Cipher
'''
from tkinter import filedialog
from tkinter import *
from tkinter.filedialog import askopenfilename



def menu():
    print('''
          Menu
          1. Encrypt Text
          2. Decrypt Text
          3. Quit
         ''')
    choice = input('Choice #: ')
    return choice

def open_file(string):
    Cfile = input('enter file name' + string)
    filename = Cfile + '.txt'
    return filename

def save_file(file,string):
    Cfile = input('enter file name' + string)
    filename = Cfile + '.txt'
    text_file = open (filename,"w")
    text_file.write(file)
    text_file.close()


def read_file(filename):
    plainText = open (filename,"r")
    pText = plainText.read()
    plainText.close()
    return pText


def encrypt(pText):
    print('''
          Enter shift value (key):
          ''')
    key = int(input(': '))
    pTextVal = []
    for c in pText:
        num = ord(c)
        if (num > 31) and  (num < 127):
            pTextVal.append(num - 32)
    trans_pvals = [(x + key)%95 for x in pTextVal]
    ctextList =  [chr(c + 32) for c in trans_pvals]

    cText =  ''.join(ctextList)

    return cText
    

def decrypt(cText):
    print('''
          Enter shift value (key):
          ''')
    key = int(input(': '))
    cTextVal = [ord(c)-32 for c in cText]
    trans_cvals = [(x - key)%95 for x in cTextVal]
    ptextList =  [chr(c+32) for c in trans_cvals]
    pText =  ''.join(ptextList)
    return pText    
    
    
if __name__ == "__main__":
    repeat = True
    while repeat:
        choice = int(menu())
        if choice == 3:
            repeat = False
        if choice == 1:
            filename = open_file(' of plain text: ')
            pText = read_file(filename)
            cText = encrypt(pText)
            save_file(cText,' of encrypted text to be saved: ')
        if choice == 2:
            filename = open_file(' of cipher text: ')
            cText = read_file(filename)
            pText = decrypt(cText)
            save_file(pText,' of decrypted text to be saved: ')


