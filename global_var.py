import sys
from typing import cast, TypedDict
from pathlib import Path
from enum import StrEnum
import frontmatter
from unicode_blocks.blocks import (
    IDEO_BLOCKS,
    CJK_UNIFIED_IDEOGRAPHS,
    CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A,
)
from unicode_blocks.unicodeBlock import UnicodeBlock

# if packaged by pyinstaller
# ref: https://stackoverflow.com/questions/404744/determining-application-path-in-a-python-exe-generated-by-pyinstaller
if getattr(sys, "frozen", False):
    # change from loading same folder to full folder, --onedir
    main_directory = Path(sys.executable).parent
    # `pyinstaller --onefile` change to use the following code
    # if '_MEIPASS2' in os.environ:
    #    main_directory = os.environ['_MEIPASS2']
    # ref: https://stackoverflow.com/questions/9553262/pyinstaller-ioerror-errno-2-no-such-file-or-directory
else:
    # dev mode
    try:  # py xx.py
        app_full_path = Path(__file__).resolve()
        main_directory = app_full_path.parent
    except NameError:  # py then run code
        main_directory = Path.cwd()


class DisplayLanguage(StrEnum):
    EN = "en"
    ZHS = "zhs"
    ZHT = "zht"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    def display_name(self):
        if self == self.EN:
            return "English"
        elif self == self.ZHS:
            return "简体中文"
        elif self == self.ZHT:
            return "正體（繁体）中文"
        else:
            return "Unknown"


class CJKGroup(StrEnum):
    JIAN = "jian"
    JIANFAN = "jianfan"
    FAN = "fan"

class FontMatterNames(TypedDict):
    en: str
    zhs: str
    zht: str


class FrontMatterMetadata(TypedDict):
    name: FontMatterNames
    cjk_group: str
    count: int


class CJKTable:
    def __init__(
        self, id: str, localised_names: FontMatterNames, cjk_group: CJKGroup, characters: set[str]
    ):
        self.id = id
        self.localised_names = localised_names
        self.cjk_group = cjk_group
        self.characters = characters

    @property
    def count(self) -> int:
        return len(self.characters)

    def localised_name(self, lang: DisplayLanguage) -> str:
        return self.localised_names.get(
            lang,
            self.localised_names.get(
                DisplayLanguage.EN,
            ),
        )

    def get_overlap(self, other: set[str]) -> set[str]:
        return self.characters.intersection(other)

    def get_diff(self, other: set[str]) -> set[str]:
        return self.characters.difference(other)

    @staticmethod
    def load(filename: Path) -> "CJKTable":
        id = filename.stem.removesuffix("-han")
        with open(filename, "r", encoding="utf-8-sig") as f:
            raw_metadata, content = frontmatter.parse(f.read())
            metadata: FrontMatterMetadata = cast(FrontMatterMetadata, raw_metadata)
            characters = set(map(str.strip, content.strip().splitlines()))
            try:
                localised_names: FontMatterNames = metadata["name"]
                cjk_group: str = metadata["cjk_group"]
            except KeyError:
                localised_names = cast(
                    FontMatterNames,
                    {lang: filename.stem for lang in DisplayLanguage},
                )
                cjk_group = "unknown"
            try:
                count: int = metadata["count"]
            except KeyError:
                count = len(characters)
            except TypeError:
                count = len(characters)
            assert count == len(
                characters
            ), f"Character count mismatch in {filename}: metadata count {count} vs actual count {len(characters)}"

            return CJKTable(id, localised_names, CJKGroup(cjk_group), characters)


def char_range(start: int, end: int) -> range:
    """Generate a range that includes the end value."""
    return range(start, end + 1)

    # normal range: range(0,5) --> [0,1,2,3,4], len(range(0,5))=5
    # character detect range: char_range(0,5) --> [0,1,2,3,4,5], len(char_range(0,5))=6


cjk_compatibility_ideographs_list = [
    0xFA0E,
    0xFA0F,
    0xFA11,
    0xFA13,
    0xFA14,
    0xFA1F,
    0xFA21,
    0xFA23,
    0xFA24,
    0xFA27,
    0xFA28,
    0xFA29,
]  # 﨎﨏﨑﨓﨔﨟﨡﨣﨤﨧﨨﨩
gbk_compatibility_list = cjk_compatibility_ideographs_list + [
    0xF92C,
    0xF979,
    0xF995,
    0xF9E7,
    0xF9F1,
    0xFA0C,
    0xFA0D,
    0xFA18,
    0xFA20,
]  # 郎凉秊裏隣兀嗀礼蘒

# special unicode blocks
CJK_ZERO_BLOCK = UnicodeBlock(
    "〇",
    ord("〇"),
    ord("〇"),
    assigned_ranges=[(ord("〇"), ord("〇"))],
)

CJK_NON_COMPATIBILITY_IDEOGRAPHS = UnicodeBlock(
    "  Non-Compatibility (Unified) Ideographs",
    cjk_compatibility_ideographs_list[0],
    cjk_compatibility_ideographs_list[-1],
    assigned_ranges=[
        (char_code, char_code) for char_code in cjk_compatibility_ideographs_list
    ],
)


