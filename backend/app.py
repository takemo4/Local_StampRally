from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pyngrok import ngrok
from dotenv import load_dotenv
import os
from sqlalchemy.orm import DeclarativeBase


# テンプレートと静的ファイルの置き場所
TEMPLATE_PATH = '../project/templates'
STATIC_PATH = '../project/static'

# .envファイルの読み込み
load_dotenv()
# トークンを設定
ngrok.set_auth_token(os.getenv("NGROK_AUTH_TOKEN"))
#アプリの初期化
class Base(DeclarativeBase):
  pass
#インスタンス化
db = SQLAlchemy(model_class=Base)

def create_app():
    # Flask アプリケーションのインスタンスを作成
    app = Flask(__name__, template_folder=TEMPLATE_PATH, static_folder=STATIC_PATH)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sample_db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # dbのインスタンスをアプリケーションにバインド
    db.init_app(app)
    # APIルートの登録
    from backend.routes import register_routes
    register_routes(app)
    return app


