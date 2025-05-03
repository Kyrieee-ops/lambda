# LambdaからNotionに連携しレコードを取得

## 環境
- OS: Windows10 Pro 64bit
- GitBashを私用
- Python Verision 3.13

## 前提
- Pythonがインストールされていること

## 事前準備
1. notion_clientライブラリのインストール
```bash
mkdir python
cd python
# 作成したディレクトリにnotion-clientをインストール
pip install notion-client -t .
cd ../
# pythonディレクトリを再帰的にzipし、Lambdaレイヤーを作成
zip -r notion_layer.zip python
```
2. AWS Lambdaコンソールから新しいレイヤーを作成し、zipをアップロード 
3. Lambda関数を作成し、レイヤーを追加
4. 環境変数の定義
- Lambdaコンソールの設定から環境変数をクリック
- 編集で以下のキーと値を作成
    - キー: NOTION_DB_ID, 値: 実際のNotionのデータベースID
    - キー: NOTION_TOKEN, 値: NotionIntegrationで作成したSecretsキー

## 参考
NotionIntegrationの作成は以下記事を参照
- https://tektektech.com/notion-api/#Notionintegration

参考記事
- https://zenn.dev/ysksatoo/articles/66fd26893a6cdd (Notion連携について)
- https://qiita.com/har1101/items/40c33d1f32dc9d4b3dc8 (NotionDB IDについて)