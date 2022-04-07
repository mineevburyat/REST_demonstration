import sys
sys.path.append('gen-py')
# import glob
# sys.path.insert(0, glob.glob('../../lib/py/build/lib*')[0])

from RPC import RPCcelery
from RPC.ttypes import calcResult

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def startCalcPi(decimal):
  # Make socket
  transport = TSocket.TSocket('tserver', 9000)
  # Buffering is critical. Raw sockets are very slow
  transport = TTransport.TBufferedTransport(transport)
  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  # Create a client to use the protocol encoder
  client = RPCcelery.Client(protocol)
  # Connect!
  transport.open()
  #do task
  uuid = client.startCalcPi(decimal)
  transport.close()
  return uuid

def getTaskStatus(uuid):
  # Make socket
  transport = TSocket.TSocket('tserver', 9000)
  # Buffering is critical. Raw sockets are very slow
  transport = TTransport.TBufferedTransport(transport)
  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  # Create a client to use the protocol encoder
  client = RPCcelery.Client(protocol)
  # Connect!
  transport.open()
  #do task
  result = client.getTaskStatus(uuid)
  transport.close()
  return result

def listTask():
  # Make socket
  transport = TSocket.TSocket('tserver', 9000)
  # Buffering is critical. Raw sockets are very slow
  transport = TTransport.TBufferedTransport(transport)
  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  # Create a client to use the protocol encoder
  client = RPCcelery.Client(protocol)
  # Connect!
  transport.open()
  #do task
  result = client.listTasks()
  transport.close()
  return result