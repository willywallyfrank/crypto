'''
cipher modual
'''
class Reverse():
        
    def encrypt(self,message):
        self.pText = message
        reverse = ''
        i = len(message) - 1
        while i >= 0:
            reverse = reverse + message[i]
            i = i -1
        self.cText = reverse
        return reverse               

    def decrypt(self,cText):
        message = self.encrypt(cText)
        return message

        

class Caesar():
        
    def encrypt(self,pText,key):
    
        pTextVal = []
        for c in pText:
            num = ord(c)
            if (num > 31) and  (num < 127):
                pTextVal.append(num - 32)
        trans_pvals = [(x + key)%95 for x in pTextVal]
        ctextList =  [chr(c + 32) for c in trans_pvals]
        cText =  ''.join(ctextList)
        return cText

    def decrypt(self,cText,key):
        
        cTextVal = [ord(c)-32 for c in cText]
        trans_cvals = [(x - key)%95 for x in cTextVal]
        ptextList =  [chr(c+32) for c in trans_cvals]
        pText =  ''.join(ptextList)
        return pText 
        
        
class Transposition():
    
    def encrypt(self,pText,key):
        
        cText = [''] * key
        for col in range(key):
            position = col
            while position < len(pText):
                cText[col] = cText[col] + pText[position]
                position = position + key
        return ''.join(cText) 

    def decrypt(self,cText,key):
        dText = [''] * (len(cText)//key+1)
        position = 0
        for col in range(key):
            row = 0
            val = col
            while val < len(cText):
                dText[row] = dText[row] + cText[position]
                position = position + 1
                row = row + 1
                val = val + key
        return ''.join(dText)


if __name__ == "__main__":    
    function = int(input('enter 0 for encrypt or 1 for decrypt: '))
    if not function:
        Pfile = input('enter file name containing plain text: ')
        key = int(input('enter key: ' ))
        PfileLoc = Pfile + '.txt'
        plainText = open (PfileLoc,"r")
        pText = plainText.read()
        plainText.close()
        c = Transposition()
        cText = c.encrypt(pText,key)
        Cfile =input('enter file name to contain cipher text: ')
        CfileLoc = Cfile + '.txt'
        cipherText = open (CfileLoc,"w")
        cipherText.write(cText)
        cipherText.close()
    if function:
        Cfile = input('enter file name containing cipher text: ')
        key = int(input('enter key: '))
        CfileLoc = Cfile + '.txt'
        cipherText = open (CfileLoc,"r")
        cText =cipherText.read()
        cipherText.close()
        c = Transposition()
        dText = c.decrypt(cText,key)
        Dfile =input('enter file name to contain decrypted text: ')
        DfileLoc = Dfile + '.txt'
        decipherText = open (DfileLoc,"w")
        decipherText.write(dText)
        decipherText.close()        



















        
