from pydantic import BaseModel, Field
from typing import List, Dict
# from xmlrpc.client import Boolean, boolean
import datetime


class Memory(BaseModel):
	total: int
	available: int
	percent: float
	used: int
	free: int

class Partitions(BaseModel):
	device: str = Field(..., max_length=256, min_length=1)
	mountpoint: str = Field(..., max_length=20, min_length=1)
	fstype: str
	opts: str

class Interface(BaseModel):
    name: str
    upstatus: bool
    speed: int


class CommonInfo(BaseModel):
    hostname: str
    uptime: datetime.timedelta
    cpu_core: int
    cpu_load: float
    memory: Memory = None
    partitions: List [Partitions] = None
    iflist: List [Interface] = None

class PhisicalDiskCount(BaseModel):
    read_count: int
    write_count: int
    read_bytes: int
    write_bytes: int
    read_time: int
    write_time: int

class PhisicalDisks(BaseModel):
    disks: Dict[str, PhisicalDiskCount]

class CPUTimes(BaseModel):
    user: float
    system: float
    idle: float

class CPUTimesPercent(CPUTimes):
    user: float
    system: float
    idle: float

class CPUPercent(BaseModel):
    common: float
    percpu: List[float]

class NameFloat(BaseModel):
    name: str
    value: float

class NameDict(BaseModel):
    name: str
    value: Dict

class PartUsage(BaseModel):
    total: int
    used: int
    free: int
    percent: float

class PartInfo(BaseModel):
    device: str = Field(..., max_length=256, min_length=1)
    mountpoint: str = Field(..., max_length=20, min_length=1)
    fstype: str
    opts: str
    usage: PartUsage
