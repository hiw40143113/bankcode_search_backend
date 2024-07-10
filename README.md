# Bankcode-search

## 簡介

本專案是一個結合 Django 和 React 前端技術的 Web 應用，旨在提供使用者可以方便查詢臺灣銀行代碼。因本專案架構為前後端分離，需搭配前端專案一起使用。

前端 React repo:`https://github.com/hiw40143113/bankcode_search_frontend`

## 目錄

- [Bankcode-search](#Bankcode-search)
  - [簡介](#簡介)
  - [目錄](#目錄)
  - [技術棧](#技術棧)
  - [功能](#功能)
  - [安裝與運行](#安裝與運行)
    - [先決條件](#先決條件)
    - [安裝步驟](#安裝步驟)
  - [使用範例](#使用範例)
  - [作者資訊](#作者資訊)

## 技術棧

- Django

## 功能

- 使用者可搜尋或選擇銀行及分行名稱產生分行詳細資訊
- 詳細資訊有複製代碼或複製網址按鈕提供使用者快速紀錄

## 安裝與運行

### 先決條件

- Python 3.8+
- Django
- PostgreSQL

### 安裝步驟

1. 使用 `poetry install` 安裝本專案運行時所需套件
2. 設置環境變數：

   在專案 /.bankcode 創建一個 `.env` 文件，並依照 `.env.example` 添加對應的本機端內容

3. 運行 python manage.py migrate 建立資料庫欄位

## 使用範例

你可以使用 `python manage.py load_bank_data` 指令將資料匯進資料庫，搭配前端 React 專案可在瀏覽器中訪問 `http://127.0.0.1:3000/` 來查看應用並進行操作。

## 作者資訊

- 吳軒逸  
  [GitHub](https://github.com/hiw40143113)
