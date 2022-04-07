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
    return '{"id": "{result}"}'.format(result=result)

@app.get("/task/{task_id}")
async def get_status_task(task_id: str):
    # запуск клиента thrift, который передаст RPC на thrift server и получит result задачи с заданным uuid
    # result = calcPi.delay(decimal)
    result = getTaskStatus(task_id)
    return resultTask(**result)

@app.get('/alltasks/')
async def get_tasks_list():
    return "list of tasks"


@app.get('/cpu/times_percent')
async def cpu_times_percent():
    return "getCPUTimesPercent()"

@app.get('/cpu/percent')
async def cpu_percent():
    return "getCPUPercent()"

@app.get('/partitions/usage')
async def partition_usage():
    return "getPartitionUsage()"

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
