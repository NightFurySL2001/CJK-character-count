from tkinter import messagebox
from fontTools.ttLib import TTFont

def font_import(filename, font_id=-1, lang="en"):
    #language localization
    if lang == "zhs": #simplified chinese
        message_title = "进度"
        message_text = "已加载字体文件："
    elif lang == "zht": #traditional chinese
        message_title = "進度"
        message_text = "已加載字型文件："
    else:
        message_title = "Progress"
        message_text = "Loaded font file: "
    
    messagebox.showinfo(message_title , message_text+filename)
    #open font with given number
    ttf = TTFont(filename, 0, allowVID=0,
                    ignoreDecompileErrors=True,
                    fontNumber=font_id)
    #get chars from cmap
    chars = set(y[0] for x in ttf["cmap"].tables for y in x.cmap.items())

    #close font
    ttf.close()
    return chars

def is_font(filename):
    try: #open the font with TTFont
        #if ttc or otc, fontNumber must be 0 (first font in otc)
        if filename.lower().endswith(".otc") or filename.lower().endswith(".ttc"):
            font = TTFont(filename, 0, allowVID=0,
                        ignoreDecompileErrors=True,
                        fontNumber=0)
        else: #single font use fontNumber=-1
            font = TTFont(filename, 0, allowVID=0,
                        ignoreDecompileErrors=True,
                        fontNumber=-1)
        #close font
        font.close()
        return True
    except:
        return False