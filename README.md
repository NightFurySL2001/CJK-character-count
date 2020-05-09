# CJK-character-count

This is a program that counts the amount of CJK characters based on Unicode ranges and Chinese encoding standards.

此软件以统一码（Unicode）区块与汉字编码标准统计字体内的汉字数量。

___

## How this works 如何运作

This program accepts 1 font file at a time (OpenType/TrueType single font file currently) and extract the character list from `cmap` table, which records the Unicode (base-10)-glyph shape for a font. The list is then parsed to count the amount of characters based on Unicode ranges (comparing the hexadecimal range) and Chinese encoding standards (given a list of .txt files with the actual character in it).

此软件可计算一套字体内的汉字数量，目前只限OpenType/TrueType单字体文件而已。导入字体时，软件将从`cmap`表（储存字体内（十进制）统一码与字符对应的表）提取汉字列表，然后以该列表依统一码区块（比对十六进制码位）与汉字编码标准（比对 .txt文件）统计字体内的汉字数量。

## Currently supported encoding standard/standardization list 支援的编码标准／汉字表
* [GB/T 2312](https://en.wikipedia.org/wiki/GB_2312)
* [GB/T 12345](https://zh.wikipedia.org/wiki/GB_12345)
* [GBK](https://en.wikipedia.org/wiki/GBK_(character_encoding)) 

  \**Note: Private Use Area (PUA) characters are removed and not counted, resulting in 20923 characters. 
  注：不计算私用区（PUA）字符，共计20923字。*

* [GB 18030](https://en.wikipedia.org/wiki/GB_18030)

  \**Note: Mandatory section are counted only. According to GB 18030, mandatory section of a font is all CJK characters in the Basic Multilingual Plane e.g. CJK Unified Ideographs and CJK Unified Ideographs Extension A. 
  注：只计算强制性标准部分。依据GB 18030，字体内强制需要支援的字符范围应该是基本多文种平面（BMP）内的所有汉字，即中日韩统一表意文字与中日韩统一表意文字扩展A区。*

* [Table of General Standard Chinese Characters/通用规范汉字表](https://en.wikipedia.org/wiki/Table_of_General_Standard_Chinese_Characters)
* [3500 Commonly Used Chinese Characters/3500字常用汉字表](https://github.com/kaienfr/Font/blob/master/learnfiles/%E5%B8%B8%E7%94%A8%E6%B1%89%E5%AD%97%E5%BA%93%203500.txt)

  \**Important: Source is not yet determined, may be renamed or removed in future. 
  注：未知来源，可能在未来重命名或移除。*

* [Big5/五大码](https://en.wikipedia.org/wiki/Big5)
* [Hong Kong Supplementary Character Set (HKSCS)/香港增补字符集](https://en.wikipedia.org/wiki/Hong_Kong_Supplementary_Character_Set)

## Software interface 软件界面

`main.exe` is the English version, `main-chi.exe` is the modified Chinese version.

`main.exe` 为英文版，`main-chi.exe` 为中文版。

![IPAmj English Sample](resource/ipamjm.ttf-sample-en.jpg?raw=true| width=350)
![IPAmj Chinese Sample](resource/ipamjm.ttf-sample-zh.jpg?raw=true| width=350)

## Dependencies 依赖模块

* `tkinter` 

  For software display. Non-commercial use module, should be removed and replaced in next version. 使用于软件显示。非商用模块，应在未来移除与替换该模块。
* [`fontTools`](https://github.com/fonttools/fonttools)

  Extract `cmap` table. 提取 `cmap` 表。
* [`pyinstaller`](https://github.com/pyinstaller/pyinstaller)

  Build executable for Windows in [release](https://github.com/NightFurySL2001/CJK-character-count/releases/latest). 编译软件成可执行软件。于[发布版](https://github.com/NightFurySL2001/CJK-character-count/releases/latest)内提供 Windows 版本。

## Changelog 更新日志

Refer to [readme.txt](readme.txt). 参考[readme.txt](readme.txt)。

___

This program is requested by [MaoKen](http://www.maoken.com/). Visit their site to see this in action.

此软件由[猫啃网](http://www.maoken.com/)要求。浏览该网址以查看使用方式。
