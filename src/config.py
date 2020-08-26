# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
        ("yuri", "ユーリィ", "コマロフ,ユーリィ", 24, (1,1), "male", "アーカイバ", "me:ボク"),
        ("kudo", "クド", "クドリャフカ", 5, (1,1), "male", "記録用ドローン", "me:ワタシ"),
        ("jas", "ジャスミン", "チェン,ジャスミン", 20, (1,1), "female", "図書館司書", "me:わたし"),
        ("rina", "リーナ", "", 20, (1,1), "female", "図書館司書", "me:わたし"),
        ("chen", "チェン", "チェン,ジャスミン", 30, (7,7), "female", "宇宙飛行士", "me:私"),
        ("andre", "アンドレ", "ヤン,アンドレ", 40, (1,1), "male", "宇宙飛行士", "me:私"),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
        ("Jakarta", "ジャカルタ", "", (10684,-620)),
        ("library", "図書館", "Jakarta"),
        ("highschool", "高校", "Jakarta"),
        ("classroom", "教室", "Jakarta"),
        ("mosque", "モスク", "Jakarta"),
        ("street", "路上", "Jakarta"),
            ),
        "DAYS": (
            # (tag / name / month / day / year)
        ("endday", "月落下事変", 7,7, 2098),
        ("visittown", "シティ訪問日", 11,29, 2108),
        ("voyagetown", "旅立つ日", 12,1, 2108),
            ),
        "TIMES": (
            # (tag / name / hour / minute)
            ),
        "ITEMS": (
            # (tag / name / cate / info)
            ),
        "WORDS": (
            # (tag / name / cate / info)
        ("energy", "エネルギィ"),
        ("archiver", "記録士"),
        ("cemargur", "セマルグル", "special", "記録士を管理する中央機関"),
        ("ghost", "霊的回路現象"),
        ("walpurgis", "ヴァルプルギスの火"),
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ("嘲笑", "｜嘲笑《ちょうしょう》", ("嘲笑う",)),
            ("記録士", "｜記録士《アーカイバ》"),
            ("自律機械", "｜自律機械《ドローン》",),
            ("躊躇", "｜躊躇《ちゅうちょ》", ("躊躇わ",)),
            ("そんなもしもを", "そんな｜もしも《イフ》を"),
            ("Terima kasih", "｜Terima kasih《テリマカシ》"),
            ("苔", "｜苔《こけ》"),
            ("跳ぶ", "｜跳《と》ぶ"),
            ("濁った", "濁《にご》った"),
            ("嘲笑う", "｜嘲笑《あざわら》う"),
            ("塞が", "塞《ふさ》が"),
            ("竦める", "｜竦《すく》める"),
            ("麓の", "｜麓《ふもと》の"),
            ("躊躇われた", "｜躊躇《ためら》われた"),
            ("昂り", "｜昂《たかぶ》り"),
            ("淀み", "｜淀《よど》み"),
            ),
        }

