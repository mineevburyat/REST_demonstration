from fastapi import FastAPI, Path
import uvicorn
from shema import CPUPercent, PartInfo, CPUTimesPercent


import json
import datetime
import os

app = FastAPI()

#заглушка
result = '{"id":"test-fcff2b31-f6a5-4c28-8e87-2a530b4cd2c4", "status": "SUCCESS", "pushqtime": "Thu Feb 17 00:47:22 2022", "starttime": "Thu Feb 17 00:47:22 2022", "result": 3.14159, "stoptime": "Thu Feb 17 00:49:08 2022"}'

@app.get('/',)
async def home():
    return "show info"

@app.get('/leibnic/{decimal}')
async def leibnic_method_calc_from_celery(decimal: int):
    #запуск клиента thrift и запрос на RPC calcPI в ответ получаем json result задачи
    # result = calcPi.delay(decimal)
    return result

@app.get("/tasks/{task_id}")
async def get_status_task(task_id: str):
    #запуск клиента thrift и запрос на RPC calcPI в ответ получаем json result задачи
    # result = calcPi.delay(decimal)
    return result

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
