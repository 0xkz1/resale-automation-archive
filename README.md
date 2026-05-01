# Resale Automation Pipeline

## Overview
This repository contains a suite of Python scripts and automation tools I developed to streamline and fully automate e-commerce resale operations. The system was built out of a personal need to replace repetitive manual data entry, scraping, and inventory management tasks across multiple online marketplaces.

It acts as a complete data processing pipeline: scraping pricing data, normalizing item attributes, and seamlessly transferring updates between different services (e.g., executing cross-platform inventory syncs or generating listing manifests).

## Learning Timeline (2019-2021)

```mermaid
timeline
    title Learning Timeline (2019-2021)
    section 2019
    2019 July Start : Python Basics, Resale Basics
    style 2019 July Start fill:#ffffff,stroke:#333333,color:#000000
    section 2020 First Half
    2020 First Half : Excel & VBA (Basic Spreadsheet) --> Manual Data Aggregation & Simple Automation
                --> Evidence: .xlsm files in prototypes/
    style 2020 First Half fill:#f0f0f0,stroke:#333333,color:#000000
    section 2020 Second Half
    2020 Second Half : Pandas, Numpy, Jupyter Notebook --> Scraped Data Cleaning & Profit Calculation
                --> Evidence: Notebooks like mBall_yahoo4.ipynb
    style 2020 Second Half fill:#778899,stroke:#333333,color:#ffffff
    section 2021 First Half
    2021 First Half : Selenium, SQL, API Integration --> Browser Automation + DB Storage + Auto Listing
                --> Evidence: syuppin_ebay*.py, local-heroku_sql.py
    style 2021 First Half fill:#606060,stroke:#333333,color:#ffffff
```

## Pipeline Architecture
1. **Scraping Layer (Multi-Source):** `mBall_yahoo*.py`
    - Uses Selenium and Requests to handle dynamic content and extract raw product data from Yahoo and other sources.
2. **Data Processing & Normalization:** `local-heroku_sql.py` / `prototypes/*.ipynb`
    - Cleans raw input, resolves encoding issues, and maps marketplace attributes to a unified database schema.
3. **Automated Sync & Listing:** `syuppin_ebay*.py` / `zaico_yahoo.py`
    - Handles automated cross-platform listing on eBay and inventory synchronization with external services like Zaico.
4. **Execution Stability:** (Built into all scripts)
    - Strategic use of `try...except` and `time.sleep` to handle network timeouts and respect rate limits.

## Why I Built This
This toolset was created to solve a real-world operational bottleneck. Moving products between marketplaces manually is error-prone and unscalable. By automating the extraction and posting logic, I could ensure data integrity while saving hundreds of hours of manual labor. 

*Note: For security reasons, all sensitive API keys, hardcoded credentials, and proprietary marketplace endpoint details have been removed or mocked in this public archive.*

---

# (Japanese) Resale Automation Pipeline

## 概要
このリポジトリは、Eコマースにおける転売・在庫管理オペレーションを完全自動化するために開発したPythonスクリプトおよび自動化ツールのコレクションです。複数のオンラインマーケットプレイスにまたがる手動でのデータ入力、スクレイピング、在庫管理の手間という個人的な課題を解決するために構築しました。

商品の価格データの収集から属性の正規化、そして異なるサービス間でのデータ同期（例：クロスプラットフォームでの在庫連携や出品リストの自動生成）までを担う、End-to-Endのデータ処理パイプラインとして機能します。

## 独学での技術習得の歩み

```mermaid
timeline
    title 独学での技術習得の歩み（2019〜2021）
    section 2019
    2019 7月開始 : Python基礎, Resale基礎
    style 2019 7月開始 fill:#ffffff,stroke:#333333,color:#000000
    section 2020 前半
    2020 前半 : Excel・VBA（表計算の基本） --> 手作業のデータ集計・簡易自動化
            --> 証拠：prototypes/ 内の .xlsm ファイル
    style 2020 前半 fill:#f0f0f0,stroke:#333333,color:#000000
    section 2020 後半
    2020 後半 : Pandas, Numpy, Jupyter Notebook --> スクレイピングデータの整形・利益計算
            --> 証拠：mBall_yahoo4.ipynb などの Notebook
    style 2020 後半 fill:#778899,stroke:#333333,color:#ffffff
    section 2021 前半
    2021 前半 : Selenium・SQL・API連携 --> ブラウザ自動操作＋DB保存＋自動出品
            --> 証拠：syuppin_ebay*.py, local-heroku_sql.py
    style 2021 前半 fill:#606060,stroke:#333333,color:#ffffff
```

## パイプラインの構成
1. **スクレイピング層 (マルチソース対応):** `mBall_yahoo*.py`
    - SeleniumやRequestsを用い、Yahoo等の複雑なサイト構造から商品データを抽出します。
2. **データの整形と正規化:** `local-heroku_sql.py` / `prototypes/*.ipynb`
    - 未加工のデータをクレンジングし、内部DBや共通フォーマットに変換・正規化します。
3. **在庫・価格の自動同期:** `syuppin_ebay*.py` / `zaico_yahoo.py`
    - eBayへの自動出品や、Zaico等の外部ツールと連携した在庫の自動同期を担います。
4. **実行の安定化:** (各スクリプトに実装)
    - `try...except` による例外処理と `time.sleep` を組み合わせ、制限回避と安定稼働を両立させています。

## 開発の背景
このツールは、現実のオペレーションにおけるボトルネックを解消するために作成しました。マーケットプレイス間で手動で商品を移動・管理するのはミスが起きやすく、スケールしません。データ抽出から出品までのロジックをプログラマブルに処理することで、データの整合性を担保しつつ、膨大な手作業の時間を削減しました。

*※セキュリティの観点から、公開アーカイブである本リポジトリではAPIキー、認証情報、および特定の非公開マーケットプレイスのエンドポイント等の機密情報は削除またはモック化しています。*