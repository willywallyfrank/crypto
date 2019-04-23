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
            i = i - 1
        return reverse               

    def decrypt(self,cText):
        message = self.encrypt(cText)
        return message
        

class Ceasar():
        
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
        cText = ['']*key
        for col in range(key):
            position = col
            while position < len(pText):
                cText[col] = cText[col] + pText[position]
                position = position + key
        return ''.join(cText)
##
##    def decrypt(self,cText,key):
##        dText = ['']*key
##        position = 0
##        while position < len(cText):
##            for 
            




        
message = 'abcdefghijklmnopqrstuvwxyz'               
R = Reverse()
C = Ceasar()
T = Transposition()
cR = R.encrypt(message)
cC = C.encrypt(message,4)
cT = T.encrypt(message,4)
##print(cR)
##print(cC)
print(cT)


    
        
