from tkinter import messagebox

from itertools import chain
import sys

from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode

def font_import(filename):
    messagebox.showinfo("Progress","Loaded file: "+filename)
    ttf = TTFont(filename, 0, verbose=0, allowVID=0,
                    ignoreDecompileErrors=True,
                    fontNumber=-1)

    chars = chain.from_iterable([y + (Unicode[y[0]],) for y in x.cmap.items()] for x in ttf["cmap"].tables)
    return chars

