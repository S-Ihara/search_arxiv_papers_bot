# search_arxiv_papers_bot

## これは何
arXivから論文を引っ張ってくるbot

## requirements
```
arxiv==1.4.2
requests
```

## 使い方
``` bash
git clone https://github.com/S-Ihara/search_arxiv_papers_bot.git
cd search_arxiv_papers_bot
```
### 設定
1. DeepLのAPIキーを取得する
2. setting.pyを以下のように作成する
    - API_KEYにはDeepLのAPIキーを指定
    - Search_Querysにはarxivを検索する際のQueryを指定。Queryについての詳細は[こちら](https://arxiv.org/help/api/user-manual#query_details)
```
API_KEY = XXXXXXXXXXXXXXXXXXXXXXX # 自身のAPIキーを指定

# cat:cs.* AND (ti:explain OR abs:explain)
Search_Querys = [
    XXXXX,
    OOOOO,
]
```

### 実行
``` python 
python main.py
```
上記コマンドを実行することでpapersファイルに論文の情報がtxtファイルで保存される。
