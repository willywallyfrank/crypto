'''
cipher modual
'''
import random

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

class Affine():
    # key = (a,b) gcd(b,95) must = 1
    
    def encrypt(self,pText,key):
        a = key[0]
        b = key[1]
        pTextVal = []
        for c in pText:
            num = ord(c)
            if (num > 31) and  (num < 127):
                pTextVal.append(num - 32)
        trans_pvals = [(a + b*x)%95 for x in pTextVal]
        ctextList =  [chr(c + 32) for c in trans_pvals]
        cvals = [ord(c) for c in ctextList]
        cText =  ''.join(ctextList)
        return cText

    def decrypt(self,cText,key):
        a = key[0]
        b = key[1]
        cTextVal = [ord(c)-32 for c in cText]
        b_inv = (b**71)%95
        print('b:',b,'   inv of b: ',b_inv)
        trans_cvals = [b_inv*(x - a)%95 for x in cTextVal]
        ptextList =  [chr(c + 32) for c in trans_cvals]
        pText =  ''.join(ptextList)
        return pText
        

class Vigenere():
    
    def encrypt(self,pText,key):   
        pTextVals = []
        keyVals = []
        trans_pvals = []
    
    
        for c in pText:
            pnum = ord(c)
        
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

    def decrypt(self,cText,key):
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

    

class Stream():
    
    def encrypt(self,ptext,userkey):
        pText = self.cleanText(ptext)
        key_len = len(pText)
        key = self.enterKey(key_len,userkey)
        pTextVals = []    
        trans_pvals = []    
        for c in pText:         
            pnum = ord(c)
            if (pnum > 31) and  (pnum < 127):
                pTextVals.append(pnum - 32)
        lenText = len(pTextVals)
        
        for c in range(lenText):
            keynum = int(key[c])
#            random.seed(keynum)
#            keyval = random.randint(0,94)
            enum = (keynum+pTextVals[c])%95
            trans_pvals.append(enum) 
        ctextList =  [chr(c + 32) for c in trans_pvals]
        cText =  ''.join(ctextList)
        return cText

    def decrypt(self,ctext,userkey):
        cText = self.cleanText(ctext)
        key_len = len(cText)
        key = self.enterKey(key_len,userkey)
        trans_dvals = []
        cTextVals = [ord(c)-32 for c in cText]    
        lencText = len(cText)
        for c in range(lencText):
            keynum = int(key[c])
#            random.seed(keynum)
#            keyval = random.randint(0,94)
            dnum = (cTextVals[c]-keynum)%95
            trans_dvals.append(dnum) 
        dtextList =  [chr(c + 32) for c in trans_dvals]
        dText =  ''.join(dtextList)
        return dText

    def enterKey(self,n,userkey):
        keyStrList = [str(ord(c)) for c in userkey]
        keyStr = ''.join(keyStrList)
        keyseed = int(keyStr)
        random.seed(keyseed)
        a = 10**(n-1)
        b = 10**n-1
        key = random.randint(a,b)
        return str(key)

    def cleanText(self,text):
        cleanText = []
        for c in text:
            if (ord(c) > 31) and (ord(c) < 127):
                cleanText.append(c)
        return cleanText


    

class Block():
    pass

class RSA():
    pass



if __name__ == "__main__":
    
        c = Stream()
        key = 'asRR15456eedf'
        
        plainText = open ('pText.txt',"r")
        pText = plainText.read()
        plainText.close()       
        cText = c.encrypt(pText,key)
        dText = c.decrypt(cText,key)
        cipherText = open ('cText.txt',"w")
        cipherText.write(cText)
        cipherText.close()
        decipherText = open ('dText.txt',"w")
        decipherText.write(dText)
        decipherText.close()
