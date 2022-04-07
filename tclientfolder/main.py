from fastapi import FastAPI, Path
import uvicorn
from shema import resultTask
from tclient import *

import json
import datetime
import os

app = FastAPI()

@app.get('/',)
async def home():
    return "show info"

@app.get('/calcpi/{decimal}')
async def calc_pi_in_celery(decimal: int):
    # запуск клиента thrift, который передаст RPC на thrift server и получит uuid задачи
    # result = calcPi.delay(decimal)
    result = startCalcPi(decimal)
    return result

@app.get("/task/{task_id}")
async def get_status_task(task_id: str):
    # запуск клиента thrift, который передаст RPC на thrift server и получит result задачи с заданным uuid
    # result = calcPi.delay(decimal)
    result = getTaskStatus(task_id)
    # print(result)
    return result

@app.get('/alltasks/')
async def get_tasks_list():
    return listTask()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
