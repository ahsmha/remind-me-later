import sqlalchemy as sa
import sqlalchemy.orm as so
from datetime import datetime, date, timezone
from flask import jsonify
from app import db

class Message(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    message: so.Mapped[str] = so.mapped_column(sa.String(140))
    message_time: so.Mapped[datetime] = so.mapped_column(sa.String(140))
    message_date: so.Mapped[date] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(sa.DateTime, index=True, default=lambda: datetime.now(timezone.utc))

    def from_dict(self, data):
        for field in ['message', 'message_time', 'message_date']:
            if field in data:
                setattr(self, field, data[field])
        setattr(self, 'timestamp', datetime.now(timezone.utc))

    def create_tables():
        db.create_all()
