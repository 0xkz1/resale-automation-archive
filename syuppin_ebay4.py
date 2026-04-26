# 2021年。エクセルの清書シートをPandas に置き換える途中。さらに、SQLを使って完全体
# ４の手前は3ではなく、2だった。2・2ｂ・2ｃがあるが 。。
# syp_eB.ipynb を見てみろ

# 2020年までのメモ
# 清書シートの整形をこのファイルで. pandas を使う
# 各アカ、カテゴリで分けて、清書シートをカテゴリでソート（ピボットテーブル？）したのをCSVにして、提出


import os
import pandas as pd
import shutil
import time
import xlwings as xw
from xlwings.constants import AutoFillType
from selenium.common.exceptions import NoSuchElementException
from string import ascii_lowercase
import itertools

import os
current_dir = os.getcwd()


def main(atk):
    # 清書シートのオートフィル
    app = xw.App(visible=False)
    wb = app.books.open(atk)
    # 清書シートはどの列も終わりの行数が分からないので、入力用シートのA列の最下行を取得、その数字を清書のRangeに代入
    sht1 = wb.sheets['入力用']  # (1)にしていたが
    sht2 = wb.sheets['清書_詳細']
    lastRow1 = sht1.range('A4').end(-4121).row


    # これをPythonで代替するので、コメントアウトせよ
    # app.books.open("C:/Users/[USERNAME_MASKED]/AppData/Roaming/Microsoft/Excel/XLSTART/PERSONAL.XLSB")
    # macro = app.macro('PERSONAL.XLSB!AutoFilterAdvanced_RedNumber_tenki2')
    # macro()

    # アルファベットをbreak指定の番までカウントし続ける　
    def iter_all_strings():  # https://stackoverflow.com/questions/29351492/how-to-make-a-continuous-alphabetic-list-python-from-a-z-then-from-aa-ab-ac-e
        for size in itertools.count(1):
            for s in itertools.product(ascii_lowercase, repeat=size):
                yield "".join(s)

    for col in iter_all_strings():
        # print(col)
        # sht2.range('{}2:{}3'.format(col, col)).api.AutoFill(
        #     sht2.range("{}3:{}{}".format(col, col, lastRow1)).api, AutoFillType.xlFillDefault)
        sht2.range('{}2'.format(col)).api.AutoFill(
            sht2.range("{}2:{}{}".format(col, col, lastRow1)).api, AutoFillType.xlFillDefault)
        time.sleep(0.2)
        if col == 'bp':  # 小文字にすること
            break

    wb.save()
    app.kill()

    id_list = ['[EMAIL_MASKED]@gmail.com',
                '[EMAIL_MASKED]@gmail.com',
                '[EMAIL_MASKED]@gmail.com',
                '[EMAIL_MASKED]@gmail.com',
                '[EMAIL_MASKED]@gmail.com',

                '[EMAIL_MASKED]@gmail.com',
                '[EMAIL_MASKED]@gmail.com',
                '[EMAIL_MASKED]@gmail.com',
                '[EMAIL_MASKED]@gmail.com',
                '[EMAIL_MASKED]@gmail.com',

                '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', # サスペンド

                '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
                '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
                '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
                '[EMAIL_MASKED]@gmail.com']
    categ_list = [[13666], # 0
                    [1345],      # 1345 Legend of the Galactic Heroes
                    [158671],    # 13666 dragonball
                    [75708],     # star wars  >> 75708
                    [73466],     #  other antique
                    [38125], # 5 # 38125> painting scroll
                    [38126],     # 38126 prints
                    [37935],     # 37935 bowls
                    [],

                    [66841],    # 刀のパーツ。刀は駄目 価格帯下げても刃物出てくる
                    [32749],     #32749 marvel doujinshi
                    [73466], # 9     73466= many genre 二度目。15品目から入れた

                    ] # ここの数字がない場合でも問題なく動く
# figure
    # 1345	shingeki no kyojin
    # 1345	Legend of the Galactic Heroes
    # 1345	zoids
    # 1345	transformerのプラモデルとか
    # 13666	dragonball

# figure, comic, marvel
    # 32749	marvel doujinshi これSuperheroの番号。
    # 158671 Comic Book Hero Action Figures
        # 17076	batman
        # 17082	spiderman
        # 17085	x-men >> 34254
        # 17085	spawn
        # 17079	avengers
        # 32750	star wars  >> 75708

        # 32762	superman
        # 17084	wolverine
        # 32767	incredible huk
        # 32757	deadpool
        # 32768	wonder woman

