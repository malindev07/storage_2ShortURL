from sqlalchemy import Table, Column, Integer, String, MetaData
from database import Base
from sqlalchemy.orm import Mapped, mapped_column


class UrlsOrm(Base):
    __tablename__ = "urls"
    id: Mapped[int] = mapped_column(primary_key=True)
    longurl: Mapped[str] = mapped_column(String(30))
    shorturl: Mapped[str] = mapped_column(String(30))


metadata_obj = MetaData()

# urls = Table(
#     "urls",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("longurl", String),
#     Column("shorturl", String)
# )
