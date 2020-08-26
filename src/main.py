#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
# from scenes import xxx
from episodes import e1_ghostworld
from episodes import e2_oldlibrary
from episodes import e3_waitinggirl
from episodes import e4_truth


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8
#   4. Spec
#   5. Plot         - 1/4
#   6. Scenes
#   7. Conte        - 1/2
#   8. Layout
#   9. Draft        - 1/1
#
################################################################

# Constant
TITLE = "滅びた世界で、本を読む"
MAJOR, MINOR, MICRO = 2, 1, 0
COPY = "全てが滅びた世界でも、人は本を読む"
ONELINE = "約18000字のSF短編。全てが滅んだ世界を記録する記録士と相棒のロボ犬の物語"
OUTLINE = "すべてが滅んだ世界で、それでもまだ人類が生き延びる為に調査をしている「記録士」と呼ばれる存在がいた。その一人であるユーリィは相棒の記録用犬型ドローン「クド」と共に未登録地区を探して旅をしていた。その最中、本が残っている図書館を発見する"
THEME = "本を読む、という行為"
GENRE = "SF／ヒューマンドラマ"
TARGET = "20-40years"
SIZE = "電撃サイズで50枚"
CONTEST_INFO = "創元SF短編賞一次突破作品を改稿し、電撃小説大賞に応募。一次落選"
CAUTION = ""
NOTE = "元々のオリジナルはエブリスタの妄想コンテストに応募した8000字のSF短編です"
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
TAGS = ["SF", "ロボット", "犬", "本", "記録", "図書館"]
RELEASED = (8, 25, 2020)


# Chapters
def ch_main(w: World):
    return w.chapter("main",
            e1_ghostworld.ep_ghostworld(w),
            e2_oldlibrary.ep_old_library(w),
            e3_waitinggirl.ep_waiting_girl(w),
            e4_truth.ep_truth(w),
            )


# Main
# NOTE: 電撃サイズは42x34
def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_taginfos(*TAGS)
    w.config.set_released(*RELEASED)
    return w.run(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

