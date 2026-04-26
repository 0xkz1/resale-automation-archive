
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
    id_list = ['[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
               '[EMAIL_MASKED]@gmail.com','[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
               '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
               '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
               '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
               '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
               '[EMAIL_MASKED]@gmail.com']
    categ_list = [[13666], [1345], [17076, 17082],
                  [17085, 17079, 32749, 32750], [73466], [38125],
                  [38126], [37935], [37937],
                  [66841]] # ここの数字がない場合でも問題なく動く
    # 1345	shingeki no kyojin
    # 1345	Legend of the Galactic Heroes
    # 1345	zoids
    # 1345	transformerのプラモデルとか
    # 13666	dragonball

    # 32749	marvel doujinshi
    # 17076	batman
    # 17082	spiderman
    # 17085	x-men
    # 17085	spawn
    # 17079	avengers
    # 32750	star wars
    # 32762	superman
    # 17084	wolverine
    # 32767	incredible huk
    # 32757	deadpool
    # 32768	wonder woman

    # 73466	incense burner
    # 38125	painting scroll
    # 38126	prints
    # 37935	bowls
    # 37937	glasses
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

    for id, categ in zip(id_list[3:11], categ_list[3:]): #　id_list[3:11], categ_list[3:]
        print(id, categ)
         # print(atk)
        syp(atk, id, categ) # Selenium でCSV ダウンロード


def syp(at, id, categ):
    # 清書シートのオートフィル
    app = xw.App(visible=False)
    wb = app.books.open(at)
    # 清書シートはどの列も終わりの行数が分からないので、入力用シートのA列の最下行を取得、その数字を清書のRangeに代入
    sht1 = wb.sheets['入力用']  # (1)にしていたが
    sht2 = wb.sheets['清書_詳細']
    lastRow1 = sht1.range('A4').end(-4121).row
    # nextRow1 = lastRow1 + 1
    # lastRow2 = sht2.range('AZ4').end(-4121).row  # ATK 状態列＝AZの最下行
    # nextRow2 = lastRow2 + 1
    # my_values = sht1.range('H1:H{}'.format(str(lastRow1))).options(ndim=2).value  # lwr_cell2を、wb1の方に書いてどうする。。半日気付けなかった
    # sht2.range('AV4').value = my_values

    # 1, 2行目を選択、オートフィル、これmBall_yahooでは１行しか選択していないが、重量列が数字繰り上がってない。
    # ここでも一行でいいのでは
    # アルファベットをbreak指定の番までカウントし続ける　
    def iter_all_strings(): # https://stackoverflow.com/questions/29351492/how-to-make-a-continuous-alphabetic-list-python-from-a-z-then-from-aa-ab-ac-e
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
        if col == 'ah':# 小文字にすること
            break
    # col_list = ['A', 'D', 'E', 'J', 'K', 'L', 'M', 'AH', 'AI', 'AJ', 'AU', 'AY', 'BK', 'BL', 'BM', 'BN', 'BO', 'BP',
    #             'BQ', 'BR', 'BS', 'BT', 'BU', 'BV', 'BW', 'BX']
    # for col in col_list:  # DEG がタイトル関連、YZが重量、　ADが見込売値, AU~AYがヤフオク、 BK以降は利益計算
    #     sht2.range('{}2:{}3'.format(col, col)).api.AutoFill(
    #         sht2.range("{}3:{}{}".format(col, col, lastRow1)).api, AutoFillType.xlFillDefault)

    # カテゴリ
    # category_list = ['13666', '2222']
    # フィギュアの中でも、ジャンル別で番号あるから、結構リスト増える。
    # リスト作らなくていいかも
    # if id == id_list[0]:
    #     categ = '13666' #  & '2211'
    # elif id == id_list[1]:
    #     categ = '222'

    # categ、数値を' ' で囲むとキーエラー起こるかも
    # アクセス数を優先している。ウォッチ書いても書かなくても結果は同じ
    df = pd.read_excel(at, sheet_name='清書_詳細', index=None) \
        .sort_values(['watch', 'access'], ascending=[True, False]).drop(['watch', 'access'], axis=1)
    df2 = df[df['カテゴリ'].isin(categ)] # https://note.nkmk.me/python-pandas-query/
    # カテゴリ列の categ の値のみに絞る。isin以外にも queryが使えそうだった
    # print(df2)  # categ_groupby = df.groupby('カテゴリ').get_group(categ) # categには、各々のカテゴリ番号が入る
    # df2 = df.loc('カテゴリ', categ)
    # df をloc やiloc で、列指定はできるが、　値で絞ることは出来るか > iloc
    # 清書からフィルタするから、値は「フィギア、本」ではなく、「13666, 」だよ
    # 更に、ウォッチとアクセス（列をつくり、）数が多い順に並べ、その２列を非表示にしたものを、to_csvする
    # 上から出品されるので、上から優先zド高い品に並べる

    csv_auc = r'C:/Users/[USERNAME_MASKED]\Desktop\00.Myself\04.Buyer\2.出品\syuppin_auc\syuppin_ebay%s.csv'
    i = 0
    # renbanName = csv_auc % i
    while os.path.exists(csv_auc % i):
        i += 1
    with open(csv_auc % i, mode="w", newline="", encoding="utf-8_sig") as f:
        df2.to_csv(f) #, index=False, encoding='cp932')
    # sypUp(csv_auc % i, id) # 下の定義関数は過去の記録として置いておく
    import syuppin_ebay3 as syp
    syp.sypUp(csv_auc % i, id)


