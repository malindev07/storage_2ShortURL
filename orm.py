from sqlalchemy import text, insert, select

from database import async_engine, sync_engine, session_factory, async_session_factory, Base
from models import UrlsOrm, metadata_obj, urls


class SyncORM():
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_data_orm():
        with session_factory() as session:
            url = UrlsOrm(longurl="Это лоноговая урла!", shorturl="Это короткая урла!")
            session.add(url)
            session.commit()

    @staticmethod
    def select_url():
        with session_factory() as session:
            # id_url = 1
            # first_url = session.get(UrlsOrm, id_url)
            query = select(UrlsOrm)
            res = session.execute(query)
            url_arr = res.all()

            print(f"{url_arr=}")

    @staticmethod
    def update_url(id: int = 1, new_url: str = "Это тоже новый урл"):
        with session_factory() as session:
            first_url = session.get(UrlsOrm, id)
            first_url.longurl = new_url
            session.commit()


async def insert_data_async_orm():
    async with async_session_factory() as session:
        url = UrlsOrm(longurl="Это лоноговая урла!!!", shorturl="Это короткая урла!!!")
        session.add(url)
        await  session.commit()
