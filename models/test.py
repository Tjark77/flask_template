from flask import jsonify
from models import objects
from models.database import Db_Connection


class Test:

    db_con = Db_Connection()

    async def get_all_data_from_db(self):
        example = objects.Example()
        return jsonify(await self.db_con.get_all_from_db(example))

    async def get_filtered_data_from_db(self, input_id):
        example = objects.Example()
        # Erstellt den Filter für die Query
        filter_obj = "id=" + input_id
        return jsonify(
            await self.db_con.get_filtered_from_db(example, filter_obj)
        )
    
    async def get_json_string(self):
        examples = [{'id': 1, 'name': 'foo'}, {'id': 2, 'name': 'bar'}]
        return jsonify(examples)

    async def get(self):
        print("Funktionsaufruf models/test.py get()")
        return await self.get_json_string()
    
    async def post(self, input):
        print("Funktionsaufruf models/test.py post()")
        print(input)
        return await self.get_json_string()