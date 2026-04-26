# Resale Automation / Arbitrage System Archive (2019-2021)
*[日本語版は後半に記載しています]*

This repository contains the archive of an automated cross-border e-commerce (arbitrage) system I developed starting from **2019**. This project represents my journey from manual business operations to a fully automated pipeline.

**Note: Sensitive information such as database credentials, personal email addresses, and absolute local paths have been masked (`[MASKED]`) in all text and notebook files for security reasons.**

## 🎯 Project Journey: Evolution from Excel to SQL
This project is a testament to the "muddy" and iterative process of professional automation. It follows a distinct evolutionary path:

1.  **Phase 1: Excel & VBA Prototype (The Muddy Start):**
    Initially, I built the entire business logic using Excel and VBA. You can find these original "muddy" prototypes (logic-heavy spreadsheets and macros) in the `evolution/` directory. These spreadsheets handled the first iterations of price scraping results and manual profit calculations.
2.  **Phase 2: Exploratory Python (Jupyter Notebooks):**
    As the volume grew, Excel reached its limits. I began experimenting with Python to handle larger datasets and more complex scraping. The `.ipynb` files in the `evolution/` directory show the raw, unpolished record of my trials and errors during this transition.
3.  **Phase 3: Scalable Backend (Python/Pandas/SQL):**
    The final stage was moving to a production-like environment using Python scripts, Pandas for data processing, and a PostgreSQL database on Heroku for persistence. This allowed for multi-account management and high-volume automation.

## 🚀 Key Features & Problem-Solving Mindset
- **Circumventing Technical Roadblocks:** When official APIs were inaccessible, I used `Selenium` to automate a third-party management UI, effectively creating my own "API".
- **Disparate System Integration:** Seamlessly connected Web Scraping (`BeautifulSoup`), Machine Translation (`googletrans`), Data Analysis (`Pandas`), and Database Management (`SQLAlchemy`).
- **Development Support Skills:** This archive demonstrates my ability to bridge gaps between manual processes and high-level automation—a core competency for Development Support and Pipeline roles.

---

# 自動化せどり・アービトラージシステム (2019-2021年アーカイブ)

このリポジトリは、私が**2019年**に独学でPythonを学び始めた当初から構築・拡張してきた、物販ビジネス（アービトラージ）自動化システムのアーカイブです。実務の泥臭い課題を解決しながら進化した軌跡を記録しています。

**※セキュリティ上の観点から、コード、ノートブック、テキストファイル内の機密情報（DB情報、アドレス等）はプログラムにより `[MASKED]` 処理済みです。**

## 🎯 プロジェクトの軌跡：ExcelからSQLへの進化
本プロジェクトは、単なるWebアプリ開発ではなく、実務のスケールに合わせて技術スタックを進化させてきた「泥臭い」プロセスそのものです。

1.  **フェーズ1：Excel & VBA によるプロトタイプ（すべての始まり）：**
    最初はすべてのロジックをExcelとVBAで構築しました。`evolution/` ディレクトリには、当時の「泥臭さ」が詰まったオリジナルの計算表やマクロ（.xlsm / .xlsx）をあえて含めています。
2.  **フェーズ2：Pythonによる試行錯誤 (Jupyter Notebooks)：**
    データ量が増えるにつれ、Excelの限界が見えてきました。そこでPythonを使い始め、実験を繰り返した記録が `evolution/` 内の `.ipynb` ファイル群です。試行錯誤の生々しい記録を確認いただけます。
3.  **フェーズ3：スケーラブルなバックエンド構築 (Python/Pandas/SQL)：**
    最終的に、Pythonスクリプト、Pandasでの高速処理、Heroku上のPostgreSQLによるデータ永続化へと移行しました。これにより、複数アカウントの同時運用や大量の商品管理が現実のものとなりました。

## 🚀 現場への貢献：やり切る力と自動化マインド
- **技術的障壁の突破：** 公式APIが使えない状況下で `Selenium` を用いて既存サービスのUIを自動操縦し、自作の「擬似API」を構築して自動化を貫徹しました。
- **異種システムの統合力：** スクレイピング、機械翻訳、データ解析、DB管理を1つのパイプラインとして統合。
- **Development Support職に向けて：** 手作業によるプロトタイプから高度な自動化へとワークフローを押し上げたこの経験は、クリエイターとエンジニアの橋渡しをし、現場の「詰まり」を解消する Development Support の職務に直結するものと確信しています。