# この関数は使わない
# def sypUp(f, id):
#     app = xw.App(visible=False)
#     wb = app.books.open(f)  # XWは、CSVを修正出来る  # (f)は一旦なし
#     sheet = wb.sheets(1)
#     sheet['F2:F500'].number_format = '0'  # カテゴリ、商品数、状態の数値に、[.0]がつくのを防ぐ試み
#     sheet['L2:L500'].number_format = '0'
#     sheet['M2:M500'].number_format = '0'
#     wb.save()
#     app.kill()
#     #
#     # id_list = ['[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
#     #            '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com']
#     # id = id_list[0]  # 0~5
#     browser = webdriver.Chrome(r'C:\\Users\\Kazuki Yuno\\Desktop\\chromedriver_win32\\chromedriver.exe')  # \\
#     browser.get('https://global.auctown.jp/items/create/bulk')  # 一括出品用ページ
#     # アカウント切替時はIDとパスワード入力。てかアカ毎にブラウザ切り替えなくていいか
#     email = browser.find_element_by_id('email')
#     email.send_keys(id)
#     passwd = browser.find_element_by_id('passwd')
#     passwd.send_keys('[PASSWORD_MASKED]')
#     time.sleep(3)
#     login = browser.find_element_by_id('submit')
#     login.click()
#     time.sleep(10)
#     # f = r'C:/Users/[USERNAME_MASKED]\Desktop\00.Myself\04.Buyer\2.出品\syuppin_auc\syuppin_ebay36.csv'
#     browser.find_element_by_id('upload_csv').send_keys(f)  # csv_auc ではない
#     time.sleep(10)
#
#     check = browser.find_element_by_xpath("//input[@type='checkbox']")  #
#     browser.execute_script("arguments[0].click();", check)
#     # check.click()
#     time.sleep(5)
#     # 出品ボタン
#     addItem = browser.find_element_by_id("add-items")
#     # addItem = browser.find_element_by_css_selector("#add-items") # Selector は# 要らない？？
#     browser.execute_script("arguments[0].click();", addItem)  # コレで成功
#
#     done = None
#     while not done:  # 待つ動作を繰り返し、もし[１００％]の要素が見えたら、break
#         try:
#             time.sleep(10)
#             done = browser.find_element_by_css_selector('#progress > div.progress-project-header > span')
#         except NoSuchElementException:
#             time.sleep(10)
#     browser.quit()
    #
    # dirname = r"C:/Users/[USERNAME_MASKED]\Downloads"
    # # 指定ディレ内の最新ファイルのパスを取得
    # # def get_latest_modified_file_path(dirname):
    # # p = Path(".")
    # p = Path(dirname)
    # files = list(p.glob("*"))
    # file_updates = {file_path: os.stat(file_path).st_mtime for file_path in files}
    # # global newest_fPath
    # newest_fPath = max(file_updates, key=file_updates.get)
    # print(newest_fPath)
    # fix(atk, newest_fPath, id)
    # cancel(atk, newest_fPath, id)


if __name__ == '__main__':
    atk = r"C:/Users/[USERNAME_MASKED]/Desktop/00.Myself/04.Buyer/1.利益計算/AtackList_Buyer43.xlsx"
    main(atk)