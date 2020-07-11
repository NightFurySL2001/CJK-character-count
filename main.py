from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import get_char
import count_char
import global_var
import ntpath

#start window
main = Tk()
#set title
main.title("Font Character Count")
#window size
main.geometry('500x750')

output_text=StringVar(main)

#text label + button
input_lbl = Label(main, text="Choose font file: ")
input_lbl.grid(column=0, row=0)
btn = Button(main, text ='Open', command = lambda:open_file() )
btn.grid(column=1, row=0)

#show file name
font_name = StringVar()
font_name_lbl = Label(main, textvariable=font_name, justify="left")
font_name_lbl.grid(column=0, row=1, sticky=W, padx=12)
font_name.set("File name: null")

#section 1: chinese encoding
my_font=("Segoe UI",12, "underline")
cjk_enc_lbl = Label(main, text="Chinese Encodings", font=my_font, anchor="w")
cjk_enc_lbl.grid(column=0, row=2)

cjk_lbl={}
cjk_empty={}
cjk_count={}
cjk_var={}
cjk_start=3
#listing with cjk encoding
for i, (cjk_enc, cjk_enc_name) in enumerate(global_var.cjk_list.items()):
    cjk_var[cjk_enc] = StringVar()
    cjk_lbl[cjk_enc] = Label(main, text=cjk_enc_name+":", justify="left").grid(column=0, row=i+cjk_start, sticky=W, padx=12)
    cjk_empty[cjk_enc] = Label(main, textvariable=cjk_var[cjk_enc], justify="left").grid(column=1, row=i+cjk_start)
    cjk_count[cjk_enc] = Label(main, text="/"+str(global_var.cjk_count[cjk_enc]), justify="left").grid(column=2, row=i+cjk_start, sticky=W)
    unicode_start=cjk_start+i

unicode_start+=1
#section 2: unicode section
unicode_lbl = Label(main, text="Unicode Sector", font=my_font)
unicode_lbl.grid(column=0, row=unicode_start)
unicode_lbl={}
unicode_empty={}
unicode_count={}
unicode_var={}
#listing with unicode area
for i, (unicode_enc, unicode_enc_name) in enumerate(global_var.unicode_list.items()):
    unicode_var[unicode_enc] = StringVar()
    unicode_lbl[unicode_enc] = Label(main, text=unicode_enc_name+":", justify="left").grid(column=0, row=i+unicode_start+1, sticky=W, padx=12)
    unicode_empty[unicode_enc] = Label(main, textvariable=unicode_var[unicode_enc], justify="left").grid(column=1, row=i+unicode_start+1)
    unicode_count[unicode_enc] = Label(main, text="/"+str(global_var.unicode_count[unicode_enc]), justify="left").grid(column=2, row=i+unicode_start+1, sticky=W)


#open file react function
def open_file():
    #get file with open file dialog
    filename = fd.askopenfilename(initialdir = 'shell:Desktop', title="Select font file",
                                  filetypes = [("TrueType/OpenType font","*.ttf *.otf"),
                                               ("TrueType font","*.ttf"),
                                               ("OpenType font","*.otf"),
                                               ("All files","*.*")
                                              ]
                                 )
    #check if its font
    if filename.lower().endswith(".otf") or filename.lower().endswith(".ttf"):
        #show filename
        font_name.set("File name: "+path_leaf(filename))
        #get character list in font
        char_list = get_char.font_import(filename)
        #get count
        output = count_char.count_char(char_list)
        cjk_char_count = output[0]
        unicode_char_count = output[1]
        #update count
        for cjk_enc in global_var.cjk_list:
            cjk_var[cjk_enc].set(cjk_char_count[cjk_enc])
        for unicode_enc in global_var.unicode_list:
            unicode_var[unicode_enc].set(unicode_char_count[unicode_enc])
    else:
        #not a font, change filename back to null n give error message
        font_name.set("File name: null")
        messagebox.showwarning(title="Error", message="This is not a font file.")


#get filename only
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

#UI stay appear
main.mainloop()
