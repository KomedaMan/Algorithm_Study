新規プロジェクトを始める

↓

プロジェクトに\
「src」\
「assets」\
というディレクトリを作成する\
（「.venv」と並列）

↓

「assets」ディレクトリに\
「fonts」\
「images」\
「sounds」\
というディレクトリを作成する

↓

同じくプロジェクトに\
「.gitignore」\
「README.md」\
「requirements.txt」\
というファイルを作成する

↓

.gitignoreに

venv/    \
__pycache__/    \
.idea/      

を記載する

↓
 
GitHub　に連携する

# pyxelインストール

ターミナルに\
python -m pip install -U pyxel    \
を記載する

↓

ターミナルに\
 python -m pip freeze > requirements.txt    \
を記載する