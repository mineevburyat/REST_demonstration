from .celery import app
from time import sleep
import json, datetime

@app.task(bind=True)
def calcPi(self, decimal:int):
  accuracy = {2: 1000, 3: 10000, 4: 100000, 5: 1000000, 6: 10000000, 7: 100000000, 8: 1000000000, 9:10000000000}
  sleepConst = { 2: 1.5, 3: 1, 4: 1, 5: 0.5}
  # print(decimal)
  if decimal > 9:
    decimal = 9
  if decimal < 2:
    decimal = 2
  summa = 1
  percent = 0
  sleepVar = 0
  id = self.request.id
  file_id = 'results/' + id
  selfresult = {'starttime': datetime.datetime.now().strftime('%c'),
                'status': "PROGRESS",
                'result': {'percent': 0, 'intermediate': 3}}
  with open(file_id, 'w') as f:
        json.dump(selfresult, f)
  # percentwork
  _halfpercent = accuracy[decimal] * 0.005
  _maxrange = accuracy[decimal]
  # slepping for speed calc
  if decimal < 6:
    sleepVar = sleepConst[decimal]
  for i in range(1,_maxrange):
    summa += pow(-1, i) / (2*i + 1)
    if i % _halfpercent == 0:
      percent += 0.5
      selfresult['result'] = {'percent': percent, 'intermediate': round(summa*4, decimal)}
      with open(file_id, 'w') as f:
        json.dump(selfresult, f)
      sleep(sleepVar)
  selfresult['status'] = "SUCCESS"
  selfresult['result'] = round(summa * 4, decimal)
  selfresult['stoptime'] = datetime.datetime.now().strftime('%c')
  with open(file_id, 'w') as f:
        json.dump(selfresult, f)