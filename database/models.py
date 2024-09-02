import datetime

from sqlalchemy import func
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Model = declarative_base()


class Task(Model):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    status: Mapped[str] = mapped_column(nullable=False)
    create_time: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    start_time: Mapped[datetime.datetime] = mapped_column(nullable=True)
    execute_to_time: Mapped[int] = mapped_column(nullable=True)
