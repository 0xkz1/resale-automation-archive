# Resale Automation / Arbitrage System Archive (2019-2021)
*[日本語版は後半に記載しています]*

This repository contains the archive of an automated cross-border e-commerce (arbitrage) system I developed starting from **2019**. This project represents my journey from manual business operations to a fully automated pipeline.

**Note: Sensitive information such as database credentials, personal email addresses, and absolute local paths have been masked (`[MASKED]`) in all text and notebook files for security reasons.**

## 🎯 Project Journey: Evolution from Excel to SQL
This project is a testament to the "muddy" and iterative process of professional automation. It follows a distinct evolutionary path:

1.  **Phase 1: Excel & VBA Prototype (The Muddy Start):**
    Initially, I built the entire business logic using Excel and VBA. You can find these original "muddy" prototypes (logic-heavy spreadsheets and macros) in the `prototypes/` directory. These spreadsheets handled the first iterations of price scraping results and manual profit calculations.
2.  **Phase 2: Exploratory Python (Jupyter Notebooks):**
    As the volume grew, Excel reached its limits. I began experimenting with Python to handle larger datasets and more complex scraping. The `.ipynb` files in the `prototypes/` directory show the raw, unpolished record of my trials and errors during this transition.
3.  **Phase 3: Scalable Backend (Python/Pandas/SQL):**
    The final stage was moving to a production-like environment using Python scripts, Pandas for data processing, and a PostgreSQL database on Heroku for persistence. This allowed for multi-account management and high-volume automation.

## 🚀 Key Features & Problem-Solving Mindset
- **Circumventing Technical Roadblocks:** When official APIs were inaccessible, I used `Selenium` to automate a third-party management UI, effectively creating my own "API".
- **Disparate System Integration:** Seamlessly connected Web Scraping (`BeautifulSoup`), Machine Translation (`googletrans`), Data Analysis (`Pandas`), and Database Management (`SQLAlchemy`).
- **Development Support Skills:** This archive demonstrates my ability to bridge gaps between manual processes and high-level automation—a core competency for Development Support and Pipeline roles.

## 📁 Business Process Pipeline & Code Mapping
To maximize speed and efficiency, I designed the business pipeline primarily into 6 phases. I deliberately automated the most data-heavy phases (0 to 2) using Python, while leaving the latter phases (3 to 5) as manual operations because the ROI on automating them was too low at that time. This shows my ability to evaluate the true value of automation vs. manual effort.

* **0. Research & 1. Profit Calculation (Fully Automated):**
  * `mBall_yahoo6.py`, `zaico_yahoo.py` (Automated scraping, translation via `googletrans`, and profit margin calculation saving to Heroku DB).
* **2. Listing / Exporting (Fully Automated):**
  * `syuppin_ebay3.py`, `syuppin_ebay4.py` (CSV generation and automated browser UI manipulation via `Selenium` for bulk listing).
* **3. Promotion / 4. Purchasing / 5. Shipping (Manual Operation):**
  * Handled via manual review to maintain quality control and avoid over-engineering.

---

# 自動化せどり・アービトラージシステム (2019-2021年アーカイブ)

このリポジトリは、私が**2019年**に独学でPythonを学び始めた当初から構築・拡張してきた、物販ビジネス（アービトラージ）自動化システムのアーカイブです。実務の泥臭い課題を解決しながら進化した軌跡を記録しています。

**※セキュリティ上の観点から、コード、ノートブック、テキストファイル内の機密情報（DB情報、アドレス等）はプログラムにより `[MASKED]` 処理済みです。**

## 🎯 プロジェクトの軌跡：ExcelからSQLへの進化
本プロジェクトは、単なるWebアプリ開発ではなく、実務のスケールに合わせて技術スタックを進化させてきた「泥臭い」プロセスそのものです。

1.  **フェーズ1：Excel & VBA によるプロトタイプ（すべての始まり）：**
    最初はすべてのロジックをExcelとVBAで構築しました。`prototypes/` ディレクトリには、当時の「泥臭さ」が詰まったオリジナルの計算表やマクロ（.xlsm / .xlsx）をあえて含めています。
2.  **フェーズ2：Pythonによる試行錯誤 (Jupyter Notebooks)：**
    データ量が増えるにつれ、Excelの限界が見えてきました。そこでPythonを使い始め、実験を繰り返した記録が `prototypes/` 内の `.ipynb` ファイル群です。試行錯誤の生々しい記録を確認いただけます。
3.  **フェーズ3：スケーラブルなバックエンド構築 (Python/Pandas/SQL)：**
    最終的に、Pythonスクリプト、Pandasでの高速処理、Heroku上のPostgreSQLによるデータ永続化へと移行しました。これにより、複数アカウントの同時運用や大量の商品管理が現実のものとなりました。

## 🚀 現場への貢献：やり切る力と自動化マインド
- **技術的障壁の突破：** 公式APIが使えない状況下で `Selenium` を用いて既存サービスのUIを自動操縦し、自作の「擬似API」を構築して自動化を貫徹しました。
- **異種システムの統合力：** スクレイピング、機械翻訳、データ解析、DB管理を1つのパイプラインとして統合。
- **Development Support職に向けて：** 手作業によるプロトタイプから高度な自動化へとワークフローを押し上げたこの経験は、クリエイターとエンジニアの橋渡しをし、現場の「詰まり」を解消する Development Support の職務に直結するものと確信しています。

## 📁 業務パイプラインとコードの対応関係
当時の実際の業務は、以下のような業務フェーズに沿ったディレクトリ構成で管理し、各段階でPythonスクリプトを走らせていました。
「何でもかんでも自動化する」のではなく、データ処理が重い前半フェーズ（0〜2）をプログラムで完全自動化し、残りのフェーズ（3〜5）はあえて費用対効果（ROI）の観点から人的リソースでカバーし、ビジネスの立ち上げ速度を最優先しました。

* **0. リサーチ / 1. 利益計算（完全自動化）:** 
  * `mBall_yahoo6.py`, `zaico_yahoo.py` 等（国内データ収集、自動翻訳、各種手数料・送料判定を含んだ利益計算データベース構築）
* **2. 出品（完全自動化）:**
  * `syuppin_ebay3.py`, `syuppin_ebay4.py` （出品用CSVの生成、およびSeleniumを利用したツールのUI自動操縦による一括出品処理）
* **3. 販促 / 4. 仕入れ / 5. 発送（手動オペレーション）:**
  * 自動化の費用対効果とクオリティコントロールの観点から、意図的に目視と手作業のオペレーションとして残しました。
