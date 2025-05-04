import os
from pprint import pprint
# from requests.exceptions import RequestException

from notion_client import Client

def lambda_handler(event, context):
    # 例外が発生する可能性のある処理
    try:
        # 環境変数からトークンを取得
        notion_token = os.getenv('NOTION_TOKEN')
        notion_db_id = os.getenv('NOTION_DB_ID')
        if not notion_token:
            raise ValueError("Notion token not found in environment variables")
        if not notion_db_id:
            raise ValueError("Notion database ID not found in environment variables")


        # Notionクライアントの初期化
        notion = Client(auth=notion_token)


        # 対象のNotionDBかをクエリしてデータを取得
        db = notion.databases.query(
            database_id=notion_db_id
        )

        return query_notion_db(db)


    except Exception as e:
        return {
            "statusCode": 500,
            "body": {
                "message": "Error",
                "error": str(e)
            }
        }
        
def query_notion_db(db):

    pages_data = []

    for page in db['results']:
        # Title の取得（titleプロパティの最初の要素からtext.contentを取得）
        title = page['properties']['Title']['title'][0]['text']['content']
        
        # URL の取得（urlプロパティを直接取得）
        url = page['properties']['URL']['url']
        
        # Tag の取得（multi_selectからタグ名のリストを取得）
        tags = [tag['name'] for tag in page['properties']['tag']['multi_select']]

        # データを辞書形式で保存
        pages_data.append({
            "title": title,
            "url": url,
            "tags": tags
        })
    
    print(f"取得レコード数: {len(pages_data)}")  # 取得レコード数がNotionDBと一致しているか確認

    # 要素取得
    return {
        "statusCode": 200,
        "body": {
            "message": "Success",
            "data": pages_data  # 全データをJSON形式で返す
        }
    }

