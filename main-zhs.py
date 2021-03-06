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
main.title("字体计数软件")
#window size
main.geometry('')
#prepare font
title_font=("Microsoft YaHei UI", 18, "bold underline")
text_font=("Microsoft YaHei UI", 16)
#add frame
frame = Frame(main)
frame.pack(padx=(25,40), pady=(0,30))
#set module language
current_lang="zhs"


#text label + button
input_lbl = Label(frame, text="选择字体档：　　　", font=text_font)
input_lbl.grid(column=0, row=0, sticky=E)
btn = Button(frame, text ='打开', font=text_font, command = lambda:open_file() )
btn.grid(column=0, row=0, sticky=E)

#show file name
font_name = StringVar(main)
font_name_lbl = Label(frame, textvariable=font_name, justify="left", font=text_font)
font_name_lbl.grid(column=2, row=0, sticky=W, columnspan=3)
font_name.set("无")

font_txt_lbl = Label(frame, text="字体档：", justify="right", font=text_font)
font_txt_lbl.grid(column=1, row=0, sticky=E, padx=(5,0))


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
for i, (cjk_enc, cjk_enc_name) in enumerate(global_var.cjk_jian_list_zhs.items()):
    cjk_var[cjk_enc] = StringVar(main)
    cjk_lbl[cjk_enc] = Label(frame, text=cjk_enc_name+"：", justify="left", font=text_font).grid(column=0, row=i+cjk_jian_start+1, sticky=W)
    cjk_empty[cjk_enc] = Label(frame, textvariable=cjk_var[cjk_enc], justify="left", font=text_font).grid(column=1, row=i+cjk_jian_start+1)
    cjk_count[cjk_enc] = Label(frame, text="/"+str(global_var.cjk_count[cjk_enc]), justify="left", font=text_font).grid(column=2, row=i+cjk_jian_start+1, sticky=W)
    cjk_jian_fan_start=cjk_jian_start+i+1

cjk_jian_fan_start+=2
cjk_enc_lbl = Label(frame, text="简体/繁体中文编码", font=title_font, anchor="w")
cjk_enc_lbl.grid(column=0, row=cjk_jian_fan_start-1, rowspan=2, sticky="SW", padx=5)
#loop label for cjk jian-fan
for i, (cjk_enc, cjk_enc_name) in enumerate(global_var.cjk_jian_fan_list_zhs.items()):
    cjk_var[cjk_enc] = StringVar(main)
    cjk_lbl[cjk_enc] = Label(frame, text=cjk_enc_name+"：", justify="left", font=text_font).grid(column=0, row=i+cjk_jian_fan_start+1, sticky=W)
    cjk_empty[cjk_enc] = Label(frame, textvariable=cjk_var[cjk_enc], justify="left", font=text_font).grid(column=1, row=i+cjk_jian_fan_start+1)
    cjk_count[cjk_enc] = Label(frame, text="/"+str(global_var.cjk_count[cjk_enc]), justify="left", font=text_font).grid(column=2, row=i+cjk_jian_fan_start+1, sticky=W, padx=(0,16))
    cjk_fan_start=cjk_jian_fan_start+i+1

cjk_fan_start+=2
cjk_enc_lbl = Label(frame, text="繁体中文编码", font=title_font, anchor="w")
cjk_enc_lbl.grid(column=0, row=cjk_fan_start-1, rowspan=2, sticky="SW", padx=5)
#loop label for cjk fan
for i, (cjk_enc, cjk_enc_name) in enumerate(global_var.cjk_fan_list_zhs.items()):
    cjk_var[cjk_enc] = StringVar(main)
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
for i, (unicode_enc, unicode_enc_name) in enumerate(global_var.unicode_list_zhs.items()):
    unicode_row=i+3
    unicode_var[unicode_enc] = StringVar(main)
    unicode_lbl[unicode_enc] = Label(frame, text=unicode_enc_name+"：", justify="left", font=text_font).grid(column=3, row=unicode_row, sticky=W)
    unicode_empty[unicode_enc] = Label(frame, textvariable=unicode_var[unicode_enc], justify="left", font=text_font).grid(column=4, row=unicode_row)
    unicode_count[unicode_enc] = Label(frame, text="/"+str(global_var.unicode_count[unicode_enc]), justify="left", font=text_font).grid(column=5, row=unicode_row, sticky=W)

notice_oldname = Label(frame, text="＊旧称「3500 字常用汉字表」。", justify="right", font=text_font).grid(column=3, row=unicode_row+3, sticky=E, columnspan=3)

#open file react function
def open_file():
    #get file with open file dialog
    filename = fd.askopenfilename(initialdir = 'shell:Desktop', title="选择字体文件",
                                  filetypes = [("所有支援的字体格式","*.ttf *.otf *.woff *.woff2 *.otc *.ttc"),
                                               ("单独字体文件","*.ttf *.otf *.woff *.woff2"),
                                               ("TrueType 字体","*.ttf"),
                                               ("OpenType 字体","*.otf"),
                                               ("网页开放字体 (WOFF)","*.woff *.woff2"),
                                               ("OpenType 合集字体","*.otc *.ttc"),
                                               ("全部文件","*.*")
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
        font_name.set(path_leaf(filename))
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
        font_name.set("无")
        messagebox.showwarning(title="无选择", message="没有选择字体。")
    elif not is_a_font:
        #not a font, change filename back to null n give error message
        font_name.set("无")
        messagebox.showwarning(title="非字体", message="这不是一个标准字体档。")
    else:
        #unknown error
        font_name.set("无")
        messagebox.showwarning(title="错误", message="出现问题，请重试。")
        


#get filename only
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

#add icon
main.tk.call('wm', 'iconphoto', main._w, PhotoImage(file='appicon.png'))
#UI stay appear
main.mainloop()
