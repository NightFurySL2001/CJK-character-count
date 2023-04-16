Made by NightFurySL2001 / 夜煞之乐2001
Released under MIT License
Copyright © 2020-2023 NFSL2001

2023-04-13 v0.20
Major optimization on code: OpenType limit 65k is possible to be done in <5sec
Add output to text file feature with -r/--report option in command line

2022-09-13 v0.17
Add IICore (deprecated standard in Unicode)
Update GB 18030 to follow GB 18030-2022 range: Basic, Compatibility ideograph and Ext-A to Ext-F (pseudo-standard before this, total count still incorrect due to newly added character at the end of Basic, Ext-A, Ext-B and Ext-C)
Update suppchara to version 1.8 (2022/09/06)
Unicode 15.0 newly added characters Ext-C, newly added block Ext-H

2021-12-25 v0.16
Add List of Graphemes of Commonly-Used Chinese Characters (Hong Kong)
Fix drag and drop fail for fonts outside of program folder

2021-09-24 v0.15.1
Emergency patch: Unicode 14.0 newly added characters in Basic, Ext-B and Ext-C

2021-09-16 v0.15
Officially released under MIT License
Fix text files for BIG5, Table of Standard Form of Commonly Used National Characters
Add Table of Standard Form of Less Commonly Used National Characters (removed in v0.10), FounderType Simp/Trad, Hanyi Simp/Trad list, non-compatible Unified Ideographs, total ideograph count
Add progress bar when counting
Changed "Unicode Sectors" to "Unicode Blocks", same for Chinese interface
Shrink font size (TODO: variable font size)
Support for drag file onto .exe file to start counting automatically (i.e. accepting parameters as `main.exe font.ttf`)

2020-10-03 v0.11
Add TTC processing
Add more vigorous checking of font file
Fix range bug
More complete localization of Chinese interface
Localization of Chinese (Traditional) interface
Change English interface to the same as Chinese because list too long

2020-09-24 v0.10
Taiwan Cichangyong removed due to lack of standard character table
Xiandai Hanyu Tongyong Zibiao, Yiwu Jiaoyu Zibiao, BIG5 Common Character Set added
Source of 3500 Changyong Zibiao renamed to Xiandai Hanyu Changyong Zibiao
Taiwan Changyong renamed to Table of Standard Form of Commonly Used National Characters
Fixed errors in HKSCS
Add U+3007 Ideographic Number Zero Unicode Character to Unicode list
Reset count to 0 if new font loaded
Increased Chinese interface font size
Rename -chi to -zhs (Simplified)
Created logo

2020-06-23 v0.04
Taiwan Changyong, Cichangyong added
Refactor loops to decrease loops
Source of 3500 Changyong Zibiao checked, may rename to Xiandai Hanyu Changyong Zibiao
Official name to CJK-character-count

2020-04-30 v0.03
3500 Changyong Zibiao added

2020-04-20 v0.02
main-chi.py included, Chinese (Simplified) interface

2020-04-16 v0.01
Update program to include CJK Ext. G range, refactor loops to decrease loops