# antique
    # 73466	incense burner, tea ceremony, buddhist仏,  kanzashi, lacquer ware漆塗り, samurai, bell, art, sculpture #色々ジャンル
    # 38125	painting scroll
    # 38126	prints
    # 37935	bowls

    # 37937	glasses     # ここからは未開拓
    # 162976 tea caddies
    # 66841	katana
    # 37940	vases
    # 162973	statues
    # 162969	armor
    # 37939	plates
    # 162977	teapots
    # 37938	netsuke
    # 37936	boxes
    # 162975	masks
    # 155353	kimonos & textiles

    # 多くのキーを持つカテゴリの中で、いくつかに絞りたい時に
    mainkey_list = ['shingeki no kyojin', 'kimetsu no yaiba', # 1345
                    'incense burner', 'tea ceremony',
                    'buddhist art', 'buddhist alter', 'buddhist copper',
                    'kanzashi hairpin', 'lacquer ware',
                    'samurai', 'bell', 'art', 'sculpture',
                    '',''] # other antique

    for id, categ in list(zip(id_list, categ_list))[7:9]: #8]: #　id_list[3:11], categ_list[3:]
        print(id, categ)
         # print(atk)
        if categ == 1345: #
            mainkey = mainkey_list[0]
        elif categ == 73466: #antique
            mainkey = mainkey_list[0]
        elif duplicate(categ == 73466: # ２回めの73466の時、どう変えられるか
            xxx = "test"

        syp(atk, id, categ, mainkey) # Selenium でCSV ダウンロード





def syp(atk, id, categ, mainkey):
    # 利益4000円以上、販売価格5万以内のフィルタ。Cancel時は 8万超えたら
    # アクセス数を優先している。ウォッチ書いても書かなくても結果は同じ    # 0以外の値がある行に絞る https://stackoverflow.com/questions/50593621/pandas-sort-value-and-ignore-0
    df = pd.read_excel(atk, sheet_name='清書_詳細', index=None)\
        .sort_values(['watch', 'access'], ascending=[True, False]) # watchは1つでもあれば、トップの方へ
    df = df[df['即決価格_y'] != 0].drop(['watch', 'access', '即決価格_y'], axis=1)
    df = df[df['カテゴリ'].isin([categ])]
    df = df[df['mainkey'].isin([mainkey])].query('開始価格 <= 500')
    # print(df)

    # pandasで清書DF つくる
    df = pd.read_excel(atk, sheet_name='Sheet1', skiprows=2, index=None,
                       usecols=['Category', 'SKU', 'title', #'説明',
                                '画像1', '画像2', '画像3', '画像4', '画像5', '画像6', '画像7',
                                '最高売値', '即決価格_y', '状態_y', '送料設定', '営業利益', '利益率']).\
        query('営業利益 >= 700 and 利益率 >= 8 and 最高売値 <= 50000').drop(['営業利益', '利益率'], axis=1).\
        sort_values(['watch', 'access'], ascending=[True, False])
    df[df['即決価格_y'] != 0, df['Category'].isin(categ)].drop(['即決価格_y'], axis=1) #.\
    df['最高売値'] /= 100
             # 即決価格がある品に絞るが、毎時間FixCanかけられるようになったら、絞るのやめる
             # loc[:, ['Category', 'SKU', 'title', '説明',
             #         '画像1', '画像2', '画像3', '画像4', '画像5', '画像6', '画像7',
             #         '最高売値', '状態_y', '送料設定']] # 'kg(after)',
    # 各カテゴリごとに内容が変わる列＞ 商品説明、状態、
    # 状態を番号に
    df = df.replace({'状態_y': {' 新品 ': 1000, ' 未使用 ': 1000, ' 未使用に近い ': 3000, ' 中古 ': 3000,
                                ' 目立った傷や汚れなし ': 3000, ' やや傷や汚れあり ': 3000, ' 傷や汚れあり ': 3000}})
    # antiqueは状態を非表示に or = |
    categ_list = [73466, 38125, 38126, 37935, 37937, 162978, 162976, 66841, 37940, 162973,
                  162969, 37939, 162977, 37938, 37936, 162975, 155353]
    for categ in categ_list:
        df.loc[df['Category'] == categ, '状態_y'] = ''
    # df.loc[(df['Category'] == 73466) | (df['Category'] == 38125)
    #         | (df['Category'] == 38126) | (df['Category'] == 37935), '状態_y'] = ''

    # 説明　英訳説明は desc にする。リミット額内に収まる出品予定枠に入ったら、英訳する
    # desc_frame = ['desc_book', # 本
    #              'BBB', # フィギュア
    #              'CCC', # アンティーク
    #              ]
    # paymentPolicy = '' # これを後のformat で代入する
    # shipPolicy = ''
    if categ == 2222: # "本"のカテ番
        著者 = df['著者']
        with open('desc_book.txt', ) as f:
            s = f.read()
            # タイトルと紹介文は要らない
            # 全てのreplace を一つのformatで置き換えられる
            s.format(著者) #,paymentPolicy)　これは共通の説明パートにすればいい、formatに入れるのはそのカテゴリ固有の
            # 本の詳細情報は、説明文に組み込まなくていい
            # desc_frame[0].format(replace("タイトルと紹介文", concat(入力用!D4, "<br><br>", 入力用!D4, "<br><br>", 入力用!F4, "<br>")).\
            # replace("ページ数", 入力用!AI4).replace("出版社", 入力用!AJ4).replace("言語", 入力用!AH4).replace("ISBN10コード", 入力用!Z4).\
            # replace("ISBN13コード", 入力用!AA4).replace("eBay製品コード", 入力用!AB4).replace("製品ディメンション", 入力用!AC4).\
            # replace("重さ", 入力用!AD5).replace("著者", 入力用!AK4).replace("ジャンル", 入力用!AL4).replace("出版国", 入力用!AM4).\
            # .replace("サブジェクト", 入力用!AN4).replace("発行日", 入力用!AO4)
    elif categ == 1111:
            with open('desc_antique.txt', ) as f:
                s = f.read()
            s.format("説明文", 入力用!D4).df['説明'] #これは 説明列の全行だから、一行ずつにして


    df.column = ['カテゴリ', 'SKU', 'タイトル', '商品説明',
                 '画像1', '画像2', '画像3', '画像4', '画像5', '画像6', '画像7',
                 '開始価格', '状態', '配送方法ポリシー']  # 清書用の列名に変更 # 不要な列名があるとエラー起きるならこれ必要
    print(df)


    # まだ途中
    # 清書にのみ存在する列と値を作る. 清書読み込んで横に Mergeする？ オートフィル対象の列は、関数を
    df_auc = pd.DataFrame({'サイトID': '', '商品数': 1, '決済方法ポリシー': , '返品ポリシー', '入札制限ポリシー',
                           '出品形式', '商品発送元の地域', '商品発送元の国', '開始日時', '期間', '通貨'})
        # 下記は、各列の値
        ['0.5~0.8kg', '支払い設定１','返品設定１（セラー負担）', '' ,'fixed', 'Sapporo', 'JP', 'GTC', 'USD']

    concat = pd.concat([df, df_auc], axis=1)

    # dfの行数に合わせて、df_auc の行数を増やし、値を入れる



    print('出品予定の品数 ' + str(len(df)))

    # csv_auc = r'C:/Users/[USERNAME_MASKED]\Desktop\00.Myself\04.Buyer\2.出品\syuppin_auc\syuppin_ebay%s.csv'
    csv_auc = f"{current_dir}\syuppin_auc\syuppin_ebay%s.csv"
    i = 0
    # renbanName = csv_auc % i
    while os.path.exists(csv_auc % i):
        i += 1
    with open(csv_auc % i, mode="w", newline="", encoding="utf-8_sig") as f:
        df.to_csv(f) #, index=False, encoding='cp932')

    # sypUp(csv_auc % i, id) # 下の定義関数は過去の記録として置いておく
    # なぜ3からインポートするのか。ここに入れてしまったら？
    import syuppin_ebay3 as syp
    syp.sypUp(csv_auc % i, id)



# def 一つのカテゴリを復数アカで






if __name__ == '__main__':
    # atk = r"C:/Users/[USERNAME_MASKED]/Desktop/00.Myself/04.Buyer/1.利益計算/AtackList_Buyer43.xlsx"
    # atk = f"{current_dir}\AtackList_Buyer43.xlsx"
    connection_config = {
        'host': '[DB_HOST_MASKED]',
        'database': '[DB_NAME_MASKED]',
        'user': '[DB_USER_MASKED]',
        'port': '5432',
        'password': '[DB_PASSWORD_MASKED]'
    }
    global engine
    engine = create_engine(
        'postgres://[DB_USER_MASKED]:[DB_PASSWORD_MASKED]@[DB_HOST_MASKED]:5432/[DB_NAME_MASKED]'.
            format(**connection_config))

    atk = pd.read_sql('atklist4', con=engine)
    main(atk)