from backend.models import db, StampRally, Spot
from backend.app import create_app


app = create_app()

with app.app_context():

    db.create_all()
    
    # スタンプラリー 1: さいたま市
    rally1 = StampRally(name="さいたま市スタンプラリー", description="さいたま市内の観光スポットを巡るラリー")
    rally2 = StampRally(name="秋田市スタンプラリー", description="秋田市内の観光スポットを巡るラリー")

    # さいたま市スポット
    spots_rally1 = [
        Spot(name="さいたま市役所", latitude=35.861729, longitude=139.645482, description="さいたま市の行政機関所在地"),
        Spot(name="埼玉スタジアム2002", latitude=35.905808, longitude=139.717037, description="サッカー専用の国内最大級のスタジアム"),
        Spot(name="もみじ公園", latitude=35.846546, longitude=139.673109, description="さいたま市の公園"),
        Spot(name="さいたま市民医療センター", latitude=35.881917, longitude=139.598223, description="病院"),
        Spot(name="文明堂さいたまあおぞら工房", latitude=35.881129, longitude=139.59849, description="お菓子屋さん"),
        Spot(name="パティスリーＭＯＡ", latitude=35.853847, longitude=139.67436, description="ケーキ屋さん"),
    ]
    rally1.spots.extend(spots_rally1)

    # 秋田市スポット
    spots_rally2 = [
        Spot(name="秋田城跡", latitude=39.728636, longitude=140.090801, description="秋田市内の歴史的な城跡"),
        Spot(name="秋田市立千秋美術館", latitude=39.720942, longitude=140.102305, description="秋田市中心部にある美術館"),
        Spot(name="秋田市大森山動物園", latitude=39.682995, longitude=140.057011, description="秋田市にある家族連れに人気の動物園"),
        Spot(name="秋田市民市場", latitude=39.719714, longitude=140.102483, description="秋田の新鮮な食材を購入できる市場"),
    ]
    rally2.spots.extend(spots_rally2)

    # データベースに追加
    db.session.add(rally1)
    db.session.add(rally2)

    # コミットして保存
    db.session.commit()

    print("データの登録が完了しました！")
