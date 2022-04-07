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
    result = calcPi.delay(decimal)
    fileresult = {'id': result.id, 'status': "WAITING", 'pushtime': datetime.datetime.now().strftime('%c')}
    with open('results/'+result.id, 'w') as f:
        json.dump(fileresult, f)
    print('[Server] startCalcPi({param}) - task UUID: {uuid}'.format(param=decimal, uuid=result.id))
    return result.id

  def getTaskStatus(self, uuid):
    try:
        with open('results/' + uuid, 'rb') as f:
            fresult = json.load(f)
    except FileNotFoundError:
        return {'error': "tasks not found"}
    print('getTaskStatus with UUID: {uuid}. Result: {fresult}'.format(uuid=uuid, fresult=fresult))
    result = calcResult(**fresult)
    # result.id = fresult.id
    # result.pushtime = fresult.pushtime
    # result.status = fresult.status
    # result.starttime = fresult.starttime
    # result.result = fresult.result
    return result

  def listTask(self):
    files = os.listdir('results')
    results = []
    for file in files:
        with open('results/'+file, 'r') as f:
          task = json.load(f)
          results.append(calcResult(**task))
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