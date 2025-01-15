from backend.models import db, StampStatus,StampRally, Spot
from backend.app import create_app


app = create_app()

with app.app_context():
    
    # データベースをリセット
    db.drop_all()
    db.create_all()

    
    # テスト用に登録
    rally1 = StampRally(name="テスト", description="テスト")
    spots_rally1 = [
        Spot(name="新宿駅", latitude=35.690129, longitude=139.700571, description=""),
        Spot(name="ひみつ", latitude=35, longitude=135, description=""),
    ]
    rally1.spots.extend(spots_rally1)

    # テスト用に登録2コンプリート用
    test_rally = StampRally(name="テスト2", description="テスト2")
    test_spot_rally = [
        Spot(name="京都", latitude=35, longitude=135, description=""),
        Spot(name="ひみつ", latitude=35, longitude=135, description=""),
    ]
    test_rally.spots.extend(test_spot_rally)
    
    # スタンプラリー 1: さいたま市
    rally2 = StampRally(name="さいたま市スタンプラリー", description="さいたま市内の観光スポットを巡るラリー")

    # さいたま市スポット
    spots_rally2 = [
        Spot(name="さいたま市役所", latitude=35.861729, longitude=139.645482, description="さいたま市の行政機関所在地"),
        Spot(name="埼玉スタジアム2002", latitude=35.905808, longitude=139.717037, description="サッカー専用の国内最大級のスタジアム"),
        Spot(name="もみじ公園", latitude=35.846546, longitude=139.673109, description="さいたま市の公園"),
        Spot(name="さいたま市民医療センター", latitude=35.881917, longitude=139.598223, description="病院"),
        Spot(name="文明堂さいたまあおぞら工房", latitude=35.881129, longitude=139.59849, description="お菓子屋さん"),
        Spot(name="パティスリーＭＯＡ", latitude=35.853847, longitude=139.67436, description="ケーキ屋さん"),
    ]
    rally2.spots.extend(spots_rally2)


    # スタンプラリー: 函館スタンプラリー
    rally_hakodate = StampRally(name="函館スタンプラリー", description="函館市内の観光スポットを巡るラリー")
    spots_hakodate = [
        Spot(name="café D'ici", latitude=41.7619165656088, longitude=140.71546285581877, description="カフェ"),
        Spot(name="旧函館区公会堂", latitude=41.765293954105985, longitude=140.70906354269226, description="異国情緒あふれる建物"),
        Spot(name="ハセガワストア", latitude=41.76587987924099, longitude=140.71507639189474, description="やきとり弁当がおいしい！"),
        Spot(name="パリジア", latitude=41.78992945737932, longitude=140.7446683568185, description="カフェ"),
        Spot(name="金森倉庫", latitude=41.76665271646128, longitude=140.71634551014856, description="ショッピングモール")
    ]
    rally_hakodate.spots.extend(spots_hakodate)

    # スタンプラリー: 仙台おすすめスポット
    rally_sendai = StampRally(name="仙台おすすめスポット", description="仙台市内の人気スポットを巡るラリー")
    spots_sendai = [
        Spot(name="青山文庫", latitude=38.261294871866795, longitude=140.87877456656162, description="本が読めるカフェ"),
        Spot(name="CHICCI", latitude=38.25668119218366, longitude=140.87376224041284, description="チーズケーキが美味しいカフェ"),
        Spot(name="HEY", latitude=38.25793084725114, longitude=140.8686198953971, description="ドーナツがかわいいカフェ"),
        Spot(name="フォーラム仙台", latitude=38.27288044898135, longitude=140.86675036656234, description="レトロな映画館"),
        Spot(name="山の洋食屋ざびえる", latitude=38.26271482374395, longitude=140.8461424953975, description="牛タンシチューが美味しい")
    ]
    rally_sendai.spots.extend(spots_sendai)

    # スタンプラリー: 京都おすすめスポット
    rally_kyoto = StampRally(name="京都おすすめスポット", description="京都市内のおすすめグルメスポット")
    spots_kyoto = [
        Spot(name="菓子工房&Sweets Cafe KYOTO KEIZO", latitude=35.0086433, longitude=135.7498018, description="10分モンブランが有名"),
        Spot(name="魏飯夷堂 三条店", latitude=35.0086927, longitude=135.7506829, description="小籠包が美味しい"),
        Spot(name="グリルデミ", latitude=35.0147779, longitude=135.7584955, description="ハンバーグが美味しい"),
        Spot(name="fiveran", latitude=35.0089737, longitude=135.7578655, description="美味しいパン屋")
    ]
    rally_kyoto.spots.extend(spots_kyoto)

    # スタンプラリー: 大阪スタンプラリー
    rally_osaka = StampRally(name="大阪スタンプラリー", description="大阪市内の観光スポットを巡るラリー")
    spots_osaka = [
        Spot(name="中之島美術館", latitude=34.69241263, longitude=135.49123275, description=""),
        Spot(name="日本聖公会川口基督教会", latitude=34.6821225, longitude=135.4821734, description="ステンドグラスがきれい"),
        Spot(name="海遊館", latitude=34.6545245, longitude=135.428913, description="ジンベエザメがいます"),
        Spot(name="喫茶アメリカン", latitude=34.8404418, longitude=135.6822745, description="純喫茶"),
        Spot(name="あべのハルカス", latitude=34.6460823, longitude=135.5132966, description="展望台と美術館おすすめ")
    ]
    rally_osaka.spots.extend(spots_osaka)

    # データベースに追加
        # データベースに追加
    db.session.add(rally1)
    db.session.add(test_rally)
    db.session.add(rally2)
    db.session.add(rally_hakodate)
    db.session.add(rally_sendai)
    db.session.add(rally_kyoto)
    db.session.add(rally_osaka)

     # 各スポットに対応するStampStatusを追加
    all_spots = Spot.query.all()
    for spot in all_spots:
        stamp_status = StampStatus(spot=spot, rally=spot.rally, is_completed=False)
        db.session.add(stamp_status)

    # コミットして保存
    db.session.commit()

    print("データの登録が完了しました！")