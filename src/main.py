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
from episodes.e1_ghostworld import ep_ghostworld
from episodes.e2_oldlibrary import ep_old_library
from episodes.e3_waitinggirl import ep_waiting_girl
from episodes.e4_truth import ep_truth


## define alias
W = Writer
_ = Writer.getWho()

################################################################
#
#   1. 滅びた世界
#   2. 図書館の女性
#   3. 待つこと
#   4. 記録士の仕事
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

