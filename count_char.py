from tkinter import *
import global_var
import os

#special cjk compatibility for gbk, defined at end
global gbk_compatibility_deci_list
gbk_compatibility_deci_list = []

global cjk_compatibility_ideographs_deci_list
cjk_compatibility_ideographs_deci_list = []

#function prevent closing popup
def disable_event():
    pass

#input:char_list iterable
# master to create popup
# lang to change popup lang
#output:tuple of number 
def count_char(char_list, master, lang="en"):
    #get font unicode list
    unicode_char_count={}

    #prepare unicode area count storage
    for item in global_var.unicode_list:
        unicode_char_count[item]=0
    #prepare cjk encoding count storage, moved extracting text from txt to main code bottom
    for encoding in global_var.cjk_list:
        cjk_char_count[encoding]=0

    #row is unicode in decimal
    for row in char_list:
        #check range with base 10 unicode and count by range
        range = uni_range_check(row)

        #if character is in cjk range
        if range:
            #count unicode range
            unicode_char_count[range]+=1

            #compatibility but unified ideographs, use cjk_compatibility_ideographs_deci_list
            if range == "compat" and row in cjk_compatibility_ideographs_deci_list:
                unicode_char_count["compat-ideo"]+=1

            #cjk encoding is only count if it is in cjk range of unicode
            #get real character
            char = chr(row)
            #filter and count cjk
            for encoding in global_var.cjk_list:
                #gb18030 no file list, escape total
                if encoding == "gb18030":
                    continue
                #gbk no file list, however use CJK range in Unicode 1.0
                if encoding == "gbk":
                    if row in char_range(deci("4E00"), deci("9FA5")) or row in gbk_compatibility_deci_list:
                        cjk_char_count[encoding]+=1
                    continue
                #see if in cjk encoding
                if char in cjk_dict[encoding]:
                    cjk_char_count[encoding]+=1

        #if already saw, skip it
        continue

    #gb18030 mandatory CJK Unified Ideographs and CJK Unified Ideographs Extension A
    cjk_char_count["gb18030"]=unicode_char_count["basic"]+unicode_char_count["ext-a"]+unicode_char_count["zero"]
    
    #sum up total cjk unified ideographs
    unicode_char_count["total"] = unicode_char_count["zero"]+unicode_char_count["basic"]+unicode_char_count["ext-a"]+unicode_char_count["compat-ideo"]+unicode_char_count["ext-b"]+unicode_char_count["ext-c"]+unicode_char_count["ext-d"]+unicode_char_count["ext-e"]+unicode_char_count["ext-f"]
    #print(unicode_char_count["ext-g"])
    return (cjk_char_count, unicode_char_count)



#load encoding file
def load_sample_file(filename):
    font_list = []
    full_path = os.path.join(global_var.main_directory, filename)
    for line in open(full_path, "r", encoding="utf-8"):
        font_list.append(line.strip("\r\n").strip(" "))
    return set(font_list)

#conversion to base 10, return 0 if failed
def deci(number):
    try:
        return int(number,16)
    except:
        return 0

# special check range function as python default range don't include ending number
def char_range(start, end):
    return range(start, end+1)
# normal range: range(0,5) --> [0,1,2,3,4], len(range(0,5))=5
# character detect range: char_range(0,5) --> [0,1,2,3,4,5], len(char_range(0,5))=6

#check range of character:
def uni_range_check(char_base10):
    #filter and count unicode
    if char_base10 in char_range(deci("4E00"), deci("9FFF")): #4E00 - 9FFF CJK Unified Ideographs
        return "basic"
    elif char_base10 in char_range(deci("2F00"), deci("2FDF")): #2F00 — 2FDF Kangxi Radicals
        return "kangxi"
    elif char_base10 in char_range(deci("2E80"), deci("2EFF")): #2E80 — 2EFF CJK Radical Supplements
        return "kangxi-sup"
    elif char_base10 == 12295: # U+3007 Ideographic Number Zero Unicode Character
        return "zero"
    elif char_base10 in char_range(deci("3400"), deci("4DBF")): #3400 — 4DBF CJK Unified Ideographs Extension A
        return "ext-a"
    elif char_base10 in char_range(deci("F900"), deci("FAFF")): #F900 — FAFF CJK Compatibility Ideographs
        return "compat"
    elif char_base10 in char_range(deci("20000"), deci("2A6DF")): #20000 — 2A6DF CJK Unified Ideographs Extension B
        return "ext-b"
    elif char_base10 in char_range(deci("2A700"), deci("2B73F")): #2A700 – 2B73F CJK Unified Ideographs Extension C
        return "ext-c"
    elif char_base10 in char_range(deci("2B740"), deci("2B81F")): #2B740 – 2B81F CJK Unified Ideographs Extension D
        return "ext-d"
    elif char_base10 in char_range(deci("2B820"), deci("2CEAF")): #2B820 – 2CEAF CJK Unified Ideographs Extension E
        return "ext-e"
    elif char_base10 in char_range(deci("2CEB0"), deci("2EBEF")): #2CEB0 – 2EBEF CJK Unified Ideographs Extension F
        return "ext-f"
    elif char_base10 in char_range(deci("2F800"), deci("2FA1F")): #2F800 — 2FA1F CJK Compatibility Ideographs Supplement
        return "compat-sup"
    elif char_base10 in char_range(deci("30000"), deci("3134F")): #30000 - 3134F CJK Unified Ideographs Extension G
        return "ext-g"
    elif char_base10 in char_range(deci("31350"), deci("323AF")): #31350 - 323AF CJK Unified Ideographs Extension H
        return "ext-h"


#definition of gbk_compatibility_deci_list and cjk_compatibility_ideographs_deci_list, require deci(number)
cjk_compatibility_list_hex=["FA0E", "FA0F", "FA11", "FA13", "FA14", "FA1F", "FA21", "FA23", "FA24", "FA27", "FA28", "FA29"] #﨎﨏﨑﨓﨔﨟﨡﨣﨤﨧﨨﨩
gbk_compatibility_deci_list_hex=["F92C", "F979", "F995", "F9E7", "F9F1", "FA0C", "FA0D", "FA18", "FA20"] #郎凉秊裏隣兀嗀礼蘒
for item in cjk_compatibility_list_hex:
    gbk_compatibility_deci_list.append(deci(item))
    cjk_compatibility_ideographs_deci_list.append(deci(item))
for item in gbk_compatibility_deci_list_hex:
    gbk_compatibility_deci_list.append(deci(item))

#get cjk encoding character list from txt files - will do when imported on start
cjk_dict = {}
cjk_char_count = {}
for encoding in global_var.cjk_list:
    #gb18030 no file list, obsolete gbk file list
    if encoding == "gb18030" or encoding == "gbk":
        continue
    cjk_dict[encoding] = load_sample_file(encoding+"-han.txt")
    cjk_char_count[encoding]=0
