import global_var
import os

#special cjk compatibility for gbk
global gbk_compatibility_list
global cjk_compatibility_ideographs_list
#definition of gbk_compatibility_list and cjk_compatibility_ideographs_list, require deci(number)
cjk_compatibility_ideographs_list = [
    0xFA0E, 0xFA0F, 0xFA11, 0xFA13, 0xFA14, 0xFA1F, 0xFA21, 0xFA23, 0xFA24, 0xFA27, 0xFA28, 0xFA29
] #﨎﨏﨑﨓﨔﨟﨡﨣﨤﨧﨨﨩
gbk_compatibility_list = cjk_compatibility_ideographs_list + [
    0xF92C, 0xF979, 0xF995, 0xF9E7, 0xF9F1, 0xFA0C, 0xFA0D, 0xFA18, 0xFA20
] #郎凉秊裏隣兀嗀礼蘒


# input:char_list iterable
# output:tuple of number 
def count_char(char_list):
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

            #compatibility but unified ideographs, use cjk_compatibility_ideographs_list
            if range == "compat" and row in cjk_compatibility_ideographs_list:
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
                    if row in char_range(0x4E00, 0x9FA5) or row in gbk_compatibility_list:
                        cjk_char_count[encoding]+=1
                    continue
                #see if in cjk encoding
                if char in cjk_dict[encoding]:
                    cjk_char_count[encoding]+=1

        #if already saw, skip it
        continue

    # add zero to gbk
    cjk_char_count["gbk"]+=unicode_char_count["zero"]
    #gb18030 mandatory CJK Unified Ideographs and CJK Unified Ideographs Extension A
    cjk_char_count["gb18030"]=unicode_char_count["basic"]+unicode_char_count["ext-a"]+unicode_char_count["zero"]
    
    #sum up total cjk unified ideographs
    unicode_char_count["total"] = unicode_char_count["zero"]+unicode_char_count["basic"]+unicode_char_count["compat-ideo"]+sum([
        y for x,y in unicode_char_count.items() if x.startswith("ext-")
    ])

    return (cjk_char_count, unicode_char_count)



#load encoding file
def load_sample_file(filename):
    font_list = []
    full_path = os.path.join(global_var.main_directory, filename)
    for line in open(full_path, "r", encoding="utf-8"):
        font_list.append(line.strip("\r\n").strip(" "))
    return set(font_list)

# special check range function as python default range don't include ending number
def char_range(start, end):
    return range(start, end+1)
# normal range: range(0,5) --> [0,1,2,3,4], len(range(0,5))=5
# character detect range: char_range(0,5) --> [0,1,2,3,4,5], len(char_range(0,5))=6

#check range of character:
def uni_range_check(char_base10):
    cjk_blocks_list = global_var.unicode_block_range

    #filter unicode
    for block_name, (start, end) in cjk_blocks_list.items():
        if char_base10 in char_range(start, end):
            return block_name

#get cjk encoding character list from txt files - will do when imported on start
cjk_dict = {}
cjk_char_count = {}
for encoding in global_var.cjk_list:
    #gb18030 no file list, obsolete gbk file list
    if encoding == "gb18030" or encoding == "gbk":
        continue
    cjk_dict[encoding] = load_sample_file(encoding+"-han.txt")
    cjk_char_count[encoding]=0
