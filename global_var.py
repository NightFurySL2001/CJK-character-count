global cjk_list
global unicode_list
global cjk_count
global unicode_count
global cjk_jian_list
global cjk_jian_fan_list
global cjk_fan_list
global unicode_cn_list


#english name
cjk_list = {"gb2312":"GB/T 2312",
            "gb12345":"GB/T 12345",
            "gbk":"GBK",
            "gb18030":"GB 18030",
            "tongyong-guifan":"通用规范汉字表",
            "3500changyong":"3500 字常用汉字表",
            "4808changyong":"台湾教育部常用字",
            "6341cichangyong":"台湾教育部次常用字",
            "big5":"五大码",
            "hkscs":"香港增补字符集"
           }
unicode_list = {"kangxi":"Kangxi Radicals",
                "kangxi-sup":"CJK Radical Supplements",
                "basic":"CJK Unified Ideographs",
                "ext-a":"CJK Unified Ideographs Extension A",
                "compat":"CJK Compatibility Ideographs",
                "ext-b":"CJK Unified Ideographs Extension B",
                "ext-c":"CJK Unified Ideographs Extension C",
                "ext-d":"CJK Unified Ideographs Extension D",
                "ext-e":"CJK Unified Ideographs Extension E",
                "ext-f":"CJK Unified Ideographs Extension F",
                "compat-sup":"CJK Compatibility Ideographs Supplement",
                "ext-g":"CJK Unified Ideographs Extension G"
                }

#character count
cjk_count = {"gb2312":6763,
            "gb12345":6866,
            "gbk":20923,
            "gb18030":27581,
            "tongyong-guifan":8105,
            "3500changyong":3500,
            "4808changyong":4808,
            "6341cichangyong":6341,
            "big5":13058,
            "hkscs":4640
           }
unicode_count = {"kangxi":214,
                "kangxi-sup":115,
                "basic":20989,
                "ext-a":6592,
                "compat":472,
                "ext-b":42718,
                "ext-c":4149,
                "ext-d":222,
                "ext-e":5762,
                "ext-f":7473,
                "compat-sup":542,
                "ext-g":4939
                }

#chinese name
cjk_jian_list = {"gb2312":"GB/T 2312",
                 "3500changyong":"3500 字常用汉字表",
                 "tongyong-guifan":"通用规范汉字表"
                }
cjk_jian_fan_list = {"gbk":"GBK",
                     "gb18030":"GB 18030"
                    }
cjk_fan_list = {"4808changyong":"台湾教育部常用字",
                "6341cichangyong":"台湾教育部次常用字",
                "gb12345":"GB/T 12345",
                "big5":"五大码 (Big5)",
                "hkscs":"香港增补字符集 (HKSCS)"
               }
unicode_cn_list = {"kangxi":"康熙部首",
                "kangxi-sup":"汉字部首补充",
                "basic":"中日韩统一表意文字",
                "ext-a":"中日韩统一表意文字—扩展A区",
                "compat":"中日韩兼容表意文字",
                "ext-b":"中日韩统一表意文字—扩展B区",
                "ext-c":"中日韩统一表意文字—扩展C区",
                "ext-d":"中日韩统一表意文字—扩展D区",
                "ext-e":"中日韩统一表意文字—扩展E区",
                "ext-f":"中日韩统一表意文字—扩展F区",
                "compat-sup":"中日韩兼容表意文字（补充区）",
                "ext-g":"中日韩统一表意文字—扩展G区"
                }