import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import text


class Db_Connection:
    def obj_to_dict(self, obj):
        objects_dict = {}
        obj_nr = 1

        result_list = obj.scalars().all()
        for result_single in result_list:
            attr_list = sqlalchemy.inspect(result_single).mapper.column_attrs
            object_dict = {}
            for attr_single in attr_list:
                object_dict[attr_single.key] = getattr(result_single, attr_single.key)

            objects_dict[obj_nr] = object_dict
            obj_nr += 1

        return objects_dict

    async def get_all_from_db(self, input_type):
        # Fragt alle Daten aus der Datenbank ab, die Tabelle hängt vom eingehenden Datentyp ab
        engine = create_async_engine(
            "DATABASECONNECTION", echo=False
        )
        async with AsyncSession(engine) as session:
            stmt = select(type(input_type))
            res = await session.execute(stmt)
        await engine.dispose()
        return self.obj_to_dict(res)

    async def get_filtered_from_db(self, input_type, input_filter):
        # Fragt alle Daten aus der Datenbank ab, die Tabelle hängt vom eingehenden Datentyp ab, und filtert diese nach dem gegebenen Filter
        # Bsp: input_filter = {"type": "1"}

        engine = create_async_engine(
            "DATABASECONNECTION", echo=False
        )
        async with AsyncSession(engine) as session:
            # stmt = select(type(input_type)).where(**input_filter)
            stmt = select(type(input_type)).where(text(input_filter))
            res = await session.execute(stmt)
        await engine.dispose()
        return self.obj_to_dict(res)

