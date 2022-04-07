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


class Handler:
  def __init__(self):
    self.log = {}

  def startCalcPi(self, decimal):
    print('startCalcPi with {param} parametrs'.format(param=decimal))
    return 'fcff2b31-f6a5-4c28-8e87-2a530b4cd2c4'

  def getTaskStatus(self, uuid):
    print('getTaskStatus with UUID: {uuid}'.format(uuid=uuid))
    result = calcResult()
    result.id = 'fcff2b31-f6a5-4c28-8e87-2a530b4cd2c4'
    result.pushtime = 'Thu Feb 17 00:47:22 2022'
    result.status = 'WORKED'
    result.starttime = 'Thu Feb 17 00:47:22 2022'
    result.result = 0
    return result

  def listTask(self):
    print('listTask')

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