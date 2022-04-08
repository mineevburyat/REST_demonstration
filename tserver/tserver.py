# import glob
import sys
sys.path.append('gen-py')
# sys.path.insert(0, glob.glob('../../lib/py/build/lib*')[0])
from RPC import RPCcelery
from RPC.RPCcelery import Client
from RPC.ttypes import calcResult
# from shared.ttypes import SharedStruct

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from calcpicelery.tasks import calcPi
import datetime
import json
import os

class Handler:
  def __init__(self):
    self.log = {}

  def startCalcPi(self, decimal):
    task = calcPi.delay(decimal)
    fileresult = {'id': task.id, 'status': "WAITING", 'pushqtime': datetime.datetime.now().strftime('%c')}
    with open('results/' + task.id, 'w') as f:
        json.dump(fileresult, f)
    print('[Server] startCalcPi({param}) - task UUID: {uuid}'.format(param=decimal, uuid=task.id))
    return task.id

  def getTaskStatus(self, uuid):
    try:
        with open('results/' + uuid, 'rb') as f:
            fresult = json.load(f)
    except FileNotFoundError:
        return {'error': "tasks not found"}
    print('[Server] getTaskStatus with UUID: {uuid}. \n[Server]Result: {fresult}'.format(uuid=uuid, fresult=fresult))
    result = calcResult(**fresult)
    print(result)
    return result
    # result.id = fresult.id
    # result.pushtime = fresult.pushtime
    # result.status = fresult.status
    # result.starttime = fresult.starttime
    # result.result = fresult.result
    # return result

  def listTasks(self):
    files = os.listdir('results')
    results = []
    for file in files:
        with open('results/'+file, 'r') as f:
          fresult = json.load(f)
          results.append(calcResult(**fresult))
    return results

  def ping(self):
    print('ping()')


if __name__ == '__main__':
  handler = Handler()
  processor = RPCcelery.Processor(handler)
  transport = TSocket.TServerSocket(host='0.0.0.0', port=9000)
  tfactory = TTransport.TBufferedTransportFactory()
  pfactory = TBinaryProtocol.TBinaryProtocolFactory()

  # server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

  # You could do one of these for a multithreaded server
  server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
  # server = TServer.TThreadPoolServer(
  #     processor, transport, tfactory, pfactory)

  print('Starting the server...')
  server.serve()
  print('done.')