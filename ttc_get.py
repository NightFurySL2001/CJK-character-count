from tkinter import *

from fontTools.ttLib import TTCollection


def get_ttc_list(filename):
    #clear font list
    ttc_names = []
    #lazy=True: https://github.com/fonttools/fonttools/issues/2019
    ttc = TTCollection(filename, lazy=True)
    for font in ttc:
        # single font name in getName(nameID, platformID, platEncID, langID=None), 0x409 make sure all font in English name
        ttf_name=font["name"].getName(4, 3, 1, 0x409)
        # add the font name itself instead of the XML representation
        ttc_names.append(str(ttf_name))
    #return array of names
    return ttc_names


class TTC_popup (object):
    #TTC_popup(main, filename) refering to (master, filename) below when initialing
    def __init__(self, master, filename, lang="en"):
        #language localization
        if lang == "zhs": #simplified chinese
            toplevel_title = "OpenType合集字体选择"
            toplevel_label = "选择计数的字体："
        elif lang == "zht": #traditional chinese
            toplevel_title = "OpenType合集字型選擇"
            toplevel_label = "選擇計數的字型："
        else:
            toplevel_title = "OpenType collection selection"
            toplevel_label = "Pick font for counting:"
        
        #create Toplevel popup
        self.toplevel = Toplevel(master)
        self.toplevel.title(toplevel_title)
        self.toplevel.minsize(400,150)
        #prepare variable to store font name
        self.ttc_name = StringVar()
        #create ttc name list in this object
        self.ttc_list = get_ttc_list(filename)

        popup_font=('Microsoft YaHei UI', 12)

        label = Label(self.toplevel, text=toplevel_label, font=popup_font)
        label.pack(pady=(12,0)) #padding above label

        #drop down menu with ttc_name storing option in *ttc_list
        option = OptionMenu(self.toplevel, self.ttc_name, *self.ttc_list)
        option.config(font=popup_font)
        option.pack(fill="x", padx=12) #padding at both side of dropdown list

        #button on click destroy the toplevel and return back to .show()
        button = Button(self.toplevel, text="OK", font=popup_font, command=self.toplevel.destroy)
        button.pack(pady=(0,12)) #padding below button
        
    #TTC_popup(main, filename).show() will initiate __init__ before calling show(self)
    def show(self):
        #waits for window to destroy before continuing
        self.toplevel.wait_window()
        try:
            #convert ttc_name to id in ttc_list
            self.result_id = self.ttc_list.index(self.ttc_name.get())
            #return result_id
            return self.result_id
        except: #font is not in list, assume as no font chosen
            #return None, parse as no font selected
            return None
