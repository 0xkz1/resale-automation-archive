# Resale System Archive (2021)

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
