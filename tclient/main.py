from fastapi import FastAPI, Path
import uvicorn
from tclient.shema import CPUPercent, PartInfo, CPUTimesPercent
from tserver.monitoring import *
from calcpicelery.tasks import calcPi
import json
import datetime
import os

app = FastAPI()

hostconf = getInfo()
@app.get('/', response_model=CommonInfo)
async def home():
    return updateInfo(hostconf)

@app.get('/leibnic/{decimal}')
async def leibnic_method_calc_from_celery(decimal: int):
    result = calcPi.delay(decimal)
    selfresult = {'status': "WAITING", 'pushqtime': datetime.datetime.now().strftime('%c')}
    with open('results/'+result.id, 'w') as f:
        json.dump(selfresult, f)
    return {'id': result.id}

@app.get("/tasks/{task_id}")
async def get_status_task(task_id: str):
    try:
        with open('results/' + task_id, 'rb') as f:
            fresults = json.load(f)
    except FileNotFoundError:
        return {'error': "tasks not found"}
    return {**fresults}

@app.get('/alltasks/')
async def get_tasks_list():
    files = os.listdir('results')
    results = {}
    for file in files:
        with open('results/'+file, 'r') as f:
            results[file] = json.load(f)
    return results


@app.get('/cpu/times_percent', response_model=Dict[int, CPUTimesPercent])
async def cpu_times_percent():
    return getCPUTimesPercent()

@app.get('/cpu/percent', response_model=CPUPercent)
async def cpu_percent():
    return getCPUPercent()

@app.get('/partitions/usage', response_model=List[PartInfo])
async def partition_usage():
    return getPartitionUsage()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")