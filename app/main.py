from time import sleep
from typing import Union
import uuid

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World", 'say': 'hello'}

@app.get("/proccess")
async def test_proccess():
    my_uuid = uuid.uuid4()
    my_uuid = str(my_uuid)

    print('first : '+my_uuid)
    sleep(5)
    print('end : '+my_uuid)
    return {"Hello": "World", 'uid': my_uuid}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q, 'say': "hi"}


@app.get("/query")
async def read_query(skip: int = 0, limit: int = 10):
    fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
    return fake_items_db[skip : skip + limit]