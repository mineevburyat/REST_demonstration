from shema import *
import datetime, psutil, socket

def _getHostname():
  return socket.gethostname()

def _getUptime():
  return datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())

def getMemory():
  return Memory(**psutil.virtual_memory()._asdict())

def getPartList():
  parts = []
  for partitions in psutil.disk_partitions():
    parts.append(Partitions(**partitions._asdict()))
  return parts

def getInterfaceList():
  interfaces = []
  for if_name, if_status in psutil.net_if_stats().items():
    interface = Interface(name=if_name, upstatus=if_status.isup, speed=if_status.speed)
    interfaces.append(interface)
  return interfaces

def getInfo():
  return CommonInfo(hostname = _getHostname(),
    uptime = _getUptime(), 
    cpu_core = psutil.cpu_count(True),
    cpu_load = psutil.cpu_percent(interval=1),
    memory = getMemory(),
    partitions=getPartList(),
    iflist = getInterfaceList())

def updateInfo(hostconf):
  hostconf.uptime = _getUptime()
  hostconf.cpu_load = psutil.cpu_percent()
  hostconf.memory = getMemory()
  hostconf.partitions = getPartList()
  return hostconf

def getPhisicalDisk():
  result = {}
  for disk, disk_count in psutil.disk_io_counters(perdisk=True).items():
    result[disk] = (PhisicalDiskCount(**disk_count._asdict()))
  return result

def getCPUTimes(id=None):
  result = {}
  items = psutil.cpu_times(percpu=True)
  if id is None:
    index = 0
    for cpu in items:
      result["cpu{i}".format(i=index)] = CPUTimes(**cpu._asdict())
      index += 1
  else:
    index = id
    result["cpu{i}".format(i=index)] = CPUTimes(**items[index]._asdict())
  return result

def getCPUTimesPercent(id=None):
  result = {}
  items = psutil.cpu_times_percent(percpu=True)
  if id is None:
    index = 0
    for cpu in items:
      result[index] = CPUTimesPercent(**cpu._asdict())
      index += 1
    return result
  else:
    index = id
    return NameDict(name="cpu{i}".format(i=index), value = CPUTimesPercent(**items[index]._asdict()))
  

def getCPUPercent(id=None):
  common_percent = psutil.cpu_percent()
  list_percent = psutil.cpu_percent(percpu=True)
  if id is None:
    return CPUPercent(common=common_percent, percpu=list_percent)
  else:
    return NameFloat(name="cpu{i}".format(i=id), value=list_percent[id])

def getPartitionUsage():
  partwithfs = []
  result = []
  for part in getPartList():
    if part.fstype != "":
      partwithfs.append(part)
  print(partwithfs)
  for workpart in partwithfs:
    usagestat = PartUsage(**psutil.disk_usage(workpart.mountpoint)._asdict())
    result.append(PartInfo(usage=usagestat, **workpart.dict()))
  return result
