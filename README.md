<div id="top"></div>

## 使用技術一覧

<!-- シールド一覧 -->
<p style="display: inline">
  <!-- バックエンドのフレームワーク一覧 -->
  <img src="https://img.shields.io/badge/-Django-092E20.svg?logo=django&style=for-the-badge">
  <!-- バックエンドの言語一覧 -->
  <img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">
</p>

## 目次

1. [環境](#環境)
2. [開発環境構築](#開発環境構築)

## 環境

| 言語・フレームワーク  | バージョン |
| --------------------- | ---------- |
| Python                | 3.13.1     |
| Django                | 5.1.4      |

## 開発環境構築

### 仮想環境の作成と起動
以下のコマンドで仮想環境を作成
```
python -m venv venv
```
以下のコマンドで仮想環境を起動
```
venv\Scripts\activate
```
### パッケージのインストール
以下のコマンドでパッケージを仮想環境にインストール
```
pip install -r requirements.txt
```
### 動作確認
以下のコマンドを実行し、ゲームを開始
```
python manage.py word_quiz
```
### 仮想環境の停止

以下のコマンドで仮想環境を停止
```
deactivate
```
