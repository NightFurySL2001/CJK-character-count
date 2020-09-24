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
main.title("字体计数软件")
#window size
main.geometry('')
#prepare font
title_font=("Microsoft YaHei UI", 18, "bold underline")
text_font=("Microsoft YaHei UI", 16)
#add frame
frame = Frame(main)
frame.pack(padx=(25,45), pady=(0,30))


#text label + button
input_lbl = Label(frame, text="选择字体档：", font=text_font)
input_lbl.grid(column=0, row=0, sticky=E)
btn = Button(frame, text ='打开', font=text_font, command = lambda:open_file() )
btn.grid(column=1, row=0)

#show file name
font_name = StringVar()
font_name_lbl = Label(frame, textvariable=font_name, justify="left", font=text_font)
font_name_lbl.grid(column=3, row=0, sticky=W)
font_name.set("无")

font_txt_lbl = Label(frame, text="字体档：", justify="right", font=text_font)
font_txt_lbl.grid(column=2, row=0, sticky=E, padx=16)


#section 1: chinese encoding
#prepare listing for string var
cjk_lbl={}
cjk_empty={}
cjk_count={}
cjk_var={}

cjk_jian_start=2
cjk_enc_lbl = Label(frame, text="简体中文编码", font=title_font, anchor="w")
cjk_enc_lbl.grid(column=0, row=cjk_jian_start, sticky=W, padx=5)
#loop label for cjk jian
for i, (cjk_enc, cjk_enc_name) in enumerate(global_var.cjk_jian_list.items()):
    cjk_var[cjk_enc] = StringVar()
    cjk_lbl[cjk_enc] = Label(frame, text=cjk_enc_name+"：", justify="left", font=text_font).grid(column=0, row=i+cjk_jian_start+1, sticky=W)
    cjk_empty[cjk_enc] = Label(frame, textvariable=cjk_var[cjk_enc], justify="left", font=text_font).grid(column=1, row=i+cjk_jian_start+1)
    cjk_count[cjk_enc] = Label(frame, text="/"+str(global_var.cjk_count[cjk_enc]), justify="left", font=text_font).grid(column=2, row=i+cjk_jian_start+1, sticky=W)
    cjk_jian_fan_start=cjk_jian_start+i+1

cjk_jian_fan_start+=2
cjk_enc_lbl = Label(frame, text="简体/繁体中文编码", font=title_font, anchor="w")
cjk_enc_lbl.grid(column=0, row=cjk_jian_fan_start-1, rowspan=2, sticky="SW", padx=5)
#loop label for cjk jian-fan
for i, (cjk_enc, cjk_enc_name) in enumerate(global_var.cjk_jian_fan_list.items()):
    cjk_var[cjk_enc] = StringVar()
    cjk_lbl[cjk_enc] = Label(frame, text=cjk_enc_name+"：", justify="left", font=text_font).grid(column=0, row=i+cjk_jian_fan_start+1, sticky=W)
    cjk_empty[cjk_enc] = Label(frame, textvariable=cjk_var[cjk_enc], justify="left", font=text_font).grid(column=1, row=i+cjk_jian_fan_start+1)
    cjk_count[cjk_enc] = Label(frame, text="/"+str(global_var.cjk_count[cjk_enc]), justify="left", font=text_font).grid(column=2, row=i+cjk_jian_fan_start+1, sticky=W)
    cjk_fan_start=cjk_jian_fan_start+i+1

cjk_fan_start+=2
cjk_enc_lbl = Label(frame, text="繁体中文编码", font=title_font, anchor="w")
cjk_enc_lbl.grid(column=0, row=cjk_fan_start-1, rowspan=2, sticky="SW", padx=5)
#loop label for cjk jian-fan
for i, (cjk_enc, cjk_enc_name) in enumerate(global_var.cjk_fan_list.items()):
    cjk_var[cjk_enc] = StringVar()
    cjk_lbl[cjk_enc] = Label(frame, text=cjk_enc_name+"：", justify="left", font=text_font).grid(column=0, row=i+cjk_fan_start+1, sticky=W)
    cjk_empty[cjk_enc] = Label(frame, textvariable=cjk_var[cjk_enc], justify="left", font=text_font).grid(column=1, row=i+cjk_fan_start+1)
    cjk_count[cjk_enc] = Label(frame, text="/"+str(global_var.cjk_count[cjk_enc]), justify="left", font=text_font).grid(column=2, row=i+cjk_fan_start+1, sticky=W)



#section 2: unicode section
unicode_lbl = Label(frame, text="统一码区块", font=title_font)
unicode_lbl.grid(column=3, row=2, sticky=W, padx=5)
unicode_lbl={}
unicode_empty={}
unicode_count={}
unicode_var={}
unicode_last_tag=0
#listing with unicode area
for i, (unicode_enc, unicode_enc_name) in enumerate(global_var.unicode_cn_list.items()):
    unicode_row=i+3
    unicode_var[unicode_enc] = StringVar()
    unicode_lbl[unicode_enc] = Label(frame, text=unicode_enc_name+"：", justify="left", font=text_font).grid(column=3, row=unicode_row, sticky=W)
    unicode_empty[unicode_enc] = Label(frame, textvariable=unicode_var[unicode_enc], justify="left", font=text_font).grid(column=4, row=unicode_row)
    unicode_count[unicode_enc] = Label(frame, text="/"+str(global_var.unicode_count[unicode_enc]), justify="left", font=text_font).grid(column=5, row=unicode_row, sticky=W)

notice_oldname = Label(frame, text="＊旧称「3500 字常用汉字表」。", justify="right", font=text_font).grid(column=3, row=unicode_row+3, sticky=E, columnspan=3)

#open file react function
def open_file():
    #get file with open file dialog
    filename = fd.askopenfilename(initialdir = 'shell:Desktop', title="选择字体文件",
                                  filetypes = [("单独字体文件","*.ttf *.otf *.woff *.woff2"),
                                               ("TrueType 字体","*.ttf"),
                                               ("OpenType 字体","*.otf"),
                                               ("网页开放字体 (WOFF)","*.woff *.woff2"),
                                               ("全部文件","*.*")
                                              ]
                                 )
    #check if its font
    if filename.lower().endswith(".otf") or filename.lower().endswith(".ttf") or filename.lower().endswith(".woff") or filename.lower().endswith(".woff2"):
        #show filename
        font_name.set(path_leaf(filename))
        #reset 0
        for cjk_enc in global_var.cjk_list:
            cjk_var[cjk_enc].set(0)
        for unicode_enc in global_var.unicode_list:
            unicode_var[unicode_enc].set(0)
        #get character list in font
        char_list = get_char.font_import(filename)
        #get list count
        output = count_char.count_char(char_list)
        cjk_char_count = output[0]
        unicode_char_count = output[1]
        #update list count
        for cjk_enc in global_var.cjk_list:
            cjk_var[cjk_enc].set(cjk_char_count[cjk_enc])
        for unicode_enc in global_var.unicode_list:
            unicode_var[unicode_enc].set(unicode_char_count[unicode_enc])
    else:
        #not a font, change filename back to null n give error message
        font_name.set("无")
        messagebox.showwarning(title="错误", message="这不是一个标准字体档。")


#get filename only
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

#add icon
main.tk.call('wm', 'iconphoto', main._w, PhotoImage(file='appicon.png'))
#UI stay appear
main.mainloop()
