# 各アカ、ループ出品
# 同じATKで、前アカが出品した数を求め、その数だけskiprowした清書シートをCSVにして提出

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import UnexpectedAlertPresentException
# from modules_scraping import tenki_at2sy as tenki
# import tenki_at2sy as tenki
import os
import pandas as pd
import shutil
import time
import datetime
import xlwings as xw
from pathlib import Path



def main(atk):
    # 66行分（アイテム）全て出品して、次は[3:]
    id_list = ['[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
               '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
               '[EMAIL_MASKED]@gmail.com','[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
               '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
               '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
               '[EMAIL_MASKED]@gmail.com','[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
               '[EMAIL_MASKED]@gmail.com'] # まずは100個で
    # category_list = ['フィギア', '本']


    # Listではなく、len(df) で行数測ればいいのでは？

    lastRow_list = []
    for id in id_list[:11]: #　[1:]＞Caoile飛ばす
        print(id)
        # category_list[i]
        # i += 1
        dirname = r"C:/Users/[USERNAME_MASKED]\Downloads"
        # 指定ディレ内の最新ファイルのパスを取得
        p = Path(dirname)
        files = list(p.glob("*"))
        file_updates = {file_path: os.stat(file_path).st_mtime for file_path in files}
        newest_fPath = max(file_updates, key=file_updates.get)
        print(newest_fPath)
        previous = os.path.getmtime(newest_fPath) # 前回時刻(ファイルのタイムスタンプ取得)
        current = time.time() # 現時刻
        # 現時刻 - 前回時刻を比較
        if (current - previous) < 1 * 60:  # もし2分以内にダウンロードされたファイルが有れば実行。。

            app = xw.App(visible=False)
            wb = app.books.open(newest_fPath)
            sht = wb.sheets(1)
            lastRow = sht.range('A1').end(-4121).row  # H1にしていた  タイトル列
            # df1 = pd.DataFrame(newest_fPath)
            # 行数 = len(df1)
            print('前アカactiveリストの最下行数 - ' + str(lastRow))
            # nextRow = lastRow + 1
            lastRow_list.append(lastRow)
            # ダウンロードディレの最新パス、読み込み、その最下行を求め、それ - 1  # その値を、skiprowsに渡す。ただし列名は飛ばさないように。

            df = pd.read_excel(atk, sheet_name='清書_詳細', index=None,
                               skiprows=range(1, 82 + sum(lastRow_list))) # caoile 出品を飛ばす場合、caoile 分 20を足す.
                                # 途中のアカから出品するときは既出の数値を足す
                                # なぜ82 ？？
            print('skipした出品アイテム行数 - ' + str(sum(lastRow_list)))
            syp(id, df)

        else: # 1分経過していたら、これまで通り Skiprow しない（先頭のCaoileの場合のみ
            df = pd.read_excel(atk, sheet_name='清書_詳細', index=None,
                               skiprows=range(1, 82)) # Caoile はfixCanした後だから、Active数も変わる。
            # 再度出品させてリミットまで出品させる。既存のものは既ににあるから問題ない。その後DownloadしてActive数を計算させる
            syp(id, df)


        import fixcancel_auc4 as fixcan
        fixcan.downFile(id) # fixCan 関係ないけどdownが最新だから呼ぶことにする
        # downFile(id)



def syp(id, df): # AT>SYの転記、清書シートのCSV出力、Aucへ出品
    syp_csv = r'C:/Users/[USERNAME_MASKED]\Desktop\00.Myself\04.Buyer\2.出品\syuppin_auc\syuppin_ebay%s.csv'
    i = 0
    while os.path.exists(syp_csv % i):
        i += 1
    with open(syp_csv % i, mode="w", newline="", encoding="utf-8_sig") as f:# encoding='cp1252' errors="ignore",  デフォルトがencoding="cp932"
        # pandasでファイルオブジェクトに書き込む        # utf-8-sig（BOMあり）も駄目. ｗ
        df.to_csv(f) # , delimiter = ','
    sypUp(syp_csv % i, id) # インデント、with と並列にならないように



