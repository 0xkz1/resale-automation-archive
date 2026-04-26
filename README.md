# Resale Automation Pipeline

## Overview
This repository contains a suite of Python scripts and automation tools I developed to streamline and fully automate e-commerce resale operations. The system was built out of a personal need to replace repetitive manual data entry, scraping, and inventory management tasks across multiple online marketplaces.

It acts as a complete data processing pipeline: scraping pricing data, normalizing item attributes, and seamlessly transferring updates between different services (e.g., executing cross-platform inventory syncs or generating listing manifests).

## Core Features
1. **Multi-Source Scraping:** Robust HTML and API-based extraction logic capable of handling various marketplace structures and data formats.
2. **Data Normalization Engine:** A core module that cleans raw datasets, handles character encoding issues, and transforms disparate marketplace attributes into a unified internal schema.
3. **Automated Inventory Synchronization:** Headless browser integration and direct API requests to monitor stock levels and propagate price updates across disparate platforms in real-time.
4. **Resilient Execution & Logging:** Implements exponential backoff for rate limits, comprehensive error handling for network volatility, and detailed log rotation to ensure high-availability without manual intervention.

## Why I Built This
This toolset was created to solve a real-world operational bottleneck. Moving products between marketplaces manually is error-prone and unscalable. By automating the extraction and posting logic, I could ensure data integrity while saving hundreds of hours of manual labor. 

*Note: For security reasons, all sensitive API keys, hardcoded credentials, and proprietary marketplace endpoint details have been removed or mocked in this public archive.*

---

# (Japanese) Resale Automation Pipeline

## 概要
このリポジトリは、Eコマースにおける転売・在庫管理オペレーションを完全自動化するために開発したPythonスクリプトおよび自動化ツールのコレクションです。複数のオンラインマーケットプレイスにまたがる手動でのデータ入力、スクレイピング、在庫管理の手間という個人的な課題を解決するために構築しました。

商品の価格データの収集から属性の正規化、そして異なるサービス間でのデータ同期（例：クロスプラットフォームでの在庫連携や出品リストの自動生成）までを担う、End-to-Endのデータ処理パイプラインとして機能します。

## 主要な機能
1. **マルチソース・スクレイピング:** 多様なマーケットプレイスの構造に対応し、HTMLやAPIから商品データを確実に抽出するロジックを実装。
2. **データ正規化エンジン:** 未加工のデータセットをクレンジングし、文字コードの問題を解決した上で、各マーケットプレイス独自の属性を統一された内部スキーマに変換します。
3. **自動在庫同期システム:** ヘッドレスブラウザや直接のAPIリクエストを組み合わせ、在庫レベルや価格変動をリアルタイムで監視し、プラットフォーム間で同期させます。
4. **堅牢な実行環境とログ管理:** APIのレートリミットに対するエクスポネンシャルバックオフの実装や、ネットワークの不安定さに耐えるエラーハンドリング、詳細なログローテーションにより、無人での安定稼働を実現しています。

## 開発の背景
このツールは、現実のオペレーションにおけるボトルネックを解消するために作成しました。マーケットプレイス間で手動で商品を移動・管理するのはミスが起きやすく、スケールしません。データ抽出から出品までのロジックをプログラマブルに処理することで、データの整合性を担保しつつ、膨大な手作業の時間を削減しました。

*※セキュリティの観点から、公開アーカイブである本リポジトリではAPIキー、認証情報、および特定の非公開マーケットプレイスのエンドポイント等の機密情報は削除またはモック化しています。*
