#開発環境
OS：Windows11
言語：Python ver3.13.1
framework：Django
エディタ：VSCode

#Python ver3.13.1をインストール
https://www.python.org/

#PC再起動

#Pythonバージョン確認
python -V

#任意のディレクトリに移動し、clone
git clone "https://~"

#ルートディレクトリに移動
cd myapp

#仮想環境生成
python -m venv venv

#仮想環境起動
venv\Scripts\activate.bat

#パッケージを仮想環境にインストール
pip install -r requirements.txt

#コマンド実行（ゲーム開始）
python manage.py word_quiz

#仮想環境停止
deactivate
