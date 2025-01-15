 # DB定義やデータ操作関連
from __future__ import annotations
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy import  DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, validates
from backend.app import db


class StampRally(db.Model):
    __tablename__ = "stamp_rally"
    # ラリーの ID（主キー）
    rally_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # ラリー名
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    # ラリーの説明
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    # リレーション: スポット
    spots: Mapped[list["Spot"]] = relationship("Spot", back_populates="rally", cascade="all, delete-orphan")
    #ラリー完了フラグ
    @property
    def is_completed(self) -> str:
        """
        スタンプラリーの進捗状況を計算:
        - 全て完了: 'completed'
        - 一部完了: 'in_progress'
        - 未着手: 'not_started'
        """
        # クエリで完了ステータスの統計を取得
        total_spots = db.session.query(StampStatus).filter_by(rally_id=self.rally_id).count()
        completed_spots = db.session.query(StampStatus).filter_by(rally_id=self.rally_id, is_completed=True).count()

        if total_spots == 0:
            return "not_started"  # スポットが存在しない場合は未着手
        elif completed_spots == total_spots:
            return "completed"
        elif completed_spots > 0:
            return "in_progress"
        else:
            return "not_started"


class Spot(db.Model):
    __tablename__ = "spot"
    # スポットの ID（主キー）
    spot_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # 紐づくラリーの ID（外部キー）
    rally_id: Mapped[int] = mapped_column(ForeignKey("stamp_rally.rally_id"), nullable=False)
    # スポット名
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    # 緯度
    latitude: Mapped[float] = mapped_column(nullable=False)
    # 経度
    longitude: Mapped[float] = mapped_column(nullable=False)
    # スポットの説明
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    stamp_statuses: Mapped[list["StampStatus"]] = relationship("StampStatus", back_populates="spot")
    rally = relationship("StampRally", back_populates="spots")


class StampStatus(db.Model):
    __tablename__ = "stamp_status"
    status_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    spot_id: Mapped[int] = mapped_column(ForeignKey("spot.spot_id"), nullable=False)
    rally_id: Mapped[int] = mapped_column(ForeignKey("stamp_rally.rally_id"), nullable=False)
    is_completed: Mapped[bool] = mapped_column(default=False)
    spot: Mapped["Spot"] = relationship("Spot", back_populates="stamp_statuses")
    rally: Mapped["StampRally"] = relationship("StampRally")