def sypUp(f, id):
    app = xw.App(visible=False)
    wb = app.books.open(f)  # XWは、CSVを修正出来る  # (f)は一旦なし
    sheet = wb.sheets(1)
    sheet['F2:F500'].number_format = '0' # カテゴリ、商品数、状態の数値に、[.0]がつくのを防ぐ試み
    sheet['L2:L500'].number_format = '0'
    sheet['M2:M500'].number_format = '0'
    wb.save()
    app.kill()
    #
    # id_list = ['[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com',
    #            '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com', '[EMAIL_MASKED]@gmail.com']
    # id = id_list[0]  # 0~5
    browser = webdriver.Chrome(r'C:\\Users\\Kazuki Yuno\\Desktop\\chromedriver_win32\\chromedriver.exe')  # \\
    browser.get('https://global.auctown.jp/items/create/bulk')  # 一括出品用ページ
    # アカウント切替時はIDとパスワード入力。てかアカ毎にブラウザ切り替えなくていいか
    email = browser.find_element_by_id('email')
    email.send_keys(id)
    passwd = browser.find_element_by_id('passwd')
    passwd.send_keys('[PASSWORD_MASKED]')
    time.sleep(3)
    login = browser.find_element_by_id('submit')
    login.click()
    time.sleep(15)
    #f = r'C:/Users/[USERNAME_MASKED]\Desktop\00.Myself\04.Buyer\2.出品\syuppin_auc\syuppin_ebay36.csv'
    browser.find_element_by_id('upload_csv').send_keys(f)  # csv_auc ではない
    time.sleep(20)

    # check = browser.find_element_by_xpath("//input[@type='checkbox']") #
    # browser.execute_script("arguments[0].click();", check)

    check = None
    while not check:
        try:
            check = WebDriverWait(browser, 10).until(EC.presence_of_element_located((
                By.XPATH, "//input[@type='checkbox']")))  # https://www.guru99.com/xpath-selenium.html
            # By.XPATH, '//*[@id="progress"]/div[1]/span/following-sibling::span[1]'))) # following-sibling::span[1] がitem-parcentクラスの100%を指す
            time.sleep(3)
            check.click()  # 待ってくれない。。
        except NoSuchElementException:  # as te:
            print('no such element, retrying...')
        except TimeoutException: # as te:
            print('Timeout, retrying...')
        except ElementClickInterceptedException:
            print('Click Intercepted, retrying...')
        except UnexpectedAlertPresentException:
            print('unexpected Alerting, retrying...')

    # element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((
    #         By.XPATH,
    # check.click()
    time.sleep(5)
    # 出品ボタン
    addItem = browser.find_element_by_id("add-items")
    # addItem = browser.find_element_by_css_selector("#add-items") # Selector は# 要らない？？
    browser.execute_script("arguments[0].click();", addItem)  # コレで成功
    # time.sleep(500) # 一旦これでa
    hundred = None
    while not hundred:
        try: # 100% の要素が見えたら 終了
            hundred = WebDriverWait(browser, 60).until(EC.presence_of_element_located((
                By.XPATH, '//*[@id="progress"]//*[text()="100%"]'))) # https://www.guru99.com/xpath-selenium.html
                # By.XPATH, '//*[@id="progress"]/div[1]/span/following-sibling::span[1]'))) # following-sibling::span[1] がitem-parcentクラスの100%を指す
            hundred.click() # 待ってくれない。。
        except TimeoutException: # as te:
            print('Timeout, retrying...')
        except NoSuchElementException:  # as te:
            print('no such element, retrying...')
        except ElementClickInterceptedException:
            print('Click Intercepted, retrying...')
        except UnexpectedAlertPresentException:
            print('unexpected Alerting, retrying...')
    browser.quit()


if __name__ == '__main__':
    atk = r"C:/Users/[USERNAME_MASKED]/Desktop/00.Myself/04.Buyer/1.利益計算/AtackList_Buyer43.xlsx"
    main(atk)

