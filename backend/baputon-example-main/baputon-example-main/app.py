from flask import Flask, json, request, g

from src.middleware.cors import cors
from src.database.database import init_db
from config import config

from src.database.controller import create_user
from src.database.models import Users


def init_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = config.SECRET_KEY

    # app에 뭔가 더 추가하고 싶은게 있으면 여기에 추가
    cors.init_app(app)

    return app

app = init_app()
engine, get_db = init_db(config.DATABASE_URI)


# 연결이 끊어질때 db close
@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/status')
def status():
    return json.jsonify({'status': 'ok'})

@app.route("/your/backend/endpoints", methods=["GET", "POST"])
def your_backend_endpoints():
    # 여기에 로직을 추가해주세요.
    if request.method == "GET":
        return json.jsonify({"method": "GET"})
    elif request.method == "POST":
        return json.jsonify({"method": "POST"})
    

@app.route("/your/backend/endpoints2", methods=["GET", "POST"])
def your_backend_endpoints2():
    # 이런식으로 여러개 추가도 가능해요. 함수 이름만 안겹치면 되여.
    if request.method == "GET":
        return json.jsonify({"method": "GET"})
    elif request.method == "POST":
        return json.jsonify({"method": "POST"})
    


@app.route("/controller/example")
def controller_example():
    # 일단 요청 온 데이터들은 모두 저희가 생각했던 타입으로만 온다고 생각하고 코딩해봐요.
    request_data = request.get_json()
    user = Users(**request_data)

    db = get_db()
    create_user(db, user)
    
    return json.jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=13242)