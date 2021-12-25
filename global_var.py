global cjk_list
global unicode_list

global cjk_jian_list
global cjk_jian_fan_list
global cjk_fan_list

global cjk_count
global unicode_count

import os, sys
global main_directory

#if packaged by pyinstaller
#ref: https://stackoverflow.com/questions/404744/determining-application-path-in-a-python-exe-generated-by-pyinstaller
if getattr(sys, 'frozen', False):
    #change from loading same folder to full folder, --onedir
    main_directory = os.path.dirname(sys.executable)
    #`pyinstaller --onefile` change to use the following code
    #if '_MEIPASS2' in os.environ:
    #    main_directory = os.environ['_MEIPASS2']
    #ref: https://stackoverflow.com/questions/9553262/pyinstaller-ioerror-errno-2-no-such-file-or-directory
else:
    #dev mode
    try: #py xx.py
        app_full_path = os.path.realpath(__file__)
        main_directory = os.path.dirname(app_full_path)
    except NameError: #py then run code
        main_directory = os.getcwd()


#english name
#old list for compatibility
cjk_list = {"gb2312":"GB/T 2312",
            "gb12345":"GB/T 12345",
            "gbk":"GBK",
            "gb18030":"GB 18030",
            "hanyi-jianfan":"Hanyi Fonts Simp./Trad. List",
            "fangzheng-jianfan":"FounderType Simp./Trad. List",
            "tongyong-guifan":"Table of General Standard Chinese Characters", #通用规范汉字表
            "3500changyong":"List of Frequently Used Characters in Modern Chinese", #现代汉语常用字表
            "7000tongyong":"List of Commonly Used Characters in Modern Chinese", #现代汉语通用字表
            "yiwu-jiaoyu":"List of Frequently Used Characters of Compulsory Education", #义务教育语文课程常用字表
            "4808changyong":"Chart of Standard Forms of Common National Characters", #常用国字标准字体表
            "6343cichangyong":"Chart of Standard Forms of Less-Than-Common National Characters", #次常用国字标准字体表
            "big5changyong":"BIG5 Common Character Set",
            "big5":"BIG5",
            "hkchangyong":"List of Graphemes of Commonly-Used Chinese Characters", #常用字字形表
            "hkscs":"Hong Kong Supplementary Character Set",
            "suppchara":"Common Supplementary Characters in Hong Kong (Level 1-6)"
           }
cjk_jian_list_en = {"gb2312":"GB/T 2312",
                 "3500changyong":"List of Frequently Used Characters in Modern Chinese",
                 "7000tongyong":"List of Commonly Used Characters in Modern Chinese",
                 "yiwu-jiaoyu":"List of Frequently Used Characters of Compulsory Education",
                 "tongyong-guifan":"Table of General Standard Chinese Characters"
                }
cjk_jian_fan_list_en = {"hanyi-jianfan":"Hanyi Fonts Simp./Trad. List",
                     "fangzheng-jianfan":"FounderType Simp./Trad. List",
                     "gbk":"GBK",
                     "gb18030":"GB 18030"
                    }
cjk_fan_list_en = {"4808changyong":"Chart of Standard Forms of Common National Characters",
                "6343cichangyong":"Chart of Standard Forms of Less-Than-Common National Characters",
                "big5changyong":"BIG5 Common Character Set",
                "big5":"BIG5",
                "hkchangyong":"List of Graphemes of Commonly-Used Chinese Characters",
                "hkscs":"Hong Kong Supplementary Character Set",
                "suppchara":"Common Supplementary Characters in Hong Kong (Level 1-6)",
                "gb12345":"GB/T 12345"
               }
unicode_list = {"kangxi":"Kangxi Radicals",
                "kangxi-sup":"CJK Radical Supplements",
                "zero":"〇",
                "basic":"CJK Unified Ideographs",
                "ext-a":"CJK Unified Ideographs Extension A",
                "compat":"CJK Compatibility Ideographs",
                "compat-ideo":"  Non-Compatibility (Unified) Ideographs",
                "ext-b":"CJK Unified Ideographs Extension B",
                "ext-c":"CJK Unified Ideographs Extension C",
                "ext-d":"CJK Unified Ideographs Extension D",
                "ext-e":"CJK Unified Ideographs Extension E",
                "ext-f":"CJK Unified Ideographs Extension F",
                "compat-sup":"CJK Compatibility Ideographs Supplement",
                "ext-g":"CJK Unified Ideographs Extension G",
                "total":"Total Ideographs"
                }

#chinese name (simp)
cjk_jian_list_zhs = {"gb2312":"GB/T 2312",
                 "3500changyong":"现代汉语常用字表＊",
                 "7000tongyong":"现代汉语通用字表",
                 "yiwu-jiaoyu":"义务教育语文课程常用字表",
                 "tongyong-guifan":"通用规范汉字表"
                }
