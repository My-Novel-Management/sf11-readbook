# -*- coding: utf-8 -*-
"""Main story.
"""
## path setting
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
## public libs
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## assets
from storybuilder.assets import basic, accessory
## settings
from config import PERSONS, AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS, RUBIS, LAYERS
## local files
from episodes.ghostworld import ep_ghostworld
from episodes.oldlibrary import ep_old_library
from episodes.truth import ep_truth
from episodes.waitinggirl import ep_waiting_girl


## define alias
W = Writer
_ = Writer.getWho()

################################################################
#
# Sample step:
# 1) Create the world
#       世界を作成する。
# 2) Create a new chapter
#       章の作成。
# 3) Create a episode
#       エピソード作成。
# 4) Create a new scene
#       シーン作成。物語のベース。ここに様々なActionを追加する。
# 5) Create a new stage
#       舞台作成。シーンに必須要素
# 6) Create a new day and time
#       日時作成。シーンのサブ要素
# 7) Add a scene plot
#       シーンプロットの作成。概要のないシーンは原則使えない
# 8) Add scene actions
#       シーンアクションの追加。
#
################################################################


## main
def ch_main(w: World):
    return w.chapter("main",
            ep_ghostworld(w),
            ep_old_library(w),
            ep_waiting_girl(w),
            ep_truth(w),
            )

def create_world():
    """Create a world.
    """
    w = World("滅びた世界で、本を読む")
    w.setCommonData()
    w.setAssets(basic.ASSET)
    w.setAssets(accessory.ASSET)
    w.buildDB(PERSONS,
            AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS,
            RUBIS, LAYERS)
    w.setBaseDate(2108)
    w.setBaseArea("Jakarta")
    w.setColumnRow(42,34)
    # set textures
    # w.entryBlock()
    # w.entryHistory()
    # w.entryLifeNote()
    w.setOutline("滅びた世界で、調査していた")
    return w


def main(): # pragma: no cover
    w = create_world()
    return w.build(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

