from math import *
from datetime import *
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import Image
import numpy as np

symSet = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
          'r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
           'S','T','U','V','W','X','Y','Z',' ',',','<','.','>','/','?','"','!','@','#','$','$$','%','^','*','(',')',
           '-','_','+','=','[',']','{','}','|','\',',':',';','`','~','&','\\',"'"]


class Cipher_GUI(Frame):

    def __init__(self,master = None):

        Frame.__init__(self,master)
        
        self.font_type = 'arial 12 bold'
        self.master.title('Affine Cipher')
        self.master.geometry('875x435')
        self.master.configure(bg = '#adadad')
        self.plain_text = ''
        self.cText = ''
        self.letters = ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g',
                   'y','p','b','v','k','j','x','q','z']
        self.widgets()
         
    def clip_board(self):    
        data = self.output.get('1.0', END)
        root.clipboard_clear()
        root.clipboard_append(data)

    def open_text(self):
        Pfile = askopenfilename()
        plainText = open (Pfile,"r")
        self.pText = plainText.read()
        plainText.close()
        self.output.delete('1.0',END)        
        self.output.insert('1.0',self.pText)
        
    def encrypt_text(self):
        a = int(self.a_ent.get('1.0',END))
        b = int(self.b_ent.get('1.0',END))
        pText = self.output.get('1.0',END)
        self.pText = pText
        pTextVal = []
        for c in pText:
            if c in symSet:
                pTextVal.append(symSet.index(c))
        trans_pvals = [(a + b*x)%97 for x in pTextVal]
        ctextList =  [symSet[c] for c in trans_pvals]
        self.cText =  ''.join(ctextList)        
        self.output.delete('1.0',END)        
        self.output.insert('1.0',self.cText)        


    def decrypt_text(self):
        a = int(self.a_ent.get('1.0',END))
        b = int(self.b_ent.get('1.0',END))
        ctext = str(self.output.get('1.0',END)).rstrip('\n')
        self.cText = ctext
        cTextVal = [symSet.index(c) for c in ctext]
        bInv = b**95%97
        trans_cvals = [((x - a)*bInv)%97 for x in cTextVal]
        ptextList =  [symSet[c] for c in trans_cvals]
        pText =  ''.join(ptextList)
        self.output.delete('1.0',END)        
        self.output.insert('1.0',pText)

    def reset(self):
        self.output.delete('1.0',END)        
        self.output.insert('1.0',self.cText)        

    def save_file(self):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        saved_text = str(self.output.get(1.0, END)) 
        file.write(saved_text)
        file.close()
      
    def hide_key(self):
        Ifile = filedialog.askopenfile()
        img = Image.open(Ifile.name)
        a = int(self.a_ent.get('1.0',END))
        b = int(self.b_ent.get('1.0',END))
        hidden_text = 'Key: a:{}, b:{}'.format(a,b)
        length = len(hidden_text)
        if length > 255:
            print("text too long! (don't exeed 255 characters)")
            return False
        if img.mode != 'RGB':
            img = img.convert("RGB")          
        encoded = img.copy()
        width, height = img.size
        index = 0
        for row in range(height):
            for col in range(width):
                r, g, b = img.getpixel((col, row))
                if row == 0 and col == 0 and index < length:
                    asc = length
                elif index <= length:
                    c = hidden_text[index -1]
                    asc = ord(c)
                else:
                    asc = r
                encoded.putpixel((col, row), (asc, g , b))
                index += 1
        encoded.save(Ifile.name)

    def find_key(self):
        Ifile = filedialog.askopenfile()
        img = Image.open(Ifile.name)
        """
        check the red portion of an image (r, g, b) tuple for
        hidden message characters (ASCII values)
        """
        width, height = img.size
        key = ""
        index = 0
        for row in range(height):
            for col in range(width):
                try:
                    r, g, b = img.getpixel((col, row))
                except ValueError:
                    # need to add transparency a for some .png files
                    r, g, b, a = img.getpixel((col, row))		
                # first pixel r value is length of message
                if row == 0 and col == 0:
                    length = r
                elif index <= length:
                    key += chr(r)
                index += 1
        self.label_key.config(text = key)

    def clear_ab(self):
        self.a_ent.delete('1.0',END)
        self.b_ent.delete('1.0',END)
        
    def clear_key(self):
        self.label_key.config(text = '')
        
    def clear_crackKey(self):
        self.c1_ent.delete('1.0',END)
        self.p1_ent.delete('1.0',END)
        self.c2_ent.delete('1.0',END)
        self.p2_ent.delete('1.0',END)

    def show_image(self):
        Ifile = filedialog.askopenfile()
        img = Image.open(Ifile.name)
        img.show()

    def ctextanalyze(self):

        letters = self.letters
        relfreq = [.127,.096,.082,.075,.07,.068,.063,.061,.06,.043,.04,.028,.028,.024,
                   .024,.022,.02,.02,.019,.015,.01,.008,.002,.002,.001,.001]
        
        sym = []
        symfreq = []
        cTextL = str(self.output.get(1.0, END)).lower()
        for c in cTextL:
            if (c in symSet) and (c not in sym):
                sym.append(c)
                symfreq.append(cTextL.count(c))
        symFreq_dict = dict(zip(sym,symfreq))
        symfreqOrd = sorted(symfreq, reverse=True)
        symOrd = sorted(symFreq_dict, key = symFreq_dict.__getitem__, reverse=True)

        N1 = len(symOrd)
        x1 = np.arange(N1)
        width = 1
        plt.subplot(211)
        plt.bar( x1, symfreqOrd, width, color = "y" )
        plt.ylabel( 'symbol frequency' )
        plt.xticks(x1, symOrd )
        

        N2 = len(str(self.output.get(1.0, END)))
        xfreq = [N2*x for x in relfreq]
        x2 = np.arange(26)
        width = 1
        plt.subplot(212)
        plt.bar(x2,xfreq,width,color='y')
        plt.ylabel('expected frequencies')
        plt.xticks(x2,letters)
        plt.show()
        
    def letter_dist(self):
        letters = self.letters
        relfreq = [.127,.096,.082,.075,.07,.068,.063,.061,.06,.043,.04,.028,.028,.024,
                   .024,.022,.02,.02,.019,.015,.01,.008,.002,.002,.001,.001]
        N = len(str(self.output.get(1.0, END)))
        freq = [N*x for x in relfreq]
        x = np.arange(26)
        width = 1
        plt.bar(x,freq,width,color='y')
        plt.ylabel('expected frequencies')
        plt.xticks(x,letters)
        plt.show()

    def crack_key(self):
        self.clear_ab()
        ss1 = str(self.c1_ent.get(1.0, END)).rstrip('\n')
        ps1 = str(self.p1_ent.get(1.0, END)).rstrip('\n')
        ss2 = str(self.c2_ent.get(1.0, END)).rstrip('\n')
        ps2 = str(self.p2_ent.get(1.0, END)).rstrip('\n')

        c1 = symSet.index(ss1)
        c2 = symSet.index(ss2)
        p1 = symSet.index(ps1)
        p2 = symSet.index(ps2)
        
        cd = (c1 - c2)
        pd = (p1 - p2)
        b = (pd**95 * cd)%97
        a = (49*(  c1 + c2 - b*(p1 + p2)))%97
        self.a_ent.insert('1.0',a)
        self.b_ent.insert('1.0',b)  
        
    def clear_text(self):
        self.output.delete('1.0',END)
        
    def widgets(self):
        
        self.input_frame = Frame(self.master,bg = '#adadad')
        self.input_frame.grid(column = 0, row= 0, columnspan=1,padx = (10,10), pady = (10,10))
        self.inputR_frame = Frame(self.master,bg = '#adadad')
        self.inputR_frame.grid(column = 5, row = 0, columnspan=1,padx = (10,10), pady = (10,10))
        self.output_frame = Frame(self.master,bg = '#adadad')
        self.output_frame.grid(column = 1, row= 0, columnspan=4,rowspan = 4,padx = (10,10), pady = (10,10))
        self.output = Text(self.output_frame,font=(self.font_type),bg = 'white',fg = 'black',width = 50,height = 20)
        self.output.grid(column = 0,row = 0, columnspan = 4, rowspan = 1, sticky = N)
        self.scroll = Scrollbar(self.output_frame)
        self.output.config(yscrollcommand = self.scroll.set)
        self.scroll.config(command = self.output.yview)
        self.scroll.grid(column = 4, row = 0,rowspan = 1,sticky='ns')
        root_menu = Menu(self.master)        
        self.master.config(menu = root_menu)        
        file_menu = Menu(root_menu) 
        root_menu.add_cascade(label = "File", menu = file_menu) 
        file_menu.add_command(label = "Exit",command = self.master.destroy)      
        edit_menu = Menu(root_menu)
        root_menu.add_cascade(label = "Functions", menu = edit_menu)                      
        edit_menu.add_command(label = "1. Symbol Frequency",command = self.ctextanalyze)
        edit_menu.add_command(label = "2. Expected Letter Freq",command = self.letter_dist)
        edit_menu.add_command(label = "3. Clear text",command = self.clear_text)
        edit_menu.add_command(label = "4. Clear a,b values",command = self.clear_ab)
        edit_menu.add_command(label = "5. Clear key",command = self.clear_key)
        edit_menu.add_command(label = "6. Clear Key Crack values",command = self.clear_crackKey)
        edit_menu.add_command(label = "7. Copy -> Clip Board")        
        Label(self.input_frame,text='Key:= (a + bP)mod97',font=(self.font_type),bg='#adadad',fg= '#9a005a').grid(row = 0,column = 0)   
        self.label_a = Label(self.input_frame,text='Key value: a =',font=(self.font_type),bg='#adadad',fg= '#9a005a')
        self.label_a.grid(row = 1,column = 0, sticky = 'w')
        self.a_ent = Text(self.input_frame,width = 14,height = 1,font=(self.font_type),bg='#adadad',fg = 'blue')
        self.a_ent.grid(row = 2, column = 0, sticky = W , padx = (10,10), pady = (10,10)) 
        self.label_b = Label(self.input_frame,text='Key value: b =  ',font=(self.font_type),bg='#adadad',fg= '#9a005a')
        self.label_b.grid(row = 3,column = 0, sticky = W, padx = (10,10), pady = (10,10))
        self.b_ent = Text(self.input_frame,width = 14,height = 1,font=(self.font_type),bg='#adadad',fg = 'blue')
        self.b_ent.grid(row = 4, column = 0, sticky = W, padx = (10,10), pady = (10,10)) 
        self.button_open_text = Button(self.input_frame,text=' Load Text ',
                                    font=(self.font_type),bg='#adadad',fg = 'blue',command = self.open_text)
        self.button_open_text.grid(row = 5,column = 0, sticky = W, padx = (10,10), pady = (10,10))
        self.button_encrypt_text = Button(self.input_frame,text='Encrypt Text',
                                    font=(self.font_type),bg='#adadad',fg = 'blue',command = self.encrypt_text)
        self.button_encrypt_text.grid(row = 6,column = 0, sticky = W, padx = (10,10), pady = (10,10))
        self.button_decrypt_text = Button(self.input_frame,text='Decrypt Text',
                                    font=(self.font_type),bg='#adadad',fg = 'blue',command = self.decrypt_text)
        self.button_decrypt_text.grid(row = 7,column = 0, sticky = W, padx = (10,10), pady = (10,10))
        self.button_save_file = Button(self.input_frame,text=' Save Text ',
                                    font=(self.font_type),bg='#adadad',fg = 'blue',command = self.save_file)
        self.button_save_file.grid(row = 8,column = 0, sticky = W, padx = (10,10), pady = (10,10))
        
        self.label_hide_key = Label(self.inputR_frame,text='Hide Key in Image',font=(self.font_type),bg='#adadad', fg= '#9a005a')
        self.label_hide_key.grid(row = 0,column = 0, sticky = W,columnspan = 2)
        self.hide_key_but = Button(self.inputR_frame,text='Hide Key in Image..',
                                    font=(self.font_type),bg='#adadad',fg = 'blue',command = self.hide_key)
        self.hide_key_but.grid(row = 1,column = 0, sticky = W, padx = (10,10), pady = (10,10),columnspan = 2)
        self.show_image_but = Button(self.inputR_frame,text=' Show  Image ',
                                    font=(self.font_type),bg='#adadad',fg = 'blue',command = self.show_image)
        self.show_image_but.grid(row = 2,column = 0, sticky = W, padx = (10,10), pady = (10,10),columnspan = 2)        
        self.find_key_but = Button(self.inputR_frame,text='Find Key in Image..',
                                    font=(self.font_type),bg='#adadad',fg = 'blue',command = self.find_key)
        self.find_key_but.grid(row = 3,column = 0, sticky = W, padx = (10,10), pady = (10,10),columnspan = 2)
        self.label_key = Label(self.inputR_frame,text='',font=(self.font_type),bg='#adadad', fg= '#9a005a')
        self.label_key.grid(row = 4,column = 0, sticky = W,columnspan = 2)
        
        self.label_keyCrack = Label(self.inputR_frame,text='Crack Cipher Key',font=(self.font_type),bg='#adadad', fg= '#9a005a')
        self.label_keyCrack.grid(row = 5,column = 0, sticky = W,columnspan = 2)

        self.label_csymbol1 = Label(self.inputR_frame,text='CT sym 1 -> PT sym 1',font=(self.font_type),bg='#adadad', fg= '#9a005a')
        self.label_csymbol1.grid(row = 6,column = 0, sticky = W,columnspan = 2)


        self.c1_ent = Text(self.inputR_frame,width = 2,height = 1,font=('arial 12 bold'),bg='#adadad',fg = 'blue')
        self.c1_ent.grid(row = 7, column = 0, sticky = W , padx = (10,10), pady = (10,10)) 
        self.p1_ent = Text(self.inputR_frame,width = 2,height = 1,font=('arial 12 bold'),bg='#adadad',fg = 'blue')
        self.p1_ent.grid(row = 7, column = 1, sticky = W , padx = (10,10), pady = (10,10)) 

        self.label_csymbol2 = Label(self.inputR_frame,text='CT sym 2 -> PT sym 2',font=(self.font_type),bg='#adadad', fg= '#9a005a')
        self.label_csymbol2.grid(row = 8,column = 0, sticky = W,columnspan = 2)


        self.c2_ent = Text(self.inputR_frame,width = 2,height = 1,font=('arial 12 bold'),bg='#adadad',fg = 'blue')
        self.c2_ent.grid(row = 9, column = 0, sticky = W , padx = (10,10), pady = (10,10)) 
        self.p2_ent = Text(self.inputR_frame,width = 2,height = 1,font=('arial 12 bold'),bg='#adadad',fg = 'blue')
        self.p2_ent.grid(row = 9, column = 1, sticky = W , padx = (10,10), pady = (10,10)) 

        self.button_crack_key = Button(self.inputR_frame,text='Crack Key',
                                    font=(self.font_type),bg='#adadad',fg = 'blue',command = self.crack_key)
        self.button_crack_key.grid(row = 10,column = 0, columnspan = 1,sticky = W, padx = (10,10), pady = (10,10))
        self.button_reset = Button(self.inputR_frame,text='Reset',
                                    font=(self.font_type),bg='#adadad',fg = 'blue',command = self.reset)
        self.button_reset.grid(row = 10,column = 1, columnspan = 1,sticky = W, padx = (10,10), pady = (10,10))

            
root = Tk()
cipherSpace = Cipher_GUI(root)
root.mainloop()
