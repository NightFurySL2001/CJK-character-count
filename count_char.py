from tkinter import *
import global_var

def count_char(char_list):

    #get font unicode list
    lines_seen = []
    font_uni_list = []
    font_list = []
    unicode_char_count={}
    #prepare unicode area count storage
    for item in global_var.unicode_list:
        unicode_char_count[item]=0
    
    #get cjk encoding character list
    cjk_dict = {}
    cjk_char_count = {}
    for encoding in global_var.cjk_list:
        #gb18030 no file list
        if encoding != "gb18030":
            cjk_dict[encoding] = load_sample_file(encoding+"-han.txt")
        cjk_char_count[encoding]=0
         
    for row in char_list:
        #check for duplicate as all `cmap` table are exported for all platform
        if row[0] not in lines_seen:
            lines_seen.append(row[0])
            #add cjk character for cjk encoding check
            if row[2][:3] == "CJK":
                #take character id and turn to hex for future update
                font_uni_list.append(hex(row[0]))

            #count kangxi radical
            #if row[2][:6] == "KANGXI": #2F00 — 2FDF Kangxi Radicals
            #    unicode_char_count["kangxi"]+=1

            #check range with base 10 unicode and count by range
            range = uni_range_check(row[0])
            #if range is defined by function (cjk only)
            if range:
                unicode_char_count[range]+=1

        #if already saw, skip it
        continue

    #process each uniqued named CJK character
    for char_num in font_uni_list:
        #get real character
        char = chr(deci(char_num))
        #filter and count cjk
        for encoding in global_var.cjk_list:
            #gb18030 no file list
            if encoding == "gb18030":
                continue
            if char in cjk_dict[encoding]:
                cjk_char_count[encoding]+=1
    
    #gb18030 mandatory CJK Unified Ideographs and CJK Unified Ideographs Extension A
    cjk_char_count["gb18030"]=unicode_char_count["basic"]+unicode_char_count["ext-a"]
    #print(unicode_char_count["ext-g"])
    return (cjk_char_count, unicode_char_count)



#load encoding file
def load_sample_file(filename):
    font_list = []
    for line in open(filename, "r", encoding="utf-8"):
        font_list.append(line.strip("\r\n"))
    return font_list

#conversion to base 10, return 0 if failed
def deci(number):
    try:
        return int(number,16)
    except:
        return 0

#check range of character:
def uni_range_check(char_base10):
    #filter and count unicode
    if char_base10 in range(deci("4E00"), deci("9FFF")): #4E00 - 9FFF CJK Unified Ideographs
        return "basic"
    elif char_base10 in range(deci("2F00"), deci("2FDF")): #2F00 — 2FDF Kangxi Radicals
        return "kangxi"
    elif char_base10 in range(deci("2E80"), deci("2EFF")): #2E80 — 2EFF CJK Radical Supplements
        return "kangxi-sup"
    elif char_base10 in range(deci("3400"), deci("4DBF")): #3400 — 4DBF CJK Unified Ideographs Extension A
        return "ext-a"
    elif char_base10 in range(deci("F900"), deci("FAFF")): #F900 — FAFF CJK Compatibility Ideographs
        return "compat"
    elif char_base10 in range(deci("20000"), deci("2A6DF")): #20000 — 2A6DF CJK Unified Ideographs Extension B
        return "ext-b"
    elif char_base10 in range(deci("2A700"), deci("2B73F")): #2A700 – 2B73F CJK Unified Ideographs Extension C
        return "ext-c"
    elif char_base10 in range(deci("2B740"), deci("2B81F")): #2B740 – 2B81F CJK Unified Ideographs Extension D
        return "ext-d"
    elif char_base10 in range(deci("2B820"), deci("2CEAF")): #2B820 – 2CEAF CJK Unified Ideographs Extension E
        return "ext-e"
    elif char_base10 in range(deci("2CEB0"), deci("2EBEF")): #2CEB0 – 2EBEF CJK Unified Ideographs Extension F
        return "ext-f"
    elif char_base10 in range(deci("2F800"), deci("2FA1F")): #2F800 — 2FA1F CJK Compatibility Ideographs Supplement
        return "compat-sup"
    elif char_base10 in range(deci("30000"), deci("3134F")): #30000 - 3134F CJK Unified Ideographs Extension G
        return "ext-g"
