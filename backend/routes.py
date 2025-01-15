from flask import Blueprint, jsonify, render_template, request
from backend.models import db, StampRally, Spot, StampStatus
from math import radians, cos, sin, sqrt, atan2

# ルートの登録
def register_routes(app):
    # スタンプラリー一覧ページ
    @app.route('/', methods=['GET'])
    def show_index():
        rallies = StampRally.query.all()
        return render_template('index.html', rallies=rallies)
    
    # スタンプラリー名一覧を返すAPI
    @app.route('/api/rallies', methods=['GET'])
    def get_all_rallies():
        rallies = StampRally.query.all()
        response = [{"rally_id": rally.rally_id, "name": rally.name} for rally in rallies]
        return jsonify(response)

    # 指定IDのスタンプラリー詳細を取得するAPI
    @app.route('/getstamp/<int:rally_id>', methods=['GET'])
    def getstamp_page(rally_id):
        rally = StampRally.query.get(rally_id)
        if not rally:
            return "スタンプラリーが見つかりませんでした。", 404

        # 辞書形式に変換
        spots = [
            {
                "spot_id": spot.spot_id,
                "name": spot.name,
                "latitude": spot.latitude,
                "longitude": spot.longitude,
                "description": spot.description,
            }
            for spot in rally.spots
        ]
        rally_data = {
            "rally_id": rally.rally_id,
            "name": rally.name,
            "description": rally.description,
            "spots": spots,
        }

        return render_template('getstamp.html', rally=rally_data)


    # スタンプを取得するAPI
    @app.route('/api/stamp-status/<int:spot_id>', methods=['POST'])
    def get_stamp(spot_id):
        spot = Spot.query.get(spot_id)
        

        if not spot:
            return jsonify({"error": "Spot not found"}), 404
        data = request.get_json()
        print(f"Received POST data: {data}")  # リクエストデータをログ出力
        user_lat = data.get("latitude")
        user_lon = data.get("longitude")

        #デバック用
        print(f"Received location: lat={user_lat}, lon={user_lon}")

        if not user_lat or not user_lon:
            return jsonify({"error": "Latitude and Longitude are required"}), 400

        # 距離計算（Haversine formula）
        def calculate_distance(lat1, lon1, lat2, lon2):
            R = 6371.0  # 地球の半径（km）
            dlat = radians(lat2 - lat1)
            dlon = radians(lon2 - lon1)
            a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            return R * c
        distance = calculate_distance(user_lat, user_lon, spot.latitude, spot.longitude)
        print(f"Calculated distance between user and spot: {distance} km")  # 距離をログ出力

        if distance > 1:  # 距離が500メートルを超える場合
            print("Distance is greater than 0.5 km, returning error")
            return jsonify({"status": "error", "message": "範囲外です。"}), 400

        # スタンプの進捗を更新
        stamp_status = StampStatus.query.filter_by(spot_id=spot_id).first()
        if stamp_status:
            stamp_status.is_completed = True
            db.session.commit()
            return jsonify({"status": "success", "message": "スタンプを取得しました。"})
        else:
            return jsonify({"error": "Stamp Status not found"}), 404
    
    @app.route('/mypage')
    def showprogress():
        # 必要なデータを取得
        completed_rallies = StampRally.query.filter_by(is_completed="completed").all()
        in_progress_rallies = StampRally.query.filter_by(is_completed="in_progress").all()
        
        # データをテンプレートに渡す
        return render_template('mypage.html', completed_rallies=completed_rallies, in_progress_rallies=in_progress_rallies)



    # 完了済みスタンプラリーを取得するAPI
    @app.route('/api/user/completed-rallies', methods=['GET'])
    def get_completed_rallies():
        rallies = StampRally.query.all()
        response = []
        for rally in rallies:
            print(f"Checking rally: {rally.name}")
            if rally.is_completed == "completed":
                response.append({
                    "rally_id": rally.rally_id,
                    "name": rally.name
                })
        return jsonify(response)


    # 進行中スタンプラリーを取得するAPI
    @app.route('/api/user/in-progress-rallies', methods=['GET'])
    def get_in_progress_rallies():
        rallies = StampRally.query.all()
        response = [{
            "rally_id": rally.rally_id,
            "name": rally.name
        } for rally in rallies if rally.is_completed == "in_progress"]
        return jsonify(response)
    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404