# special GB encodings
GBK = CJKTable(
    "gbk",
    {
        DisplayLanguage.EN: "GBK",
        DisplayLanguage.ZHS: "GBK",
        DisplayLanguage.ZHT: "GBK",
    },
    CJKGroup.JIANFAN,
    (
        set("〇")
        | set(chr(i) for i in char_range(0x4E00, 0x9FA5))
        | set(chr(i) for i in gbk_compatibility_list)
    ),
)


class GB18030(CJKTable):
    def __init__(self):
        self.id = "gb18030"
        self.localised_names = {
            DisplayLanguage.EN: "GB18030",
            DisplayLanguage.ZHS: "GB18030",
            DisplayLanguage.ZHT: "GB18030",
        }
        self.cjk_group = CJKGroup.JIANFAN

    @property
    def count(self) -> int:
        return (
            len(CJK_ZERO_BLOCK)
            + len(CJK_UNIFIED_IDEOGRAPHS)
            + len(CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A)
            + len(CJK_NON_COMPATIBILITY_IDEOGRAPHS)
        )

    def get_overlap(self, other: set[str]) -> set[str]:
        result = set()
        for char in other:
            if (
                char in CJK_ZERO_BLOCK.assigned_ranges
                or char in CJK_UNIFIED_IDEOGRAPHS.assigned_ranges
                or char in CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A.assigned_ranges
                or char in CJK_NON_COMPATIBILITY_IDEOGRAPHS.assigned_ranges
            ):
                result.add(char)
        return result

    def get_diff(self, other: set[str]) -> set[str]:
        in_set = self.get_overlap(other)
        return other.difference(in_set)


class DisplayCJKTablesList:
    table_list: dict[str, dict[str, CJKTable]] = {
        CJKGroup.JIAN: {},
        CJKGroup.JIANFAN: {"gbk": GBK, "gb18030": GB18030()},
        CJKGroup.FAN: {},
    }

    predefined_order = {
        CJKGroup.JIAN: [
            "gb2312",
            "3500changyong",
            "7000tongyong",
            "yiwu-jiaoyu",
            "tongyong-guifan",
        ],
        CJKGroup.JIANFAN: [
            "hanyi-jianfan",
            "fangzheng-jianfan",
            "iicore",
            "gbk",
            "gb18030",
        ],
        CJKGroup.FAN: [
            "4808changyong",
            "6343cichangyong",
            "big5",
            "big5changyong",
            "jf7000-core",
            "hkchangyong",
            "hkscs",
            "suppchara",
            "gb12345",
            "gujiyinshua"
        ],
    }

    for table_file in (main_directory / "cjk-tables").glob("*-han.txt"):
        table = CJKTable.load(table_file)
        table_list[table.cjk_group][table.id] = table

    @classmethod
    def get_ordered_tables_in_group(cls, group: CJKGroup) -> dict[str, CJKTable]:
        # order by predefined order
        ordered_tables = {}
        for table_id in cls.predefined_order[group]:
            if table_id in cls.table_list[group]:
                ordered_tables[table_id] = cls.table_list[group][table_id]
        # add any other tables not in predefined order to allow extensions from user file
        for table_id, table in cls.table_list[group].items():
            if table_id not in ordered_tables:
                ordered_tables[table_id] = table
        return ordered_tables

    @classmethod
    def get_all_tables(cls) -> dict[str, CJKTable]:
        all_tables = {}
        for group in CJKGroup:
            all_tables.update(cls.get_ordered_tables_in_group(group))
        return all_tables


class DisplayUnicodeBlocksList:
    block_list: dict[str, UnicodeBlock] = {
        "ZERO": CJK_ZERO_BLOCK,
        "__NON_COMPATIBILITY_(UNIFIED)_IDEOGRAPHS": CJK_NON_COMPATIBILITY_IDEOGRAPHS,
    }

    predefined_order = [
        "KANGXI_RADICALS",
        "CJK_RADICALS_SUPPLEMENT",
        "ZERO",
        "CJK_UNIFIED_IDEOGRAPHS",
        "CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A",
    ]

    total_assigned_ranges = [
        *CJK_ZERO_BLOCK.assigned_ranges.ranges,
        *CJK_NON_COMPATIBILITY_IDEOGRAPHS.assigned_ranges.ranges,
    ]
    for block in IDEO_BLOCKS:
        block_list[block.variable_name] = block
        if (
            block.variable_name == "CJK_UNIFIED_IDEOGRAPHS"
            or block.variable_name.startswith("CJK_UNIFIED_IDEOGRAPHS_EXTENSION_")
        ):
            total_assigned_ranges.extend(block.assigned_ranges.ranges)

    TOTAL_BLOCK = UnicodeBlock(
        "Total",
        0xF0000,
        0x10FFFF,
        assigned_ranges=total_assigned_ranges,
    )  # dummy block for total count

    @classmethod
    def get_ordered_blocks(cls) -> dict[str, UnicodeBlock]:
        # order by predefined order
        ordered_blocks = {}
        for block_id in cls.predefined_order:
            if block_id in cls.block_list:
                ordered_blocks[block_id] = cls.block_list[block_id]
        # add any other blocks not in predefined order to allow automatic updates
        for block_id, block in sorted(cls.block_list.items(), key=lambda item: item[1]):
            if block_id not in ordered_blocks:
                ordered_blocks[block_id] = block

        # final total block
        ordered_blocks["total"] = cls.TOTAL_BLOCK
        return ordered_blocks
