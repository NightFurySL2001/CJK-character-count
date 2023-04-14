![Banner of CJK-character-count](resource/banner.png)
# CJK-character-count

This is a program that counts the amount of CJK characters based on Unicode ranges and Chinese encoding standards.

此软件以统一码（Unicode）区块与汉字编码标准统计字体内的汉字数量。

**[Download here. 在此下载。](https://github.com/NightFurySL2001/CJK-character-count/releases)**

___

## How this works 如何运作

This program accepts 1 font file at a time (OpenType/TrueType single font file currently) and extract the character list from `cmap` table, which records the Unicode (base-10)-glyph shape for a font. The list is then parsed to count the amount of characters based on Unicode ranges (comparing the hexadecimal range) and Chinese encoding standards (given a list of .txt files with the actual character in it).

此软件可计算一套字体内的汉字数量，目前只限OpenType/TrueType单字体文件而已。导入字体时，软件将从`cmap`表（储存字体内（十进制）统一码与字符对应的表）提取汉字列表，然后以该列表依统一码区块（比对十六进制码位）与汉字编码标准（比对 .txt文件）统计字体内的汉字数量。

## Currently supported font formats 支援的字体格式

Major font formats are supported in this software.

主要字体格式本软件皆都支援。

` *.ttf, *.otf, *.woff, *.woff2, *.ttc, *.otc`

## Software interface 软件界面

`main.exe` is the English version, `main-zhs.exe` is the Chinese (Simplified) version, `main-zht.exe` is the Chinese (Traditional) version.

`main.exe` 为英文版，`main-zhs.exe` 为简体中文版，`main-zht.exe` 为繁体中文版。

<img src="https://raw.githubusercontent.com/NightFurySL2001/CJK-character-count/master/resource/jf-openhuninn-sample-en.png" width="500" >

<img src="https://raw.githubusercontent.com/NightFurySL2001/CJK-character-count/master/resource/jf-openhuninn-sample-zhs.png" width="500" >

<img src="https://raw.githubusercontent.com/NightFurySL2001/CJK-character-count/master/resource/jf-openhuninn-sample-zht.png" width="500" >

## Currently supported encoding standard/standardization list 支援的编码标准／汉字表

Details of the character lists can be found in https://github.com/NightFurySL2001/cjktables.  
字表详情可参见 https://github.com/NightFurySL2001/cjktables 。

### Encoding standard 编码标准
* [GB/T 2312](https://en.wikipedia.org/wiki/GB_2312)

* [GB/T 12345](https://zh.wikipedia.org/wiki/GB_12345)  
  \**Note: Source file from [character_set](https://gitlab.com/mrhso/character_set/-/blob/master/GB12345.txt) by @mrhso.  
  注：字表来源为 @mrhso [character_set](https://gitlab.com/mrhso/character_set/-/blob/master/GB12345.txt)。*

* [GBK](https://en.wikipedia.org/wiki/GBK_(character_encoding))  
  \**Note: Private Use Area (PUA) characters are removed and not counted, resulting in 20923 characters.  
  注：不计算私用区（PUA）字符，共计20923字。*

* [GB 18030](https://en.wikipedia.org/wiki/GB_18030)  
  \**According to latest GB 18030-2022, level 3 support includes all CJK characters in Unicode up until Extension F, including the 12 "compatibility" ideographs in the CJK compatibility block. New additions appended to end of CJK Ideographs Basic block, Extension A, B and C are counted although not existing in GB 18030-2022.*   
  依据最新 GB 18030-2022，第三级支援包括全部中日韩汉字直至扩展 F 区，包括兼容汉字区的 12 个“兼容”汉字。中日韩汉字基本区、扩展 A、B、C 区后面新增的字符虽然并未在 GB 18030-2022内，但是在本软件中已计入*

* [BIG5/五大码](https://en.wikipedia.org/wiki/Big5)

* [BIG  5 Common Character Set/五大码常用汉字表](https://en.wikipedia.org/wiki/Big5)

* [Hong Kong Supplementary Character Set (HKSCS)/香港增补字符集](https://en.wikipedia.org/wiki/Hong_Kong_Supplementary_Character_Set)

* [IICore/国际表意文字核心](https://appsrv.cse.cuhk.edu.hk/~irg/irg/IICore/IICore.htm)（Deprecated/已废除）

### Standardization list 汉字表

* [List of Frequently Used Characters in Modern Chinese/现代汉语常用字表](https://zh.wiktionary.org/wiki/Appendix:%E7%8E%B0%E4%BB%A3%E6%B1%89%E8%AF%AD%E5%B8%B8%E7%94%A8%E5%AD%97%E8%A1%A8)  
  \**Note: Old name in this software was 3500 Commonly Used Chinese Characters.  
  注：旧版软件内名称为《3500字常用汉字表》。*

* [List of Commonly Used Characters in Modern Chinese/现代汉语通用字表](https://zh.wiktionary.org/wiki/Appendix:%E7%8E%B0%E4%BB%A3%E6%B1%89%E8%AF%AD%E9%80%9A%E7%94%A8%E5%AD%97%E8%A1%A8)

* [Table of General Standard Chinese Characters/通用规范汉字表](https://en.wikipedia.org/wiki/Table_of_General_Standard_Chinese_Characters)

* [List of Frequently Used Characters of Compulsory Education/义务教育语文课程常用字表](https://old.pep.com.cn/xiaoyu/jiaoshi/tbjx/kbjd/kb2011/201202/t20120206_1099050.htm)

* [Chart of Standard Forms of Common National Characters/常用國字標準字體表](https://zh.wikipedia.org/wiki/%E5%B8%B8%E7%94%A8%E5%9C%8B%E5%AD%97%E6%A8%99%E6%BA%96%E5%AD%97%E9%AB%94%E8%A1%A8)  
  \**Note: Old name in this software was 《台湾教育部常用字表》.  
  注：旧版软件内名称为《台湾教育部常用字表》。*
  
* [Chart of Standard Forms of Less-Than-Common National Characters/次常用國字標準字體表](https://zh.wikipedia.org/wiki/%E5%B8%B8%E7%94%A8%E5%9C%8B%E5%AD%97%E6%A8%99%E6%BA%96%E5%AD%97%E9%AB%94%E8%A1%A8)  
  \**Note: Old name in this software was 《台湾教育部次常用字表》, and was temporarily removed in v0.10 and v0.11.  
  注：旧版软件内名称为《台湾教育部次常用字表》，并于 0.10 版和 0.11 版暂时移除。*

* [List of Graphemes of Commonly-used Chinese Characters/常用字字形表](https://zh.wikipedia.org/wiki/%E5%B8%B8%E7%94%A8%E5%AD%97%E5%AD%97%E5%BD%A2%E8%A1%A8)  

* [Hong Kong Supplementary Character Set/香港增補字符集](https://zh.wikipedia.org/wiki/%E9%A6%99%E6%B8%AF%E5%A2%9E%E8%A3%9C%E5%AD%97%E7%AC%A6%E9%9B%86)  

* [Supplementary Character Set (suppchara, level 1-6)/常用香港外字表（1-6级）](https://github.com/ichitenfont/suppchara)  

### Foundry list 厂商字表

* [Hanyi Fonts Simp./Trad. List/汉仪简繁字表](https://github.com/3type/glyphs-han/blob/master/Tables/Commonly%20Used%20on%20Internet.txt)  

* FounderType  Simp./Trad. List 方正简繁字表

## Dependencies 依赖模块

* `tkinter`  
  For software display. Should be removed and replaced in next version.  
  使用于软件显示。应在未来移除与替换该模块。

* [`fontTools`](https://github.com/fonttools/fonttools)  
  Extract `cmap` table.  
  提取 `cmap` 表。

* [`pyglet`](http://pyglet.org/)  
  ZHT only: Set the GUI Font to custom font ([Genyog](https://github.com/buttaiwan/genyog-font)).  
  繁中版：设置界面字体为自定义字体（[源样黑体](https://github.com/buttaiwan/genyog-font)）。

* [`pyinstaller`](https://github.com/pyinstaller/pyinstaller)  
  Build executable for Windows in [release](https://github.com/NightFurySL2001/CJK-character-count/releases/latest).  
  编译软件成可执行软件。[发布版](https://github.com/NightFurySL2001/CJK-character-count/releases/latest)内提供 Windows 版本。
  
##  License 授权

This software is licensed under [MIT License](https://opensource.org/licenses/MIT). Details of the license can be found in the [accompanying `LICENSE` file](LICENSE).

本软件以 [MIT 授权条款](https://opensource.org/licenses/MIT)发布。授权详情可在[随附的 `LICENSE` 文件内](LICENSE)查阅。

## To build 如何构建

Please install [latest version of Python 3](https://www.python.org/downloads/).

请先安装[最新版本的 Python 3](https://www.python.org/downloads/)。

### Dependencies 安装依赖模块
```
pip3 install fonttools
pip3 install pyglet
pip3 install pyinstaller
```

### Building software 构建软件

Download the required `.spec` files from [release](https://github.com/NightFurySL2001/CJK-character-count/releases/latest).

请从[发布页](https://github.com/NightFurySL2001/CJK-character-count/releases/latest)下载需要的 `.spec` 文件。
```
// To build single language
pyinstaller main.spec
pyinstaller main-zhs.spec
pyinstaller main-zht.spec

// To build full folder, use the provided .bat file
.\build.bat
```

## To-do 待办事项

* Redesign GUI with [Kivy](https://kivy.org/).

## Changelog 更新日志

Refer to [readme.txt](readme.txt). 参考[readme.txt](readme.txt)。

___

This program is requested by [MaoKen](http://www.maoken.com/). Visit their site to see this in action.

此软件由[猫啃网](http://www.maoken.com/)要求。浏览该网址以查看使用方式。
