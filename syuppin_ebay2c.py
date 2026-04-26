# marketシートの各列を元に、ループ
# 各行の詳細コメントは、syp_ebay2b.pyにある。

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

    # [EMAIL_MASKED]@gmail.com       73466.0     incense burner
    # [EMAIL_MASKED]@gmail.com       73466.0     tea ceremony
    # [EMAIL_MASKED]@gmail.com          73466.0     buddhist copper
    # [EMAIL_MASKED]@gmail.com          73466.0     buddhist altar
    # [EMAIL_MASKED]@gmail.com          73466.0     buddhist art
    # [EMAIL_MASKED]@gmail.com        73466.0     kanzashi hairpin
    # [EMAIL_MASKED]@gmail.com       73466.0     lacquer ware
    # [EMAIL_MASKED]@gmail.com          73466.0     bell
    # [EMAIL_MASKED]@gmail.com       73466.0     sculpture
    # [EMAIL_MASKED]@gmail.com      38125.0     painting scroll
    # [EMAIL_MASKED]@gmail.com       38126.0     prints
    # [EMAIL_MASKED]@gmail.com          37935.0     bowls
    # ? 66841.0 katana
    # [EMAIL_MASKED]@gmail.com   1345.0      shingeki no kyojin
    # [EMAIL_MASKED]@gmail.com         13666.0     dragon ball
    # [EMAIL_MASKED]@gmail.com        158671.0    batman
    # [EMAIL_MASKED]@gmail.com        158671.0    spiderman
    # [EMAIL_MASKED]@gmail.com        17085.0     x-men
    # [EMAIL_MASKED]@gmail.com        158671.0    x-men
    # [EMAIL_MASKED]@gmail.com        158671.0    avengers
    # [EMAIL_MASKED]@gmail.com       75708.0     star wars

    # id_list = ['[EMAIL_MASKED]@gmail.com',
    #            '[EMAIL_MASKED]@gmail.com',
    #            '[EMAIL_MASKED]@gmail.com',
    #            '[EMAIL_MASKED]@gmail.com',
    #            '[EMAIL_MASKED]@gmail.com',
    #
    #            '[EMAIL_MASKED]@gmail.com',
    #            '[EMAIL_MASKED]@gmail.com',
    #            '[EMAIL_MASKED]@gmail.com',
    #            '[EMAIL_MASKED]@gmail.com',
    #            '[EMAIL_MASKED]@gmail.com',
    #
    #            '[EMAIL_MASKED]@gmail.com',
    #            '[EMAIL_MASKED]@gmail.com',
    #
    #            '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', # サスペンド
    #
    #            '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
    #            '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
    #            '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
    #            '[EMAIL_MASKED]@gmail.com']

    # mBall_yahooと同じ、Market シート（今はSQLのテーブルだが）から、
    # atk = r"C:/Users/[USERNAME_MASKED]/Desktop/00.Myself/04.Buyer/1.利益計算/AtackList_Buyer43.xlsx"
    # 検索キーは、後の間を＋にする必要があるが、これエクセルの時点でやるか、ここでやるか> planner では空白で複合キーを生成するので、変更はここで
    df_market = pd.read_excel(atk, 'market', skiprows=2).dropna(subset=['キーフレーズ']).\
        drop_duplicates(['id', 'main key', 'categ num']) # キーフレーズ列のNan を消して表示
        # 重複削除. Groupbyの必要はない https://stackoverflow.com/questions/51865187/remove-duplicated-rows-in-groupby
    # df_market.to_excel(atk, sheet_name='出品前', index=False) # 出品前、なんてシートないのだが

    id_list = df_market.loc[:, 'id']
    mainKey_list = df_market.loc[:, 'main key']
    categNum_list = df_market.loc[:, 'categ num'] # CategNum  にしてた。つまり動くわけないし、２ｃは前回動かしたものじゃないということ

    # IDでマージ > 複数のmain keyとCategNum をリストに格納, としたいとこだが、要らないkeyもあるよね

    for id, categNum, mainKey in list(zip(id_list, categNum_list, mainKey_list)): # [:2]
        print(id, categNum, mainKey)
        syp(atk, id, categNum, mainKey) # Selenium でCSV ダウンロード




def syp(atk, id, categ, mainkey):


    # 利益4000円以上、販売価格5万以内のフィルタ。Cancel時は 8万超えたら
    # アクセス数を優先している。ウォッチ書いても書かなくても結果は同じ    # 0以外の値がある行に絞る https://stackoverflow.com/questions/50593621/pandas-sort-value-and-ignore-0
    df = pd.read_excel(atk, sheet_name='清書_詳細', index=None) \
        .sort_values(['watch', 'access'], ascending=[True, False]) # watchは1つでもあれば、トップの方へ
    # これは即決価格列の、0ではない値を持つ行に絞る＞0なら排除＝即決価格がある品のみに絞っている
    df = df[df['即決価格_y'] != 0].drop(['watch', 'access', '即決価格_y'], axis=1)
        # .query('カテゴリ in {categ} and mainkey in {mainkey)'.format(categ, mainkey))
    df = df[df['カテゴリ'].isin([categ])] # categ に値する数値がある行のみ絞る
    df = df[df['mainkey'].isin([mainkey])].query('開始価格 <= 500') # .iloc[50:]# 15行目から

    # ここも2bと違う. Main関数の最後にCateg番号をループでSyp()に渡しているのに、なぜ再びリスト作る？
    # カテ番が下記リストの数値である行の状態を空白にするのか。2bではカテゴリ列の4つの数値の行は、全て””空白にしてる
    # antiqueは状態を非表示に or = |
    categnum_list = [73466, 38125, 38126, 37935, 37937, 162978, 162976, 66841, 37940, 162973,
                  162969, 37939, 162977, 37938, 37936, 162975, 155353]
    for categnum in categnum_list:
        df.loc[df['Category'] == categnum, '状態_y'] = '' # これ何？
    # if df['カテゴリ'] == 73466 or 38125 or 38126 or 37935: # antiqueは状態非表示に
    #     df['状態'] = ''
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