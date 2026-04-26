# Resale Automation / Arbitrage System (2021 Archive)
*[日本語版は後半に記載しています]*

This repository contains the archive of an automated cross-border e-commerce (arbitrage) system I built around 2021 when I was teaching myself Python programming. 

**Note: Sensitive information such as database credentials, personal email addresses, and absolute local paths have been masked (`[MASKED]`) for security reasons.**

## 🎯 About This Project
This system was designed to fully automate my personal e-commerce business operations at the time. It managed everything from sourcing to profit calculation and final listing, closing the gap between domestic Japanese marketplaces (Yahoo Auctions) and international platforms (eBay).

## 🚀 Key Features & The "Get It Done" Mindset
From a professional software engineering standpoint—such as maintainability or object-oriented design—this codebase is very raw (procedural scripts, hardcoded variables, etc.). I am aware that this is not an example of "clean code". 
However, I am publishing this to demonstrate my **problem-solving capabilities, adaptability, and unyielding drive to automate complex workflows.**

1. **Circumventing Technical Roadblocks (Selenium API Hack):**
   When I struggled to understand the eBay API authentication, instead of giving up, I built a workaround. I used Python (`Pandas`) to format the scraped data into a specific CSV format, and then used `Selenium` to automatically log into a domestic third-party multi-listing management service and bulk-upload the CSVs by directly manipulating the DOM. 
2. **Connecting Disparate Systems:**
   I successfully glued together completely different technologies into a single continuous pipeline:
   - **Web Scraping:** Extracting prices/images directly from DOM elements using `BeautifulSoup`.
   - **Machine Translation:** Translating Japanese titles/descriptions via `googletrans`.
   - **Data Processing & Business Logic:** Using `Pandas/Numpy` to calculate complex conditional shipping costs, service fees, and break-even points.
   - **Data Persistence:** Storing data in a Heroku PostgreSQL database (`SQLAlchemy`/`psycopg2`).
   - **Local Macro Execution:** Triggering local Excel (`PERSONAL.XLSB`) macros via Windows COM objects (`xlwings`) for specific formatting.

## 💼 Why I am sharing this for a Development Support Role
In a Development Support or Tech Art/Pipeline support role, the priority is often bridging gaps between tools, unblocking creative teams, and finding ways to automate tedious workflows—even when official APIs are lacking or undocumented. 
This codebase represents my core philosophy: **"If there isn't a direct path, I will find a workaround and build a bridge to make it happen."**

---

# 自動化せどり・アービトラージシステム (2021年アーカイブ)

このリポジトリは、私がPythonプログラミングを独学で学び始めた2021年頃に、自身の物販ビジネス（アービトラージ）を自動化するために構築・稼働させていたシステムのソースコード・アーカイブです。

**※セキュリティ上の観点から、データベースのパスワード、個人のGmailアドレス、ローカルの絶対パスなどの機密情報はプログラムで `[MASKED]` 等にマスク処理（サニタイズ）を行っています。**

## 🎯 プロジェクトの概要
当時の自分のビジネス要件を満たすため、「国内の仕入れ先（ヤフオク等）からのデータ収集」→「複雑な利益計算・英語翻訳」→「海外（eBay）への出品用データ成形・自動登録」に至るまでの一連のワークフローをつなぎ合わせたものです。

## 🚀 アピールポイント（「やり切る」マインドセット）
現在のソフトウェアエンジニアリングにおける保守性やオブジェクト指向の観点から見れば、このコードは非常に荒削りな（手続き型のスパゲッティコード的な）部分が多いことを自覚しています。
しかし、あえてこの過去のコードを公開した理由は、**「どのような壁にぶつかっても、手持ちの技術を繋ぎ合わせて業務パイプラインを貫徹する問題解決能力」**を証明するためです。

1. **APIの壁を「Seleniumによる自動操縦」で突破：**
   当時、eBayの公式APIの認証や仕様が理解できなかった際、諦めるのではなく、「出品管理ツールのWeb画面にSeleniumで自動ログインし、生成したCSVを一括アップロードさせる」というアプローチを独自に考案し、強引に自動出品処理を実現させました。
2. **複数の技術を跨いだワークフロー構築力：**
   以下のような全く異なる技術領域を、1人でつなぎ合わせてビジネスツールを完成させました。
   - `BeautifulSoup` を用いたWebスクレイピング
   - `googletrans` APIを活用したタイトル・説明文の自動翻訳
   - `Pandas` / `Numpy` を駆使した、重量別送料・各種手数料の条件分岐を含む高度な利益計算ロジック
   - Heroku(PostgreSQL) へのWebデータ蓄積
   - `xlwings` (Win32COM) を介したローカル環境のExcelマクロ（PERSONAL.XLSB）の自動実行

## 💼 Development Support 等の志望動機として
Development Support やパイプライン整備の現場では、「ツール間の仕様が合わない」「APIが用意されていない」といった状況下でも、何かしらのハックやスクリプトを駆使してクリエイターの業務フロー（パイプライン）を円滑に回す能力が求められると認識しています。
このシステムを作った当時の**「道がないなら、泥臭くても迂回路を自作して業務を自動化する」というメンタリティ**は、現場の課題解決においても必ず力になると確信しています。