cjk_jian_fan_list_zhs = {"hanyi-jianfan":"汉仪简繁字表",
                     "fangzheng-jianfan":"方正简繁字表",
                     "gbk":"GBK",
                     "gb18030":"GB 18030"
                    }
cjk_fan_list_zhs = {"4808changyong":"常用国字标准字体表",
                "6343cichangyong":"次常用国字标准字体表",
                "big5changyong":"五大码 (Big5) 常用汉字表",
                "big5":"五大码 (Big5)",
                "hkchangyong":"常用字字形表",
                "hkscs":"香港增补字符集 (HKSCS)",
                "suppchara":"常用香港外字表 (1-6级)",
                "gb12345":"GB/T 12345"
               }
unicode_list_zhs = {"kangxi":"康熙部首",
                "kangxi-sup":"汉字部首补充",
                "zero":"〇",
                "basic":"中日韩统一表意文字",
                "ext-a":"中日韩统一表意文字—扩展A区",
                "compat":"中日韩兼容表意文字",
                "compat-ideo":"　非兼容（统一）表意文字",
                "ext-b":"中日韩统一表意文字—扩展B区",
                "ext-c":"中日韩统一表意文字—扩展C区",
                "ext-d":"中日韩统一表意文字—扩展D区",
                "ext-e":"中日韩统一表意文字—扩展E区",
                "ext-f":"中日韩统一表意文字—扩展F区",
                "compat-sup":"中日韩兼容表意文字（补充区）",
                "ext-g":"中日韩统一表意文字—扩展G区",
                "total":"总汉字数"
                }

#chinese name (trad)
cjk_fan_list_zht = {"4808changyong":"常用國字標準字體表",
                "6343cichangyong":"次常用國字標準字體表",
                "big5changyong":"五大碼 (Big5) 常用漢字表",
                "big5":"五大碼 (Big5)",
                "hkchangyong":"常用字字形表",
                "hkscs":"香港增補字符集 (HKSCS)",
                "suppchara":"常用香港外字表 (1-6級)",
                "gb12345":"GB/T 12345"
               }
cjk_jian_fan_list_zht = {"hanyi-jianfan":"漢儀簡繁字表",
                     "fangzheng-jianfan":"方正簡繁字表",
                     "gbk":"GBK",
                     "gb18030":"GB 18030"
                    }
cjk_jian_list_zht = {"gb2312":"GB/T 2312",
                 "3500changyong":"現代漢語常用字表",
                 "7000tongyong":"現代漢語通用字表",
                 "yiwu-jiaoyu":"義務教育語文課程常用字表",
                 "tongyong-guifan":"通用規範漢字表"
                }
unicode_list_zht = {"kangxi":"康熙部首",
                "kangxi-sup":"漢字部首補充",
                "zero":"〇",
                "basic":"中日韓統一表意文字",
                "ext-a":"中日韓統一表意文字—擴展A區",
                "compat":"中日韓兼容表意文字",
                "compat-ideo":"　非兼容（統一）表意文字",
                "ext-b":"中日韓統一表意文字—擴展B區",
                "ext-c":"中日韓統一表意文字—擴展C區",
                "ext-d":"中日韓統一表意文字—擴展D區",
                "ext-e":"中日韓統一表意文字—擴展E區",
                "ext-f":"中日韓統一表意文字—擴展F區",
                "compat-sup":"中日韓兼容表意文字（補充區）",
                "ext-g":"中日韓統一表意文字—擴展G區",
                "total":"總漢字數"
                }


#character count
cjk_count = {"gb2312":6763,
            "gb12345":6866,
            "gbk":20923,
            "gb18030":0,
            "hanyi-jianfan":9169,
            "fangzheng-jianfan":9664,
            "tongyong-guifan":8105,
            "3500changyong":3500,
            "7000tongyong":7000,
            "yiwu-jiaoyu":3500,
            "4808changyong":4808,
            "6343cichangyong":6343,
            "big5changyong":5401,
            "big5":13060,
            "hkchangyong":4825,
            "hkscs":4603,
            "suppchara":1097
           }
unicode_count = {"kangxi":214,
                "kangxi-sup":115,
                "zero":1,
                "basic":20992,
                "ext-a":6592,
                "compat":472,
                "compat-ideo":12,
                "ext-b":42720,
                "ext-c":4153,
                "ext-d":222,
                "ext-e":5762,
                "ext-f":7473,
                "compat-sup":542,
                "ext-g":4939,
                "total":0
                }
cjk_count["gb18030"] = unicode_count["zero"]+unicode_count["basic"]+unicode_count["ext-a"]
unicode_count["total"] = unicode_count["zero"]+unicode_count["compat-ideo"]+unicode_count["basic"]+unicode_count["ext-a"]+unicode_count["ext-b"]+unicode_count["ext-c"]+unicode_count["ext-d"]+unicode_count["ext-e"]+unicode_count["ext-f"]+unicode_count["ext-g"]