
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



def main(atk):
    # 清書シートのオートフィル
    app = xw.App(visible=False)
    wb = app.books.open(atk)
    # 清書シートはどの列も終わりの行数が分からないので、入力用シートのA列の最下行を取得、その数字を清書のRangeに代入
    sht1 = wb.sheets['入力用']  # (1)にしていたが
    sht2 = wb.sheets['清書_詳細']
    lastRow1 = sht1.range('A4').end(-4121).row

    app.books.open("C:/Users/[USERNAME_MASKED]/AppData/Roaming/Microsoft/Excel/XLSTART/PERSONAL.XLSB")
    macro = app.macro('PERSONAL.XLSB!AutoFilterAdvanced_RedNumber_tenki2')
    macro()
    # nextRow1 = lastRow1 + 1
    # lastRow2 = sht2.range('AZ4').end(-4121).row  # ATK 状態列＝AZの最下行
    # nextRow2 = lastRow2 + 1
    # my_values = sht1.range('H1:H{}'.format(str(lastRow1))).options(ndim=2).value  # lwr_cell2を、wb1の方に書いてどうする。。半日気付けなかった
    # sht2.range('AV4').value = my_values


    # 清書シートの2行目から求めた最下行までオートフィル
    # 1, 2行目を選択、オートフィル、これmBall_yahooでは１行しか選択していないが、重量列が数字繰り上がってない。
    # ここでも一行でいいのでは
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
    # col_list = ['A', 'D', 'E', 'J', 'K', 'L', 'M', 'AH', 'AI', 'AJ', 'AU', 'AY', 'BK', 'BL', 'BM', 'BN', 'BO', 'BP',
    #             'BQ', 'BR', 'BS', 'BT', 'BU', 'BV', 'BW', 'BX']
    # for col in col_list:  # DEG がタイトル関連、YZが重量、　ADが見込売値, AU~AYがヤフオク、 BK以降は利益計算
    #     sht2.range('{}2:{}3'.format(col, col)).api.AutoFill(
    #         sht2.range("{}3:{}{}".format(col, col, lastRow1)).api, AutoFillType.xlFillDefault)
    wb.save()
    app.kill()

    # 2ｃでは、MarketシートからID・カテ番・メインキーワードを一括で取得する。ここではわざわざ手入力でリストを作っている
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

               '[EMAIL_MASKED]@gmail.com',
               '[EMAIL_MASKED]@gmail.com',
                
               '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', # サスペンド

               '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
               '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
               '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
               '[EMAIL_MASKED]@gmail.com']
    categ_list = [[13666], # 0
                  [1345],      # 1345	Legend of the Galactic Heroes
                  [158671],    # 13666	dragonball
                  [75708],     # star wars  >> 75708
                  [73466],     #  other antique

                  [38125], # 5 # 38125> painting scroll
                  [38126],     # 38126	prints
                  [37935],     # 37935	bowls
                  [],

                  [66841],    # 刀のパーツ。刀は駄目 価格帯下げても刃物出てくる
                  [32749],     #32749	marvel doujinshi
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
                    ['incense burner', 'tea ceremony'],         # 73466
                    ['buddhist art', 'buddhist alter', 'buddhist copper'],
                    'kanzashi hairpin', 'lacquer ware',
                    'samurai', 'bell', 'art', 'sculpture',
                    '',''] # other antique

    for id, categ in list(zip(id_list, categ_list))[:1]: #[7:9]: #8]: #　id_list[3:11], categ_list[3:]
        print(id, categ)
         # print(atk)
        if categ == 1345: #
            mainkey = mainkey_list[0] # 2択
        elif categ == 73466: #antique
            # for maink in mainkey_list[2:]:
            #     mainkey = maink # mainkey_list[2]
        # duplicateを見つけ、if それに当たったら
        elif categ == 73466: # again: # ２回めの73466の時、どう変えられるか
            mainkey = mainkey_list[3]
        else:
            mainkey == '' #lambda # mainkey を使わない, 何も無いことを表現＞ Lambda?
        syp(atk, id, categ, mainkey) # Selenium でCSV ダウンロード



def syp(atk, id, categ, mainkey):
    # カテゴリ
    # category_list = ['13666', '2222']
    # フィギュアの中でも、ジャンル別で番号あるから、結構リスト増える。
    # リスト作らなくていいかも
    # if id == id_list[0]:
    #     categ = '13666' #  & '2211'
    # elif id == id_list[1]:
    #     categ = '222'
    # categ、数値を' ' で囲むとキーエラー起こるかも

    # 利益4000円以上、販売価格5万以内のフィルタ。Cancel時は 8万超えたら
    # アクセス数を優先している。ウォッチ書いても書かなくても結果は同じ    # 0以外の値がある行に絞る https://stackoverflow.com/questions/50593621/pandas-sort-value-and-ignore-0
    df = pd.read_excel(atk, sheet_name='清書_詳細', index=None) \
        .sort_values(['watch', 'access'], ascending=[True, False]) # watchは1つでもあれば、トップの方へ
    df = df[df['即決価格_y'] != 0].drop(['watch', 'access', '即決価格_y'], axis=1)
    df = df[df['カテゴリ'].isin([categ])]
    df = df[df['mainkey'].isin([mainkey])].query('開始価格 <= 500')# .iloc[50:]# 15行目から


    if df['カテゴリ'] == 73466 or 38125 or 38126 or 37935: # antiqueは状態非表示に
        df['状態'] = ''

    print(df)

    # 1000ドル以下に絞る
    # カテゴリ列の categ の値のみに絞る。isin以外にも queryが使えそうだった # https://note.nkmk.me/python-pandas-query/
    # print(df2)  # categ_groupby = df.groupby('カテゴリ').get_group(categ) # categには、各々のカテゴリ番号が入る
    # df2 = df.loc('カテゴリ', categ)
    # df をloc やiloc で、列指定はできるが、　値で絞ることは出来るか > iloc
    # 清書からフィルタするから、値は「フィギア、本」ではなく、「13666, 」だよ
    # 更に、ウォッチとアクセス（列をつくり、）数が多い順に並べ、その２列を非表示にしたものを、to_csvする
    # 上から出品されるので、上から優先zド高い品に並べる


    print('出品予定の品数 ' + str(len(df)))

    csv_auc = r'C:/Users/[USERNAME_MASKED]\Desktop\00.Myself\04.Buyer\2.出品\syuppin_auc\syuppin_ebay%s.csv'
    i = 0
    # renbanName = csv_auc % i
    while os.path.exists(csv_auc % i):
        i += 1
    with open(csv_auc % i, mode="w", newline="", encoding="utf-8_sig") as f:
        df.to_csv(f) #, index=False, encoding='cp932')

    # sypUp(csv_auc % i, id) # 下の定義関数は過去の記録として置いておく
    import syuppin_ebay3 as syp
    syp.sypUp(csv_auc % i, id)


# def 一つのカテゴリを復数アカで



if __name__ == '__main__':
    atk = r"C:/Users/[USERNAME_MASKED]/Desktop/00.Myself/04.Buyer/1.利益計算/AtackList_Buyer43.xlsx"
    main(atk)