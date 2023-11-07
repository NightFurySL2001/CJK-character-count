from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import get_char
import count_char
import global_var
import ttc_get
import ntpath

#start window
main = Tk()
#set title
main.title("Font Character Count")
#window size
main.geometry('')
#prepare font
title_font=("Segoe UI", 12, "bold underline")
text_font=("Segoe UI",12)
#add frame
frame = Frame(main)
frame.pack(padx=(12,40), pady=(0,5))
#set module language
current_lang="en"

#text label + button
input_lbl = Label(frame, text="Choose font file: ", font=text_font)
input_lbl.grid(column=0, row=0)
btn = Button(frame, text ='Open', font=text_font, command = lambda:open_file() )
btn.grid(column=1, row=0)

#show file name
font_name = StringVar(main)
font_name_lbl = Label(frame, textvariable=font_name, justify="left", font=text_font)
font_name_lbl.grid(column=0, row=1, sticky=W)
font_name.set("File name: null")

#section 1: chinese encoding
cjk_enc_lbl = Label(frame, text="Chinese Encodings", font=title_font, anchor="w")
cjk_enc_lbl.grid(column=0, row=2)

cjk_lbl={}
cjk_empty={}
cjk_count={}
cjk_var={}
cjk_start=3
#listing with cjk encoding
for i, (cjk_enc, cjk_enc_name) in enumerate(global_var.cjk_list.items()):
    cjk_var[cjk_enc] = StringVar(main)
    cjk_lbl[cjk_enc] = Label(frame, text=cjk_enc_name+":", justify="left", font=text_font).grid(column=0, row=i+cjk_start, sticky=W)
    cjk_empty[cjk_enc] = Label(frame, textvariable=cjk_var[cjk_enc], justify="left", font=text_font).grid(column=1, row=i+cjk_start)
    cjk_count[cjk_enc] = Label(frame, text="/"+str(global_var.cjk_count[cjk_enc]), justify="left", font=text_font).grid(column=2, row=i+cjk_start, sticky=W)
    unicode_start=cjk_start+i

unicode_start+=1
#section 2: unicode section
unicode_lbl = Label(frame, text="Unicode Blocks", font=title_font)
unicode_lbl.grid(column=0, row=unicode_start)
unicode_lbl={}
unicode_empty={}
unicode_count={}
unicode_var={}
#listing with unicode area
for i, (unicode_enc, unicode_enc_name) in enumerate(global_var.unicode_list.items()):
    unicode_var[unicode_enc] = StringVar(main)
    unicode_lbl[unicode_enc] = Label(frame, text=unicode_enc_name+":", justify="left", font=text_font).grid(column=0, row=i+unicode_start+1, sticky=W)
    unicode_empty[unicode_enc] = Label(frame, textvariable=unicode_var[unicode_enc], justify="left", font=text_font).grid(column=1, row=i+unicode_start+1)
    unicode_count[unicode_enc] = Label(frame, text="/"+str(global_var.unicode_count[unicode_enc]), justify="left", font=text_font).grid(column=2, row=i+unicode_start+1, sticky=W)


#open file react function
def open_file():
    #get file with open file dialog
    filename = fd.askopenfilename(initialdir = 'shell:Desktop', title="Select font file",
                                  filetypes = [("All suppported font format","*.ttf *.otf *.woff *.woff2 *.otc *.ttc"),
                                               ("Single font file format","*.ttf *.otf *.woff *.woff2"),
                                               ("TrueType font","*.ttf"),
                                               ("OpenType font","*.otf"),
                                               ("Web Open Font Format (WOFF)","*.woff *.woff2"),
                                               ("OpenType collection font","*.otc *.ttc"),
                                               ("All files","*.*")
                                              ]
                                 )
    #test if the file is a valid font file
    is_a_font = False
    if (filename.lower().endswith(".otf") or filename.lower().endswith(".ttf") or filename.lower().endswith(".woff") or filename.lower().endswith(".woff2") or filename.lower().endswith(".otc") or filename.lower().endswith(".ttc")):
        # external module: get_char
        is_a_font = get_char.is_font(filename)
    
    #default value for non-TTCollection
    font_id = -1
    #for TTCollections, get which font to check
    if is_a_font and (filename.lower().endswith(".otc") or filename.lower().endswith(".ttc")):
        #get which font to use, if no choose will return 0 as default font - external module: ttc_get
        font_id = ttc_get.TTC_popup(main, filename, lang=current_lang).show()
        #if user not select
        if font_id is None:
            filename = "" #trigger as no font selected
            is_a_font = False #prevent font to process

    if is_a_font:
        #show filename
        font_name.set("File name: "+path_leaf(filename))
        #reset 0
        for cjk_enc in global_var.cjk_list:
            cjk_var[cjk_enc].set(0)
        for unicode_enc in global_var.unicode_list:
            unicode_var[unicode_enc].set(0)
        #get character list in font - external module: get_char
        char_list = get_char.font_import(filename, font_id, lang=current_lang)
        #get list count - external module: count_char
        output = count_char.count_char(char_list)
        cjk_char_count = output[0]
        unicode_char_count = output[1]
        #update list count
        for cjk_enc in global_var.cjk_list:
            cjk_var[cjk_enc].set(cjk_char_count[cjk_enc])
        for unicode_enc in global_var.unicode_list:
            unicode_var[unicode_enc].set(unicode_char_count[unicode_enc])
    elif filename == '' or filename is None:
        #no file selected, fd.askopenfilename() will return empty string
        font_name.set("File name: null")
        messagebox.showwarning(title="No file", message="No font selected.")
    elif not is_a_font:
        #not a font, change filename back to null n give error message
        font_name.set("File name: null")
        messagebox.showwarning(title="Not a font", message="This is not a valid font file.")
    else:
        #unknown error
        font_name.set("File name: null")
        messagebox.showwarning(title="Error", message="Something happened. Please try again.")



#get filename only
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

#add icon
main.tk.call('wm', 'iconphoto', main._w, PhotoImage(file='appicon.png'))
#UI stay appear
main.mainloop()
